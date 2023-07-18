"""All exceptions thrown by this library."""
import http
from typing import Optional


class LibraryException(Exception):
    """Subclassing the base exception so it's easy to catch exceptions thrown specifically by this library."""

    pass


class ConnectionException(LibraryException):
    """A ConnectionException indicates that a client failed to connect to the requested service. 
        It consumes an optional HTTP status code if available."""
    

    def __init__(self, message: str, client_name: Optional[str] = None, http_status_code: Optional[http.HTTPStatus] = None):
        """Constructor.

        Args:
            message (str): Error message, typically returned by the service
            client_name (Optional[str]): Name of the client that raised the exception if available. Defaults to None.
            http_status_code (Optional[http.HTTPStatus], optional): HTTP Status code if available. Defaults to None.
        """
        
        self.http_status_code = http_status_code
        self.client_name = client_name
        
        super().__init__(message)
