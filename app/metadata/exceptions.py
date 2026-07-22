"""
Custom exceptions for the Metadata Platform.

"""


class MetadataException(Exception):
    """
    Base exception for all metadata-related errors.
    """
    pass


class MetadataNotFoundException(MetadataException):
    """
    Raised when metadata for a database cannot be found.
    """
    pass