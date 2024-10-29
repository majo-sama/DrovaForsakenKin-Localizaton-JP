def read_data_to_dict(data: str) -> dict:
    """
    Read data from a string format into a dictionary.

    Args:
        data (str): The input data in the specified format.

    Returns:
        dict: A dictionary representation of the input data.
    """
    result = {}
    lines = data.strip().splitlines()

    for line in lines:
        if line.strip():  # Check for non-empty lines
            key, value = line.split(" ", 1)  # Split into key and value
            key = key.strip()  # Clean up the key
            value = value.strip().strip("{} ")  # Clean up the value
            result[key] = value  # Add to dictionary

    return result


def write_dict_to_data(data_dict: dict) -> str:
    """
    Write a dictionary back to the specified string format.

    Args:
        data_dict (dict): The dictionary to write.

    Returns:
        str: A string representation of the dictionary in the specified format.
    """
    lines = []

    for key, value in data_dict.items():
        lines.append(f"{key} {{ {value} }}")  # Format each line

    return "\n\n".join(lines)  # Join all lines into a single string
