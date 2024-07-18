from typing import Dict, List

API_KEY_ENV_KEY_MAP = {
    "avalanche": "AVALANCHE_CHAINSTACK_API_KEY",
    "arbitrum": "ARBITRUM_CHAINSTACK_API_KEY",
    "base": "BASE_CHAINSTACK_API_KEY",
    "ethereum": "ETH_CHAINSTACK_API_KEY",
    "fantom": "FANTOM_CHAINSTACK_API_KEY",
    "optimism": "OPTIMISM_CHAINSTACK_API_KEY",
    "polygon": "POLYGON_CHAINSTACK_API_KEY",
    "bsc": "BSC_CHAINSTACK_API_KEY",
}

NETWORKS: Dict[str, List[str]] = {
    "avalanche": ["mainnet", "fuji"],
    "arbitrum": ["mainnet", "sepolia"],
    "base": ["mainnet", "sepolia"],
    "ethereum": ["mainnet", "holesky", "sepolia"],
    "fantom": ["mainnet", "opera"],
    "optimism": ["mainnet", "sepolia"],
    "polygon": ["mainnet", "amoy"],
    "bsc": ["mainnet", "testnet"],
}
