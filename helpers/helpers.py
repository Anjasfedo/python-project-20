import json


def readJson(path, value):
    """
    Reads a JSON file and retrieves a specific value.

    Args:
    - path (str): The path to the JSON file.
    - value (str): The key to retrieve from the JSON file.

    Returns:
    - The value associated with the specified key in the JSON file.
    """
    with open(path, "r") as configs:
        # Load the JSON content from the file
        config = json.load(configs)

        # Return the value associated with the specified key
        return config[value]
