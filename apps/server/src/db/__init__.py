import os
from mysql.connector import pooling

db_config = {
    "host": os.getenv("DATABASE_HOST", "localhost"),
    "port": int(os.getenv("DATABASE_PORT", "3306")),
    "user": os.getenv("DATABASE_USER", "root"),
    "password": os.getenv("DATABASE_PASSWORD", "password"),
    "database": os.getenv("DATABASE_NAME", "tda_app"),
}

connection_pool = pooling.MySQLConnectionPool(
    pool_name="tda_pool", pool_size=10, **db_config
)


def get_connection():
    return connection_pool.get_connection()
