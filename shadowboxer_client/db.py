from __future__ import annotations
from sqlite3 import connect, Connection, Cursor
from typing import Optional

from .const import DB_NAME, DB_FILES_TABLE


class SingletonMeta(type):
    _instance: Optional[LocalDatabase] = None

    def __call__(self) -> LocalDatabase:
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance


class LocalDatabase(metaclass=SingletonMeta):
    
    def __init__(self):
        self._db_name: str = DB_NAME
        self._files_table_name: str = DB_FILES_TABLE
        self._connection: Connection = connect(self._db_name)

    def check_and_create_initial_data(self) -> None:
        cursor: Cursor = self._connection.cursor()
        new_table_query: str = (
            f'CREATE TABLE IF NOT EXISTS {self._files_table_name}'
            '(id INTEGER PRIMARY KEY, path VARCHAR UNIQUE, changed_at DATETIME, synced_at DATETIME);'
        )
        cursor.execute(new_table_query)
        self._connection.commit()

    def get_file_data(self, filepath) -> list:
        cursor: Cursor = self._connection.cursor()
        file_data_query: str = f'SELECT * FROM {self._files_table_name} WHERE path=?;'
        cursor.execute(file_data_query, (filepath, ))
        return cursor.fetchall()

    def create_file_data(self, filepath, changed_at) -> None:
        cursor: Cursor = self._connection.cursor()
        file_data_query: str = f'INSERT INTO {self._files_table_name}(path, changed_at) VALUES (?, ?);'
        cursor.execute(file_data_query, (filepath, changed_at))
        self._connection.commit()
