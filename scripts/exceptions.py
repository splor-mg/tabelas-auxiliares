class MissingPackageError(Exception):
    """
    Exception raised when one or more required packages from project dependencies are missing.
    """

class WrongVersionPackageError(Exception):
    """
    Exception raised when one or more versions of the required packages from project dependencies are wrong.
    """
