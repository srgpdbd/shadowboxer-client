import time
import sys
import os
from typing import Union

from shadowboxer_client.core import get_folder_path
from shadowboxer_client.file import get_files_list, FilesList
from shadowboxer_client.db import LocalDatabase


def work(folder_path: str) -> None:
    # for the sake of development it is looking like this
    # but should be in cron job instead of while
    while True:
        files_in_folder: FilesList = get_files_list(folder_path)
        print(files_in_folder[0].modified_at)
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

