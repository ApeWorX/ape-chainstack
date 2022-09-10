from ape import plugins

from .providers import ChainstackProvider

NETWORKS = {
    "ethereum": [
        "mainnet",
        "ropsten",
        "rinkeby",
        "goerli",
    ],
    "polygon": [
        "mainnet",
        "mumbai",
    ],
}


@plugins.register(plugins.ProviderPlugin)
def providers():
    for ecosystem_name in NETWORKS:
        for network_name in NETWORKS[ecosystem_name]:
            yield ecosystem_name, network_name, ChainstackProvider

