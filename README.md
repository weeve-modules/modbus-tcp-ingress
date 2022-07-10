# ModbusTCP Ingress

|                |                                       |
| -------------- | ------------------------------------- |
| Name           | ModbusTCP Ingress                     |
| Version        | v1.0.0                                |
| Dockerhub Link | [weevenetwork/modbus-tcp-ingress](https://hub.docker.com/r/weevenetwork/modbus-tcp-ingress) |
| authors        | Jakub Grzelak                         |

- [ModbusTCP Ingress](#modbustcp-ingress)
  - [Description](#description)
  - [Supported TCP Functions](#supported-tcp-functions)
  - [Environment Variables](#environment-variables)
    - [Module Specific](#module-specific)
    - [Set by the weeve Agent on the edge-node](#set-by-the-weeve-agent-on-the-edge-node)
  - [Dependencies](#dependencies)
  - [Input](#input)
  - [Output](#output)

## Description

This ingress module provides readings from a selected Modbus TCP server.

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

### Set by the weeve Agent on the edge-node

Other features required for establishing the inter-container communication between modules in a data service are set by weeve agent.

| Environment Variables | type   | Description                                    |
| --------------------- | ------ | ---------------------------------------------- |
| MODULE_NAME           | string | Name of the module                             |
| MODULE_TYPE           | string | Type of the module (INGRESS, PROCESS, EGRESS)  |
| EGRESS_URLS            | string | HTTP ReST endpoint for the next module         |

## Dependencies

```txt
requests
pyModbusTCP
```

## Input

Input to this module are data read from registers of Modbus TCP server.

## Output

Output of this module is JSON body with selected registers values and following labels:

Output for Coils and Discrete Inputs:
```json
[
    {
        "bit_address": <index of register>,
        "data": <bool value read from register>
    },
]
```

Output for Holding Registers and Input Registers:
```json
[
    {
        "register_address": <index of register>,
        "data": <integer value read from register>
    }
]
```

Example for Coils and Discrete Inputs:
```json
[
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
]
```

Example for Holding Registers and Input Registers:
```json
[
    {
        "register_address": 0,
        "data": 12
    }
]
```
