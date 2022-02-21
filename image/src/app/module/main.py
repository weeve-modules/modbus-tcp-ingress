"""
All logic related to the module's main application
Mostly only this file requires changes
"""

from pyModbusTCP.client import ModbusClient
from app.config import APPLICATION
from app.weeve.egress import send_data

import time

def verifySettings():
    if APPLICATION['START_ADDRESS'] < 0 or 65535 < APPLICATION['START_ADDRESS']:
        return "Bit / Register Address must be 0 to 65535."
    if APPLICATION['FUNCTION'] == 'holding_registers' or APPLICATION['FUNCTION'] == 'input_registers':
        if APPLICATION['LENGTH'] < 1 or 125 < APPLICATION['LENGTH']:
            return "For holding_registers and input_registers number of registers to read must be 1 to 125."
    if APPLICATION['FUNCTION'] == 'coils' or APPLICATION['FUNCTION'] == 'discrete_inputs':
        if APPLICATION['LENGTH'] < 1 or 2000 < APPLICATION['LENGTH']:
            return "For coils and discrete_inputs number of registers to read must be 1 to 2000."
    return None


def module_main():
    """implement module logic here

    Args:
        parsed_data ([JSON Object]): [The output of data_validation function]

    Returns:
        [string, string]: [data, error]
    """
    try:
        # verify settings
        verification = verifySettings()
        if verification:
            return None, verification
        
        # connect to ModbusTCP server
        client = ModbusClient(host = APPLICATION['SERVER_HOST_ADDRESS'], port = APPLICATION['SERVER_HOST_PORT'])
        client.open()

        modbus_functions = {
            'coils': client.read_coils,
            'discrete_inputs': client.read_discrete_inputs,
            'holding_registers': client.read_holding_registers,
            'input_registers': client.read_input_registers
        }
        function = modbus_functions[APPLICATION['FUNCTION']]

        # convert interval unit to seconds (must do for threading Timer)
        convert_interval_unit = {
            'ms': APPLICATION['INTERVAL_PERIOD']/1000,
            's': APPLICATION['INTERVAL_PERIOD'],
            'm': APPLICATION['INTERVAL_PERIOD'] * 60,
            'h': APPLICATION['INTERVAL_PERIOD'] * 3600,
            'd': APPLICATION['INTERVAL_PERIOD'] * 3600 * 24,
        }
        interval = convert_interval_unit[APPLICATION['INTERVAL_UNIT']]

        while True:
            register_data = function(APPLICATION['START_ADDRESS'], APPLICATION['LENGTH'])

            if register_data:
                return_data = []
                for index, data in enumerate(register_data):
                    if APPLICATION['FUNCTION'] == 'coils' or APPLICATION['FUNCTION'] == 'discrete_inputs':
                        # index + APPLICATION['START_ADDRESS'] because of the shift in read values list in respect to registers
                        return_data.append({'bit_address': index + APPLICATION['START_ADDRESS'], 'data': data})
                    if APPLICATION['FUNCTION'] == 'holding_registers' or APPLICATION['FUNCTION'] == 'input_registers':
                        # index + APPLICATION['START_ADDRESS'] because of the shift in read values list in respect to registers
                        return_data.append({'register_address': index + APPLICATION['START_ADDRESS'], 'data': data})

                send_data(return_data)
                
            time.sleep(interval)
        
        return return_data, None
            
    except Exception:
        client.close()
        return None, "Unable to perform the module logic"
