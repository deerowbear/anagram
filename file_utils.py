import os
from pathlib import Path

class FileUtils:


    def fileToDictionary(file: str) -> dict:
        """Creates a dictionary from a file iterating over each line. The 
        key will be the orginal word and the value will be the sorted value of
        the word.

        Args:
            file: Path to the file

        Returns:
            A dictionary of words
        """
        dictionary = {}
        with open(file, "r") as file:
            for line in file:
                dictionary[line.strip()] = sorted(line.strip())
        return dictionary
        
    def validateFile(file: str) -> str:
        """Validates if a file exists.

        Args:
            file: Path to the file

        Returns:
            A path to the file

        Raises:
            An error if the file is not found.
        """
        if os.path.isfile(file):
            return file
        else:
            raise FileNotFoundError("File not found: " + file)
