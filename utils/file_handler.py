def export_to_html(content, filename="output/index.html"):
    """
    Saves the given content to a file.

    :param content: The content to be written to the file.
    :type content: str
    :param filename: The name of the file to be written. Default is "index.html".
    :type filename: str, optional
    """
    with open(filename, "w") as file:
        file.write(content)
