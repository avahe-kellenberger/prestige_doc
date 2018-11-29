import re


def map_class_functions(raw_source, class_name):
    """Maps the class name to its functions.

    Parameters
    ----------
    raw_source: str
        The raw text of a *.py file.
    class_name: str
        The name of the class to map.
    """
    # TODO:
    return ""


def map_class_docs(raw_source):
    """Reads the source file and maps the class names to their documentation.

    Parameters
    ----------
    raw_source: str
        The raw text of a *.py file.

    Returns
    -------
    dict: A dictionary of each class to a map of its functions' names to their documentation,
    """
    class_docs = dict()
    for class_name in find_class_names(raw_source):
        doc = find_class_doc(raw_source, class_name)
        class_docs[class_name] = doc if doc else ''
    return class_docs


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
    match = re.search(re.compile(f'class {class_name}\(.*?\):[^def]*?"""\n([^"]*)"""'), raw_source)
    if match:
        return match.group(1).rstrip()
    return None

