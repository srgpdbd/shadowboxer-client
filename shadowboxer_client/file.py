import os
from datetime import datetime
from typing import Union, List

from .db import LocalDatabase


class File:

    def __init__(self, path: str) -> None:
        self.__db_connection: LocalDatabase = LocalDatabase()
        self.path: str = path
        self.modified_at: datetime = datetime.fromtimestamp(os.path.getmtime(self.path))
        self.last_sync_at: Union[int, None] = None
        self._file_data: dict = self._get_or_create_local_file_data(self.path, self.modified_at)[0]
        self.synced_at: Union[str, list] = self._file_data[3]

    def _get_or_create_local_file_data(self, path, modified_at) -> dict:
        data: list = self.__db_connection.get_file_data(self.path)
        if not len(data):
            self.__db_connection.create_file_data(self.path, self.modified_at)
            data: list = self.__db_connection.get_file_data(self.path)
        return data

    def sync(self):
        pass


FilesList = List[File]


def get_file_path(file_path: str, current_dir: str) -> str:
    full_path: str = f'{current_dir}/{file_path}'
    print(file_path)
    if os.path.isdir(full_path):
        for name in os.listdir(full_path):
            return get_file_path(name, full_path)
    else:
        return full_path


def get_files_list(folder_path) -> FilesList:

    for name in os.listdir(folder_path):
        print('----')
        print("returned", get_file_path(name, folder_path))
        print('----')

    return [File(f'{folder_path}/{file_name}') for file_name in os.listdir(folder_path)]
