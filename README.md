# Quick Start

Chainstack network provider plugins.

This plugin allows using the Ape framework with Chainstack as a node provider in an easy and integrated way.

## Dependencies

- [python3](https://www.python.org/downloads) version 3.9 up to 3.12.

## Installation

### via `pip`

You can install the latest release via [`pip`](https://pypi.org/project/pip/):

```bash
pip install ape-chainstack
```

### via `setuptools`

You can clone the repository and use [`setuptools`](https://github.com/pypa/setuptools) for the most up-to-date version:

```bash
git clone https://github.com/ApeWorX/ape-chainstack.git
cd ape-chainstack
python3 setup.py install
```

## Quick Usage

## Set up the environment

Follow these steps to sign up on Chainstack, deploy a node, and find your endpoint credentials:

1. [Sign up with Chainstack](https://console.chainstack.com/user/account/create).
1. [Deploy a node](https://docs.chainstack.com/platform/join-a-public-network).
1. [View node access and credentials](https://docs.chainstack.com/platform/view-node-access-and-credentials).


Create an environment variable with your Chainstack node URL in this format `CHAINSTACK_"NETWORK"_URL=ENDPOINT_URL`; for example:

```sh
export CHAINSTACK_GOERLI_URL=https://nd-11X-26X-16X.p2pify.com/YOUR_API_KEY
```

Use the command `ape networks list` to see the networks available:

```sh
ethereum  (default)
├── holesky
│   ├── chainstack
│   └── node  (default)
├── local  (default)
│   ├── node
│   └── test  (default)
├── mainnet
│   ├── chainstack
│   └── node  (default)
└── sepolia
    ├── chainstack
    └── node  (default)
```

Use the `--network` command to access the console using your node; for example:

```bash
ape console --network ethereum:sepolia:chainstack
```

Check the Ape docs to see [how to select a network](https://docs.apeworx.io/ape/stable/userguides/networks.html).

Now you are ready to use Ape to develop and test your smart contract, checkout the [Ape Academy](https://academy.apeworx.io/) for tutorials.

## Development

This project is in development and should be considered a beta.
Things might not be in their final state and breaking changes may occur.
