import os

file_path = os.getenv("NETBOX_DNS_SD_FILE_DIR", "./output")

def export_to_json(content, filename=f"{file_path}/ds.json"):
    """
    Saves the given content to a file.

    :param content: The content to be written to the file.
    :type content: str
    :param filename: The name of the file to be written. Default is "index.html".
    :type filename: str, optional
    """
    with open(filename, "w") as file:
        file.write(content)
