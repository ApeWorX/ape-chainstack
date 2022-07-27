# Ape Chainstack Plugin

Chainstack Provider plugins for networks.

This plugin allows you to use the ApeWorX framework with Chainstack as a node provider, in an easy and integrated way.

ApeWorX is a smart contract development and testing framework. It is inspired by Brownie, and it has essentially the same syntax, but ApeworX focuses on a more modular approach, and it allows us to build and use external plugins to add functionality.  

## Requirements

- Linux or macOS 
- Windows Subsystem Linux ([WSL](https://docs.microsoft.com/en-us/windows/wsl/install)) if operating on windows. 

## Dependencies

* [python3](https://www.python.org/downloads) version 3.7.2 or greater
* python3-dev
  * MacOS. Should already have the [correct headers if Python is installed with ```brew```](https://stackoverflow.com/questions/32578106/how-to-install-python-devel-in-mac-os)   
  
  * Linux. Install python3-dev with:
  
  ```sh
  sudo apt-get install python3-dev
  ```


>**Note:** Always check the [ApeWorX docs to find the updated requirements](https://docs.apeworx.io/ape/stable/userguides/quickstart.html#prerequisite).

## Installation

Verify the Python version installed:

```sh
Python3 --version 
```

### Virtual environment

It is recommended to operate in a virtual environment; you will need to [install ApeWorX](https://github.com/ApeWorX/ape#installation) in the virtual environment if you decide to use one.

Create a virtual environment. 

```sh
python3 -m venv /path/to/new/environment 
```

> Keep in mind that you can place the virtual environment where you prefer. 

Then activate it. 

```sh
source /bin/activate 
```

### Install ape-chainstack via `pip`

You can install the latest release via [`pip`](https://pypi.org/project/pip/):

```bash
pip install ape-chainstack
```

### Install ape-chainstack via `setuptools`

You can clone the repository and use [`setuptools`](https://github.com/pypa/setuptools) for the most up-to-date version:

```bash
git clone https://github.com/ApeWorX/ape-chainstack.git
cd ape-chainstack
python3 setup.py install
```

## Quick Usage

Use in most commands using the `--network` option:

```bash
ape console --network ethereum:ropsten:chainstack
```

## Development

This project is in development and should be considered a beta.
Things might not be in their final state and breaking changes may occur.
Comments, questions, criticisms and pull requests are welcomed.

## License

This project is licensed under the [Apache 2.0](LICENSE).
