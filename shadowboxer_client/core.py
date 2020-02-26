from typing import Union

from configparser import ConfigParser, NoOptionError

from .messages import NO_FOLDER
from .const import CONFIG_FILES_DIR, CONFIG_MAIN_SECTION, CONFIG_FILE_NAME


def get_folder_path() -> Union[str, None]:
    config: ConfigParser = ConfigParser()
    config.readfp(open(CONFIG_FILE_NAME))
    files_dir = None
    try:
        files_dir: str = config.get(CONFIG_MAIN_SECTION, CONFIG_FILES_DIR)
    except NoOptionError:
        print(NO_FOLDER)
    return files_dir
