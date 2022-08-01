from ape import plugins

from .providers import ETH_NETWORKS, Chainstack


@plugins.register(plugins.ProviderPlugin)
def providers():
    for network_name in ETH_NETWORKS:
        yield "ethereum", network_name, Chainstack
