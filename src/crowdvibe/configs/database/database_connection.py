import logging
from abc import ABC, abstractmethod
from typing import Any, Tuple, Optional, List, Self

from tenacity import retry, stop_after_attempt, wait_fixed, retry_if_exception_type


class DatabaseConnection(ABC):
    """
    Abstract Base Class for Database Connections

    This abstract class defines the interface for managing database connections.
    Subclasses must implement the `connect`, `cursor`, and `execute_query` methods.

    Methods:
        connect(): Abstract method to establish a connection to the database.
        cursor(): Abstract method to get a cursor for executing queries.
        execute_query(query: str, params: Optional[Tuple] = None) -> List[Tuple]:
            Abstract method to execute a SQL query and return the results.
        __enter__(): Context management method for entering the context.
        __exit__(): Context management method for exiting the context.

    """

    def __init__(self, host: str, user: str, password: str, port: int, schema: str = ""):
        """
        Initialize a new DatabaseConnection instance.

        :param host: The hostname or IP address of the database server.
        :param user: The username used for authentication.
        :param password: The password used for authentication.
        :param port: The port number on which the database server is listening.
        :param schema: The default schema to use for database operations. (optional)

        """

        self.host: str = host
        self.user: str = user
        self.password: str = password
        self.port: int = port
        self.schema: str = schema
        self.connection: Optional[Any] = None

    @abstractmethod
    def connect(self) -> Self:
        """
        Establish a connection to the database.

        This method must be implemented by subclasses.

        """
        pass

    @abstractmethod
    def cursor(self) -> Any:
        """
        Get a cursor for executing queries.

        This method must be implemented by subclasses.

        """
        pass

    @abstractmethod
    def execute_query(self, query: str, params: Optional[Tuple] = None) -> List[Tuple]:
        """
        Execute a SQL query and return the results.

        This method must be implemented by subclasses.

        :param query: The SQL query to execute.
        :type query: str
        :param params: Optional parameters to pass to the query (default: None).
        :type params: Optional[Tuple]
        :return: A list of tuples representing the query results.
        :rtype: List[Tuple]

        """
        pass

    def execute_transactions(self, query: str, values: List[Tuple]):
        """
        Executes transactions on the database.

        This method must be implemented by subclasses.

        :param query: The SQL query to execute.
        :param values: A list of tuples containing the parameter values for the query.
        :return: None

        raises: db.Error: If an error occurs during the transaction execution.
        """
        pass

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2), retry=retry_if_exception_type(Exception))
    def __enter__(self) -> Any:
        """
        Context management method for entering the context.

        This method is called when entering a context defined by the `with` statement.

        """
        try:
            self.connection = self.connect()
            logging.info("Database connection was successful!")
            return self.cursor()
        except Exception as e:
            logging.error(f"Database connection error: {e}")
            raise

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        """
        Exits the context for database connection.

        Args:
            exc_type: Exception type (if any).
            exc_value: Exception value (if any).
            traceback: Traceback information (if any).
        """
        try:
            if self.connection is not None:
                self.connection.close()
        except Exception as e:
            logging.error(f"{e}")
