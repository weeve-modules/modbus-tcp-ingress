"""
This file implements module's main logic.
Data inputting should happen here.

Edit this file to implement your module.
"""

from logging import getLogger
from api.send_data import send_data
from .params import PARAMS
from pyModbusTCP.client import ModbusClient

import time

log = getLogger("module")

def verifySettings():
    if PARAMS['START_ADDRESS'] < 0 or 65535 < PARAMS['START_ADDRESS']:
        return "Bit / Register Address must be 0 to 65535."
    if PARAMS['FUNCTION'] == 'holding_registers' or PARAMS['FUNCTION'] == 'input_registers':
        if PARAMS['LENGTH'] < 1 or 125 < PARAMS['LENGTH']:
            return "For holding_registers and input_registers number of registers to read must be 1 to 125."
    if PARAMS['FUNCTION'] == 'coils' or PARAMS['FUNCTION'] == 'discrete_inputs':
        if PARAMS['LENGTH'] < 1 or 2000 < PARAMS['LENGTH']:
            return "For coils and discrete_inputs number of registers to read must be 1 to 2000."
    return None


def module_main():
    """
    Implements module's main logic for inputting data.
    Function description should not be modified.
    """

    log.debug("Inputting data...")

    try:
        # YOUR CODE HERE
        # ----------------------------------------------------------------

        # verify settings
        verification = verifySettings()
        if verification:
            log.error(f"Error occurred when verifying module settings: {verification}")

        else:
            # connect to ModbusTCP server
            client = ModbusClient(host = PARAMS['SERVER_HOST_ADDRESS'], port = PARAMS['SERVER_HOST_PORT'])
            client.open()

            modbus_functions = {
                'coils': client.read_coils,
                'discrete_inputs': client.read_discrete_inputs,
                'holding_registers': client.read_holding_registers,
                'input_registers': client.read_input_registers
            }
            function = modbus_functions[PARAMS['FUNCTION']]

            # convert interval unit to seconds (must do for threading Timer)
            convert_interval_unit = {
                'ms': PARAMS['INTERVAL_PERIOD']/1000,
                's': PARAMS['INTERVAL_PERIOD'],
                'm': PARAMS['INTERVAL_PERIOD'] * 60,
                'h': PARAMS['INTERVAL_PERIOD'] * 3600,
                'd': PARAMS['INTERVAL_PERIOD'] * 3600 * 24,
            }
            interval = convert_interval_unit[PARAMS['INTERVAL_UNIT']]

            while True:
                register_data = function(PARAMS['START_ADDRESS'], PARAMS['LENGTH'])

                log.debug(f'Register data: {register_data}')

                if register_data:
                    return_data = []
                    for index, data in enumerate(register_data):
                        if PARAMS['FUNCTION'] == 'coils' or PARAMS['FUNCTION'] == 'discrete_inputs':
                            # index + PARAMS['START_ADDRESS'] because of the shift in read values list in respect to registers
                            return_data.append({'bit_address': index + PARAMS['START_ADDRESS'], 'data': data})
                        if PARAMS['FUNCTION'] == 'holding_registers' or PARAMS['FUNCTION'] == 'input_registers':
                            # index + PARAMS['START_ADDRESS'] because of the shift in read values list in respect to registers
                            return_data.append({'register_address': index + PARAMS['START_ADDRESS'], 'data': data})

                    # send data to the next module
                    log.debug(f'Output data: {return_data}')
                    send_error = send_data(return_data)

                    if send_error:
                        log.error(send_error)
                    else:
                        log.debug("Data sent successfully.")

                time.sleep(interval)


        # ----------------------------------------------------------------

    except Exception as e:
        client.close()
        log.error(f"Exception in the module business logic: {e}")
