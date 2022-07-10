# ModbusTCP Ingress


|              |                                                                                             |
| ------------ | ------------------------------------------------------------------------------------------- |
| name         | ModbusTCP Ingress                                                                           |
| version      | v0.0.1                                                                                      |
| docker image | [weevenetwork/modbus-tcp-ingress](https://hub.docker.com/r/weevenetwork/modbus-tcp-ingress) |
| tags         | Python, Flask, Docker, Weeve, ModbusTCP, Ingress                                            |
| authors      | Jakub Grzelak                                                                               |

***
## Table of Content
- [ModbusTCP Ingress](#modbustcp-ingress)
  - [Table of Content](#table-of-content)
  - [Description](#description)
    - [Features](#features)
  - [Supported TCP Functions](#supported-tcp-functions)
  - [Environment Variables](#environment-variables)
    - [Module Specific](#module-specific)
    - [Set by the weeve Agent on the edge-node](#set-by-the-weeve-agent-on-the-edge-node)
  - [Dependencies](#dependencies)
  - [Examples](#examples)
    - [Input](#input)
    - [Output](#output)
  - [docker-compose example](#docker-compose-example)

## Description 

This ingress module provides readings from a selected Modbus TCP server.

### Features
1. Connects with Modbus TCP server
2. Reads data from registers assigned to the server

## Supported TCP Functions
The following TCP functions are supported by this module

| Modbus Function        | Variable Name       | Permitted Values                                   |
| ---------------------- | ------------------- | -------------------------------------------------- |
| Read Coils             | coils               | Number of registers to read from must be 1 to 2000 |
| Read Discrete Inputs   | discrete_inputs     | Number of registers to read from must be 1 to 2000 |
| Read Holding Registers | holding_registers   | Number of registers to read from must be 1 to 250  |
| Read Input Registers   | input_registers     | Number of registers to read from must be 1 to 250  |

## Environment Variables

### Module Specific
The following module configurations can be provided in a data service designer section on weeve platform:

| Name                | Environment Variables | type    | Description                                                                                                      |
| ------------------- | --------------------- | ------- | ---------------------------------------------------------------------------------------------------------------- |
| Server Host Address | SERVER_HOST_ADDRESS   | string  | Host address of Modbus TCP Server                                                                                |
| Server Host Port    | SERVER_HOST_PORT      | integer | Port on which the Modbus TCP Server runs                                                                         |
| Function            | FUNCTION              | enum    | [Modbus Function](#supported-tcp-functions) to apply: coils, discrete_inputs, holding_registers, input_registers |
| Start Address       | START_ADDRESS         | integer | Index of the first register to read data from                                                                    |
| Length              | LENGTH                | integer | Number of consecutive registers to read data from (starting from index of above Start Address)                   |
| Interval Period     | INTERVAL_PERIOD       | integer | Data from registers is read every interval period                                                                |
| Interval Unit       | INTERVAL_UNIT         | emum    | Unit for the time interval: ms (miliseconds), s (seconds), m (minute), h (hour), d (day)                         |
| Output Label        | OUTPUT_LABEL          | string  | The output label at which read data is dispatched                                                                |

***

Other features required for establishing the inter-container communication between modules in a data service are set by weeve agent.

### Set by the weeve Agent on the edge-node

| Environment Variables | type   | Description                                       |
| --------------------- | ------ | ------------------------------------------------- |
| MODULE_NAME           | string | Name of the module                                |
| MODULE_TYPE           | string | Type of the module (ingress, processing, egress)  |
| EGRESS_SCHEME         | string | URL Scheme                                        |
| EGRESS_HOST           | string | URL target host                                   |
| EGRESS_PORT           | string | URL target port                                   |
| EGRESS_PATH           | string | URL target path                                   |
| EGRESS_URL            | string | HTTP ReST endpoint for the next module            |


## Dependencies

```txt
requests
python-dotenv
pyModbusTCP
```

## Examples

### Input
Input to this module are data read from registers of Modbus TCP server.
### Output
Output of this module is JSON body with selected registers values and timestamp.

Output for Coils and Discrete Inputs:
```node
{
    "<OUTPUT_LABEL>": [
        {
            "bit_address": <index of register>,
            "data": <bool value read from register>
        }
    ],
    "<MODULE_NAME>Time": timestamp
}
```

Output for Holding Registers and Input Registers:
```node
{
    "<OUTPUT_LABEL>": [
        {
            "register_address": <index of register>,
            "data": <integer value read from register>
        }
    ],
    "<MODULE_NAME>Time": timestamp
}
```

* Here `OUTPUT_LABEL` is specified at the module creation and `Processed data` is a list of data from registers processed by Module Main function.

Example for Coils and Discrete Inputs:
```node
{
    "registers": [
        {
            "bit_address": 3,
            "data": true
        },
        {
            "bit_address": 4,
            "data": true
        },
        {
            "bit_address": 5,
            "data": false
        },
    ],
    "modbus-tcp-ingressTime": timestamp
}
```

Example for Holding Registers and Input Registers:
```node
{
    "registers": [
        {
            "register_address": 0,
            "data": 12
        }
    ],
    "modbus-tcp-ingressTime": timestamp
}
```

Modules return a 200 response for success, and 500 for error. No other return message is supported.

## docker-compose example

```yml
version: "3"
services:
  boilerplate:
    image: weevenetwork/modbus-tcp-ingress
    environment:
      MODULE_NAME: modbus-tcp-ingress
      MODULE_TYPE: INGRESS
      SERVER_HOST_ADDRESS: server
      SERVER_HOST_PORT: 12345
      FUNCTION: holding_registers
      START_ADDRESS: 1
      LENGTH: 3
      INTERVAL_PERIOD: 5
      INTERVAL_UNIT: s
      OUTPUT_LABEL: registers
      EGRESS_URL: localhost
```
