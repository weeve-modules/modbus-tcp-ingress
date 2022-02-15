"""
All logic related to the module's main application
Mostly only this file requires changes
"""


def module_main():
    """implement module logic here

    Args:
        parsed_data ([JSON Object]): [The output of data_validation function]

    Returns:
        [string, string]: [data, error]
    """
    try:
        return "parsed_data", None
    except Exception:
        return None, "Unable to perform the module logic"
