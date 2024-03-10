from typing import Self, Optional, Tuple, List

import psycopg2
from psycopg2.extras import RealDictCursor

from crowdvibe.configs.database.database_connection import DatabaseConnection


class PostgresConnection(DatabaseConnection):

    def connect(self) -> Self:
        """
        Establish a connection to the SQL Server database.

        :return: A connection object representing the database connection.

        """
        return psycopg2.connect(
            host=self.host,
            database=self.schema,
            user=self.user,
            password=self.password,
            port=self.port,
            cursor_factory=RealDictCursor,
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
