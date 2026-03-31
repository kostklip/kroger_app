import os
import pymssql
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    return pymssql.connect(
        server=os.getenv("DB_SERVER"),
        port=os.getenv("DB_PORT", "1435"),
        user=os.getenv("DB_USERNAME"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
    )