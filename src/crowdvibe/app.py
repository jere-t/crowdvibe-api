import importlib.metadata
import logging
import time

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from crowdvibe.configs.config import settings
from crowdvibe.configs.database.postgres_connection import PostgresConnection
from crowdvibe.routes.router import api_router

LOG_PATH = "./"
SERVICE_NAME = "crowdvibe"
LOG_LEVEL = "INFO"

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]


def config_log():
    logging.basicConfig(
        filename=f"{LOG_PATH}{SERVICE_NAME}.log",
        filemode="a",
        format='[%(asctime)s] %(levelname)s - %(message)s - File "%(pathname)s", line %(lineno)d, in %(funcName)s',
        level=LOG_LEVEL,
    )


def create_app() -> FastAPI:
    config_log()

    version = importlib.metadata.version("crowdvibe")

    app = FastAPI(
        title=SERVICE_NAME,
        version=version,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    print(settings.database_name)

    db_connection = PostgresConnection(
        host=settings.database_hostname,
        user=settings.database_username,
        password=settings.database_password,
        port=settings.database_port,
        schema=settings.database_name,
    )
    result = db_connection.execute_query("SELECT * FROM songs")

    """"# The API is useless until we are connected to the database
    while True:
        try:
            connection = db_connection.connect()
            cursor = connection.cursor()
            logging.info("Database connection was successful!")
            break
        except Exception as error:
            logging.error(f"Database connection failed. Error: {error}")
            time.sleep(2)
    """


    print(result)
    print(result[0]['artist'])

    app.include_router(api_router, prefix=settings.api_v1_str)

    return app
