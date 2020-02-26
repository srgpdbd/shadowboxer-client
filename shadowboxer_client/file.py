import os
from datetime import datetime
from typing import Union, List


class File:

    def __init__(self, path: str):
        self.path: str = path
        self.modified_at: datetime = datetime.fromtimestamp(os.path.getmtime(self.path))
        self.last_sync_at: Union[int, None] = None


FilesList = List[File]


def get_files_list(folder_path) -> FilesList:
    return [File(f'{folder_path}/{file_name}') for file_name in os.listdir(folder_path)]
