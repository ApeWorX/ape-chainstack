from ape import plugins

from .providers import Chainstack

ETH_NETWORKS = [
    "mainnet",
    "ropsten",
    "rinkeby",
]


@plugins.register(plugins.ProviderPlugin)
def providers():
    for network_name in ETH_NETWORKS:
        yield "ethereum", network_name, Chainstack
