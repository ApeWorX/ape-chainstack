from ape import plugins

from .providers import Chainstack
from .utils import NETWORKS


@plugins.register(plugins.ProviderPlugin)
def providers():
    for ecosystem_name in NETWORKS:
        for network_name in NETWORKS[ecosystem_name]:
            yield ecosystem_name, network_name, Chainstack
