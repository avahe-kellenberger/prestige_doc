from prestige_doc import parser


class Module(object):

    """
    Represents a python module, which allows access to classes and methods as strings.
    """

    def __init__(self, source_code):
        """
        Parses the source code of the given module and breaks it down into classes, functions, and global variables.

        Parameters
        ----------
        source_code: str
            The raw text of the module.
        """
        self.__classes = parser.find_classes(source_code)

    @property
    def classes(self):
        """
        TODO:

        Returns
        -------
        tuple:
            TODO.
        """
        return self.__classes
