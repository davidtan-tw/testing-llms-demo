# Testing LLMs Demo

A demo with examples on how to write automated tests (LLM-based tests) for LLM applications.  

## Setup

Run the go script to install pre-requisite dependencies. The go script will install Python 3 and Poetry, and create a virtual environment on the host. 

```shell script
# mac users
scripts/go/go-mac.sh
```

Configure your IDE to use the python virtual environment created in the go script. 
- [PyCharm instructions](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html#existing-environment)
- [VS Code instructions](https://code.visualstudio.com/docs/python/environments)

## Tasks that you can run

```sh
```shell script
# Activate virtual environment
poetry shell

# Define OPENAI_API_KEY. The example depends/calls on OpenAI models
export OPENAI_API_KEY="your key here"

# Smoke test to check everything works
python main.py

# Run automated tests
./scripts/test-llm.sh
```