from sqlmodel import SQLModel, create_engine, Session, StaticPool
import os, logging

TO_FILE = True
SQLITE_FILE_NAME = "database.db"

# # Configure the logging module
# logging.basicConfig(level=logging.INFO)  # Set the logging level to INFO

# # Create a logger for your application
# logger = logging.getLogger(__name__)

# # Set up a handler for your application logger
# formatter = logging.Formatter('%(levelname)s [%(name)s]: %(message)s')
# handler = logging.StreamHandler()
# handler.setFormatter(formatter)
# logger.addHandler(handler)

# # Create a logger specifically for SQLModel's echoed SQL statements
# sql_logger = logging.getLogger("sqlalchemy.engine.base.Engine")
# # Set the logging level for SQLModel's logger to WARNING
# sql_logger.setLevel(logging.WARNING)
# # Set up a separate handler for SQLModel's logger
# sql_handler = logging.StreamHandler()
# sql_handler.setFormatter(formatter)
# sql_logger.addHandler(sql_handler)



if TO_FILE:
    sqlite_url = f"sqlite:///{SQLITE_FILE_NAME}"
    engine = create_engine(sqlite_url, echo=True)
else:
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
        echo=True,
    )

def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)

def write_to_db(val: list) -> None:
    with Session(engine) as session:
        session.add_all(val)
        session.commit()


def delete_db_file(file_path=SQLITE_FILE_NAME):
    try:
        os.remove(file_path)
        print(f"File '{file_path}' deleted successfully.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")