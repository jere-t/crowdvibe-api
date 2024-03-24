import logging
from typing import Self, Optional, Tuple, List

import pyodbc

from crowdvibe.configs.database.database_connection import DatabaseConnection


class MssqlConnection(DatabaseConnection):

    def connect(self) -> Self:
        """
        Establish a connection to the SQL Server database.

        :return: A connection object representing the database connection.

        """
        return pyodbc.connect(
            host=self.host,
            database=self.schema,
            user=self.user,
            password=self.password,
            port=self.port,
        )

    def cursor(self):
        """
        Get a cursor for executing queries.

        :return: A cursor object for executing queries.

        """
        return self.connection.cursor()

    def execute_query(self, query: str, params: Optional[Tuple] = None) -> List[Tuple]:
        """
        Execute a SQL query and return the results.

        This method must be implemented by subclasses.

        :param query: The SQL query to execute.
        :param params: Optional parameters to pass to the query (default: None).
        :return: A list of tuples representing the query results.

        """
        with self as cursor:
            cursor.execute(query, params)
            results = cursor.fetchall()

        return results

    def execute_transactions(self, query: str, values: List[Tuple]):
        """
        Executes transactions on the database.

        :param query: The SQL query to execute.
        :param values: A list of tuples containing the parameter values for the query.
        :return: None

        :raises pyodbc.Error: If an error occurs during the transaction execution.
        """
        try:
            with self as cursor:
                cursor.executemany(query, values)
                self.connection.commit()
                logging.info("Transaction executed successfully.")
        except pyodbc.Error as e:
            logging.error(f"Error executing transaction: {e}")
