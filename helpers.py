from pathlib import Path


def list_entries_recusive(path: Path):
    entries = []
    for entry in path.iterdir():
        entries.append(entry)
        if entry.is_dir():
            entries.extend(list_entries_recusive(entry))
    return entries


def read_data_to_dict(data: str) -> dict:
    """
    Parses the input data into a dictionary, handling multi-line values within braces,
    and ignoring markdown headers.

    Args:
        data (str): The input data as a string.

    Returns:
        dict: A dictionary mapping keys to their corresponding values.
    """
    result = {}
    lines = data.strip().replace("```", "").splitlines()

    key = None
    value_lines = []
    inside_braces = False

    for line in lines:
        line = line.strip()

        # Ignore empty lines and markdown headers
        if not line or line.startswith("###"):
            continue

        if not inside_braces:
            # Check if line contains a key and starts a value
            if "{" in line:
                parts = line.split("{", 1)
                key = parts[0].strip()
                value_part = parts[1].strip()
                if value_part.endswith("}"):
                    # Single-line value
                    value = value_part[:-1].strip()
                    result[key] = value
                    key = None
                else:
                    # Multi-line value starts
                    value_lines = [value_part]
                    inside_braces = True
            else:
                # Line does not contain a key, skip
                continue
        else:
            # Inside braces, collect value lines
            if "}" in line:
                # End of multi-line value
                value_part = line.split("}", 1)[0].strip()
                value_lines.append(value_part)
                value = "\n".join(value_lines).strip()
                result[key] = value
                key = None
                value_lines = []
                inside_braces = False
            else:
                # Continue collecting value lines
                value_lines.append(line)

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
