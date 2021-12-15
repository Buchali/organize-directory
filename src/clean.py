import shutil
import sys
from pathlib import Path
from typing import Union

from loguru import logger

from src.data import DATA_DIR
from src.utils.io import read_json


class OrganizeFiles():
    """
    This class is used to organize files in a directory by
    moving the files based on their extensions.
    """
    def __init__(self):
         # Load and prepare the extension file
        extension = {}
        ext = read_json(DATA_DIR / 'extensions.json')
        for file_type, file_extentions in ext.items():
            for file_ext in file_extentions:
                extension[file_ext] = file_type
        self.extension = extension

    def __call__(self, directory: Union[str, Path]):
        """
        Organize files by moving them from directory to sub-directories
        Args:
            directory: path to a directory
        """
        directory = Path(directory)
        if not directory.exists():
            raise FileExistsError(f'{directory} does not exist!')

        logger.info(f'Organizing files in {directory.name} ...')
        # Organizor
        for file_path in directory.iterdir():
            if file_path.is_dir():
                continue

            if file_path.name.startswith('.'):
                continue

            if file_path.suffix not in self.extension:
                DEST_DIR = directory / 'other'
            else:
                DEST_DIR = directory / self.extension[file_path.suffix]
            DEST_DIR.mkdir(exist_ok=True)

            shutil.move(str(file_path), str(DEST_DIR))


if __name__ == '__main__':
    org_files = OrganizeFiles()
    org_files(sys.argv[1])
    logger.info('Done!')
