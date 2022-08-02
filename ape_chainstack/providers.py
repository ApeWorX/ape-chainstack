import os

from ape.api import Web3Provider
from ape.exceptions import ContractLogicError, ProviderError, VirtualMachineError
from web3 import HTTPProvider, Web3
from web3.exceptions import ContractLogicError as Web3ContractLogicError
from web3.middleware import geth_poa_middleware

ETH_NETWORKS = [
    "mainnet",
    "ropsten",
    "rinkeby",
    "goerli",
]

_ENVIRONMENT_VARIABLE_NAMES = [f"CHAINSTACK_{network.upper()}_URL" for network in ETH_NETWORKS]


class ChainstackProviderError(ProviderError):
    """
    An error raised in the Chainstack ape provider plugin.
    """


class Chainstack(Web3Provider):
    """
    A simple implementation for the ProviderAPI for using Chainstack in ape.
    https://chainstack.com/
    """

    @property
    def url(self) -> str:
        """
        The Chainstack node URL.
        Each Chainstack node runs a single networks.
        """

        env_var_key = f"CHAINSTACK_{self.network.name.upper()}_URL"
        env_var = os.getenv(env_var_key)
        if not env_var:
            raise ChainstackProviderError(f"Missing environment variable '{env_var_key}'")

        return env_var

    def connect(self):
        """
        Connect a web3.py instance to your Chainstack node.
        """

        self._web3 = Web3(HTTPProvider(self.url))
        if self._web3.eth.chain_id in (4, 5, 42):
            self._web3.middleware_onion.inject(geth_poa_middleware, layer=0)

        return super().connect()

    def disconnect(self):
        """
        Terminate the connection.
        """

        self._web3 = None
        return super().disconnect()

    def get_virtual_machine_error(self, exception: Exception) -> VirtualMachineError:
        if not hasattr(exception, "args") or not len(exception.args):
            return VirtualMachineError(base_err=exception)

        args = exception.args
        message = args[0]
        if (
            not isinstance(exception, Web3ContractLogicError)
            and isinstance(message, dict)
            and "message" in message
        ):
            # Is some other VM error, like gas related
            return VirtualMachineError(message=message["message"])

        elif not isinstance(message, str):
            return VirtualMachineError(base_err=exception)

        # If get here, we have detected a contract logic related revert.
        message_prefix = "execution reverted"
        if message.startswith(message_prefix):
            message = message.replace(message_prefix, "")

            if ":" in message:
                # Was given a revert message
                message = message.split(":")[-1].strip()
                return ContractLogicError(revert_message=message)
            else:
                # No revert message
                return ContractLogicError()

        return VirtualMachineError(message=message)
