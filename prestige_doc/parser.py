import re


def find_classes(source_code):
    """Maps class names to the class' source code.
    This function assumes trailing code isn't added after a class.

    Parameters
    ----------
    source_code: str
        The source code of a module.

    Returns
    -------
    dict: A dictionary mapping class names to the class' source code.

    """
    class_dict = dict()
    class_names = find_class_names(source_code)
    if class_names is not None:
        body_pattern = r'(class %s\((.*?\)):((.|\s)*?))((class [a-zA-Z_][a-zA-Z0-9_]*?\(.*?\):)|\Z)'
        for class_name in class_names:
            new_pattern = body_pattern % class_name
            match = re.search(new_pattern, source_code)
            class_dict[class_name] = match.group(1).rstrip() if match else None

    return class_dict


def map_class_functions(source_code, class_name):
    """Maps the class name to its functions.

    Parameters
    ----------
    source_code: str
        The raw text of a *.py file.
    class_name: str
        The name of the class to map.
    """
    # TODO:
    return ""


def map_class_docs(source_code):
    """Reads the source file and maps the class names to their documentation.

    Parameters
    ----------
    source_code: str
        The raw text of a *.py file.

    Returns
    -------
    dict: A dictionary of each class to a map of its functions' names to their documentation,
    """
    class_docs = dict()
    for class_name in find_class_names(source_code):
        doc = find_class_doc(source_code, class_name)
        class_docs[class_name] = doc if doc else ''
    return class_docs


def find_class_names(source_code):
    """

    Parameters
    ----------
    source_code: str
        The raw text of a *.py file.

    Returns
    -------
    list: A list of class names in the source.
    """
    return re.findall('class ([a-zA-Z_][a-zA-Z0-9_]*?)\(.*?\):', source_code)


def find_class_doc(source_code, class_name):
    """

    Parameters
    ----------
    source_code: str
        The raw text of a *.py file.
    class_name: str
        The name of the class.

    Returns
    -------
    str: The documentation associated with the class name.
    """
    match = re.search(re.compile(f'class {class_name}\(.*?\):[^def]*?"""\n([^"]*)"""'), source_code)
    return match.group(1).rstrip() if match else None

