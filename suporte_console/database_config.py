import sqlalchemy


def create_pool(
    database_user: str,
    database_pass: str,
    database_host: str,
    database_port: str,
    database_name: str,
    pool_size: int = 5,
    isolation_level=None
):
    database_conn_url = f'postgresql+pg8000://{database_user}:{database_pass}@{database_host}:{database_port}/{database_name}'

    # Creating database connection pool
    db_pool = sqlalchemy.create_engine(
        database_conn_url,
        pool_size=pool_size,
        max_overflow=2,
        pool_timeout=30,
        pool_recycle=1800,
        isolation_level=isolation_level
    )
    return db_pool
