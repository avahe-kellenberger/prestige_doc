from prestige_doc import parser


class Class(object):

    """
    Represents a python class, which allows access to its documentation and functions.
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
        self.__doc = parser.find_class_doc(source_code)
        self.__source_code = source_code

    @property
    def name(self):
        """
        Returns
        -------
        str: The name of the class.
        """
        return self.__name

    @property
    def doc(self):
        """
        Returns
        -------
        str: The documentation of the class.
        """
        return self.__doc

    @property
    def source_code(self):
        """
        Returns
        -------
        str: The source code of the class.
        """
        return self.__source_code


class Module(object):

    """
    Represents a python module, which allows access to classes and methods as strings.
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
        tuple: The classes inside the module as `prestige_doc.module.Class` objects.
        """
        return self.__classes
