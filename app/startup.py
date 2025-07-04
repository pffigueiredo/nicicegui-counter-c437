from app.database import create_tables
from app import counter


def startup() -> None:
    # this function is called before the first request
    create_tables()
    counter.create()