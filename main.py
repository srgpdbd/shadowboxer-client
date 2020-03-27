import time
import sys
import os
from typing import Union

from shadowboxer_client.core import get_folder_path
from shadowboxer_client.file import get_files_list, FilesList, File
from shadowboxer_client.db import LocalDatabase


class App:

    def __init__(self, folder_path) -> None:
        self.folder_path = folder_path

    def sync_new_file(self, file: File):
        pass

    def work(self) -> None:
        files_in_folder: FilesList = get_files_list(self.folder_path)
        for file in files_in_folder:
            if not file.synced_at:
                self.sync_new_file(file)


def work(folder_path: str) -> None:
    # for the sake of development it is looking like this
    # but should be in cron job instead of while
    while True:
        app: App = App(folder_path)
        app.work()
        print("----")
        time.sleep(5)


def main() -> None:
    folder_path: Union[str, None] = get_folder_path()

    db: LocalDatabase = LocalDatabase()
    db.check_and_create_initial_data()

    if not folder_path:
        sys.exit()

    work(folder_path)
    

if __name__ == '__main__':
    main()
