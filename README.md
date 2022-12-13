# labs-101

This repository contains the material for the Dapr Labs 101 workshop. The workshop is designed to be a hands-on introduction to Dapr in the self-hosted mode (without any of the Kubernetes stuff). It is intended for developers who are new to Dapr, and introduces three primary building blocks - 
1. State management - Learn how to manage key/value pairs using the state API
1. Pub/Sub - Learn how to publish and subscribe to messages from your application
1. Service invocation - Learn how Dapr allows service to service invocation in a secured way and supports built-in service discovery and distributed tracing
 
In these labs, you will be using cURL to make API calls and using Dapr quick-starts to explore Dapr capabilities. At the end of each lab, you will also explore how applications are written using Dapr SDKs (with programming language of your choice). Navigate to the [labs](./labs) folder and get started!

## Prerequisites

1. If you are running Windows, please install [WSL2 Install WSL | Microsoft Learn](https://learn.microsoft.com/en-us/windows/wsl/install)
1. Git and a GitHub account - [Git - Downloading Package (git-scm.com)](https://git-scm.com/download/win), [GitHub](https://github.com/)
1. Visual studio code - [Visual Studio Code - Code Editing. Redefined](https://code.visualstudio.com/) with Jupyter extension - [Jupyter Extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) and WSL extension - [WSL Extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl) 
1. Python 3 - [Python Releases for Windows | Python.org](https://www.python.org/downloads/windows/)
1. Dapr CLI - [Install the Dapr CLI | Dapr Docs](https://docs.dapr.io/getting-started/install-dapr-cli/)
1. Install Dapr - [Initialize Dapr in your local environment | Dapr Docs](https://docs.dapr.io/getting-started/install-dapr-selfhost/)