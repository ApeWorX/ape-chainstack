import pytest
from ape import networks

from ape_chainstack.providers import Chainstack, ChainstackProviderError


@pytest.mark.skip("Wait until CI env is setup")
def test_provider_ropsten():
    # NOTE: env running test must have a key set for the network
    # EXAMPLE: CHAINSTACK_ROPSTEN_URL=https://<address here>.com/<key>
    with networks.ethereum.ropsten.use_provider("chainstack") as provider:
        assert isinstance(provider, Chainstack)
        assert provider.get_balance("0x0000000000000000000000000000000000000000") > 0


def test_when_no_api_key_raises_error():
    with pytest.raises(ChainstackProviderError) as err:
        with networks.ethereum.mainnet.use_provider("chainstack"):
            pass

    expected = "Missing environment variable 'CHAINSTACK_MAINNET_URL'"
    assert expected in str(err.value)
