# Python Input Module Boilerplate

|              |                                                                  |
| ------------ | ---------------------------------------------------------------- |
| name         | Python Input Module Boilerplate                             |
| version      | v1.0.0                                                           |
| GitHub       | [python-input-module-boilerplate](https://github.com/weeve-modules/python-ingress-module-boilerplate) |
| authors      | Jakub Grzelak, Nithin Saai                                       |

***
## Table of Content

- [Python Input Module Boilerplate](#python-input-module-boilerplate)
  - [Table of Content](#table-of-content)
  - [Description](#description)
  - [Directory Structure](#directory-structure)
    - [File Tree](#file-tree)
  - [Module Variables](#module-variables)
  - [As a module developer](#as-a-module-developer)
  - [Dependencies](#dependencies)
***

## Description 

This is a Python Input Boilerplate module and it serves as a starting point for developers to build input modules for weeve platform and data services.
Navigate to [As a module developer](#as-a-module-developer) to learn how to use this module. You can also explore our weeve documentation on [weeve Modules](https://docs.weeve.engineering/concepts/edge-applications/weeve-modules) and [module tutorials](https://docs.weeve.engineering/guides/how-to-create-a-weeve-module) to learn more details. 

## Directory Structure

Most important resources:

| name              | description                                                                                            |
| ----------------- | ------------------------------------------------------------------------------------------------------ |
| src               | All source code related to the module (API and module code).                                           |
| src/main.py       | Entry-point for the module.                                                                            |
| src/api           | Code responsible for setting module's API and communication with weeve ecosystem.                      |
| src/module        | Code related to the module's business logic. This is working directory for module developers.          |
| docker            | All resources related to Docker (Dockerfile, docker-entrypoint.sh, docker-compose.yml).                |
| example.env       | Holds examples of environment variables for running the module.                                        |
| requirements.txt  | A list of module dependencies.                                                                         |
| Module.yaml       | Module's YAML file that is later used by weeve platform Data Service Designer                          |

### File Tree

```bash
├── src
│   ├── api
│   │   ├── __init__.py
│   │   ├── log.py # log configurations
│   │   └── send_data.py # sends data to the next module
│   ├── module
│   │   └── main.py # [*] main logic for the module
│   └── main.py # module entrypoint
├── docker
│   ├── .dockerignore
│   ├── docker-compose.yml
│   ├── docker-entrypoint.sh
│   └── Dockerfile
├── example.env # sample environment variables for the module
├── Module.yaml # used by weeve platform to generate resource in Data Service Designer section
├── makefile
├── README.md
├── example.README.md # README template for writing module documentation
└── requirements.txt # module dependencies, used for building Docker image
```

## Module Variables

There are 4 module variables that are required by each module to correctly function within weeve ecosystem. In development, these variables can overridden for testing purposes. In production, these variables are set by weeve Agent.

| Environment Variables | type   | Description                                       |
| --------------------- | ------ | ------------------------------------------------- |
| MODULE_NAME           | string | Name of the module                                |
| MODULE_TYPE           | string | Type of the module (Input, Processing, Output)    |
| LOG_LEVEL             | string | Allowed log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL. Refer to `logging` package documentation. |
| EGRESS_URLS           | string | HTTP ReST endpoint for the next module            |

## As a module developer

RECOMMENDED:
Make sure you have [virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)

A module developer needs to add all the configuration and business logic.

All the module logic can be written in the module package in `src/module` directory.

   * The files can me modified for the module
      2. `module/module.py`
         * The function `module_main` should input/read data for this module.
         * All the business logic about modules are written here.

## Dependencies

The following are module dependencies:

* requests
