from sqlite3 import connect, Connection, Cursor

from .const import DB_NAME, DB_FILES_TABLE


# TODO: singletone
class LocalDatabase:
    
    def __init__(self):
        self.__db_name: str = DB_NAME
        self.__files_table_name: str = DB_FILES_TABLE
        self.__connection: Connection = connect(self.__db_name)

    @property
    def __has_initial_data(self):
        # TODO: use parametriesed queries https://www.btelligent.com/en/blog/best-practice-for-sql-statements-in-python/
        existing_table_query = f"SELECT COUNT(name) FROM sqlite_master WHERE type='table' AND name='{self.__files_table_name}';"
        cursor: Cursor = self.__connection.cursor()
        rows: Cursor = cursor.execute(existing_table_query)
        tables_count: int = rows.fetchall()[0][0]
        return tables_count > 0

    def check_and_create_initial_data(self):
        if not self.__has_initial_data:
            cursor: Cursor = self.__connection.cursor()
            cursor.execute(f'CREATE TABLE {self.__files_table_name} (id INTEGER PRIMARY KEY, filename VARCHAR)')
            self.__connection.commit()
