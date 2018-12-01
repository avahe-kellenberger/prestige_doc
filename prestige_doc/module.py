from prestige_doc import parser


class Function(object):

    """
    Represents a function.
    """

    def __init__(self, source_code):
        """
        Parses the source code of the function to find its components.

        Parameters
        ----------
        source_code: str
            The source code of the function.
        """
        self.__source_code = source_code
        # TODO: Maybe have this passed in, like the Class object.
        self.__name = parser.find_function_name(source_code)
        self.__doc = parser.find_function_doc(source_code)
        # self.__parameters = parser.find_function_params(self.__doc)

    @property
    def name(self):
        """
        Returns
        -------
        str: The name of the function.
        """
        return self.__name

    @property
    def source_code(self):
        """
        Returns
        -------
        str: The source code of the function.
        """
        return self.__source_code

    @property
    def doc(self):
        """
        Returns
        -------
        str: The documentation of the function.
        """
        return self.__doc

    @property
    def parameters(self):
        """
        Returns
        -------
        dict: The parameters of the function as `parameter[name] = type`.
        """
        return ""
        # return self.__parameters


class Class(object):

    """
    Represents a class, which allows access to its documentation and functions.
    """

    def __init__(self, name, source_code):
        """
        Parses the source code of the given class and breaks it down into documentation and functions.

        Parameters
        ----------
        source_code: str
            The raw text of the class.
        """
        self.__name = name
        self.__source_code = source_code
        self.__doc = parser.find_class_doc(source_code)
        self.__functions = tuple(Function(f) for f in parser.find_functions(source_code))

    @property
    def name(self):
        """
        Returns
        -------
        str: The name of the class.
        """
        return self.__name

    @property
    def source_code(self):
        """
        Returns
        -------
        str: The source code of the class.
        """
        return self.__source_code

    @property
    def doc(self):
        """
        Returns
        -------
        str: The documentation of the class.
        """
        return self.__doc

    @property
    def functions(self):
        """
        Returns
        -------
        tuple(Function): The functions in the class.
        """
        return self.__functions


class Module(object):

    """
    Represents a module, which allows access to classes and methods as strings.
    """

    def __init__(self, source_code):
        """
        Parses the source code of the given module and breaks it down into classes and global variables.

        Parameters
        ----------
        source_code: str
            The raw text of the module.
        """
        self.__source_code = source_code
        self.__classes = tuple(Class(i[0], i[1]) for i in parser.find_classes(source_code).items())

    @property
    def source_code(self):
        """
        Returns
        -------
        str: The source code of the module.
        """
        return self.__source_code

    @property
    def classes(self):
        """
        Returns
        -------
        tuple(Class): The classes inside the module as `prestige_doc.module.Class` objects.
        """
        return self.__classes
