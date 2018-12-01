import re


def find_classes(module_source):
    """Maps class names to the class' source code.
    This function assumes trailing code isn't added after a class.

    Parameters
    ----------
    module_source: str
        The source code of a module.

    Returns
    -------
    dict: A dictionary mapping class names to the class' source code.

    """
    class_dict = dict()
    class_names = find_class_names(module_source)
    if class_names is not None:
        body_pattern = r'(class %s\((.*?\)):((.|\s)*?))((class [a-zA-Z_][a-zA-Z0-9_]*?\(.*?\):)|\Z)'
        for class_name in class_names:
            new_pattern = body_pattern % class_name
            match = re.search(new_pattern, module_source)
            class_dict[class_name] = match.group(1).rstrip() if match else None

    return class_dict


def find_class_names(module_source):
    """

    Parameters
    ----------
    module_source: str
        The raw text of a *.py file.

    Returns
    -------
    list: A list of class names in the source.
    """
    return re.findall('class ([a-zA-Z_][a-zA-Z0-9_]*?)\(.*?\):', module_source)


def find_class_doc(class_source):
    """

    Parameters
    ----------
    class_source: str
        The source code of the class.

    Returns
    -------
    str: The documentation of the class.
    """
    match = re.search(re.compile('class [a-zA-z0-9_]*?\(.*?\):[^def]*?"""\n([^"]*)"""'), class_source)
    return match.group(1).rstrip() if match else None

