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

    def check_and_create_initial_data(self):
        cursor: Cursor = self._connection.cursor()
        new_table_query: str = (
            f'CREATE TABLE IF NOT EXISTS {self._files_table_name}'
            '(id INTEGER PRIMARY KEY, filename VARCHAR, changed_at DATETIME, synced_at DATATIME);'
        )
        cursor.execute(new_table_query)
        self._connection.commit()
