import re


def find_classes(module_source):
    """
    Maps class names to the class' source code.
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
            class_dict[class_name] = match.group(1).rstrip() if match else ''

    return class_dict


def find_class_names(module_source):
    """
    Finds the names of classes inside the module.

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
    Finds the class' documentation.

    Parameters
    ----------
    class_source: str
        The source code of the class.

    Returns
    -------
    str: The documentation of the class.
    """
    match = re.search('class [a-zA-z0-9_]*?\(.*?\):[^def]*?"""\n([^"]*)"""', class_source)
    return match.group(1).rstrip() if match else ''


def find_function_doc(function_source):
    """
    Finds the function's documentation.

    Parameters
    ----------
    function_source: str
        The source code of the function.

    Returns
    -------
    str: The documentation of the function.
    """
    match = re.search('def \w+?\(.*?\):\s+?"""((.|\s)*?)"""', function_source)
    return match.group(1).lstrip().rstrip() if match else ''


def find_functions(source_code):
    """
    Finds function blocks inside of the code.

    Parameters
    ----------
    source_code: str
        The source code.

    Returns
    -------
    tuple(str): The source code of each function found.
    """
    regex = 'def (.|\n)+?("""(.|\n)*?""")(.|\n)+?(?=^\s*?def |^\s*?class |^\s*?@\w+?\s+?|\Z)'
    return [m.group(0).lstrip().rstrip()
            for m in re.finditer(re.compile(regex, re.RegexFlag.MULTILINE), source_code)]


def find_function_name(function_source):
    """
    Finds the name of the function.

    Parameters
    ----------
    function_source: str
        The source code of the function.

    Returns
    -------
    str: The name of the function.

    """
    match = re.search('def (\w+?)\(.*?\):', function_source)
    return match.group(1).rstrip() if match else ''


def find_function_params(documentation):
    """
    Parses the documentation of the function to find the parameters, their return types, and descriptions.
    NOTE: This assumes the use of my documentation format.

    Parameters
    ----------
    documentation: str
        The function's documentation.

    Returns
    -------
    dict: The parameters of the function as `parameter[name: str] = tuple(type: str, description: str)`.
    """
    params = dict()
    match = re.search('(Parameters\s+?-+\s+)((.|\s)+?)(\Z|((Returns|Throws)\s+?(-+?)))', documentation)
    param_block = match.group(2).lstrip().rstrip() if match else None

    if param_block:
        for match in re.finditer('(\w+?):\s*(.+?)\n\s+?((.|\s)+?)(?=(\w+?):|\Z)', param_block):
            params[match.group(1)] = (match.group(2), match.group(3).lstrip().rstrip())
    return params
