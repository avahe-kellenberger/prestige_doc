import re


def map_documentation(raw_source):
    """Reads the source file and maps the class and function names to their documentation.

    Parameters
    ----------
    raw_source: str
        The raw text of a *.py file.

    Returns
    -------
    dict: A dictionary of the class and function names to their documentation.
    """
    class_names = find_class_names(raw_source)
    doc_matcher = 'class Connection\(.*?\):[^"]*?"""[^a-zA-Z]*([^"]*)"""'


def find_class_names(raw_source):
    """

    Parameters
    ----------
    raw_source: str
        The raw text of a *.py file.

    Returns
    -------
    list: A list of class names in the source.
    """
    return re.findall('class ([a-zA-Z_][a-zA-Z0-9_]*?)\(.*?\):', raw_source)


def find_class_doc(raw_source, class_name):
    """

    Parameters
    ----------
    raw_source: str
        The raw text of a *.py file.
    class_name: str
        The name of the class.

    Returns
    -------
    str: The documentation associated with the class name.
    """
    doc = re.search(re.compile(f'class {class_name}\(.*?\):[^"]*?"""\n([^"]*)"""'), raw_source).group(1)
    return doc.rstrip()

