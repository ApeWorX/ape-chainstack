from ape import plugins

from .providers import Chainstack

NETWORKS = [
    "ethereum",
    "ropsten",
    "rinkeby",
    "goerli",
]


@plugins.register(plugins.ProviderPlugin)
def providers():
    for network_name in NETWORKS:
        yield  "ethereum", network_name, Chainstack
