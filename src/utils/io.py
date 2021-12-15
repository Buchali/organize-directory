import json


def read_json(file_path: str):
    """
    Load json files.
    Args:
        file_path: path to the file
    """
    with open(file_path) as f:
        return json.load(f)
