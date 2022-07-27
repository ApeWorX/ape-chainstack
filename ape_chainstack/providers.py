import os

from ape.api import Web3Provider
from ape.exceptions import ProviderError
from web3 import HTTPProvider, Web3
from web3.middleware import geth_poa_middleware


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
