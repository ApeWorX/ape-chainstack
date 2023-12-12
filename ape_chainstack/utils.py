from typing import Dict, List

API_KEY_ENV_KEY_MAP = {
    "base": "BASE_CHAINSTACK_API_KEY",
    "ethereum": "ETH_CHAINSTACK_API_KEY",
    "gnosis": "GNOSIS_CHAINSTACK_API_KEY",
    "optimism": "OPTIMISM_CHAINSTACK_API_KEY",
    "polygon": "POLYGON_CHAINSTACK_API_KEY",
}

NETWORKS: Dict[str, List[str]] = {
    "base": ["mainnet", "goerli", "sepolia"],
    "ethereum": ["mainnet", "ropsten", "rinkeby", "goerli", "sepolia"],
    "gnosis": ["mainnet", "chiado"],
    "optimism": ["mainnet", "goerli", "sepolia"],
    "polygon": ["mainnet"],
}
