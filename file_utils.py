import os
from pathlib import Path

class FileUtils:

    def fileToDictionary(file: str) -> dict:
        dictionary = {}
        with open(file, "r") as file:
            for line in file:
                dictionary[line.strip()] = sorted(line.strip())
        return dictionary
        
    def validateFile(file: str) -> str:
        if os.path.isfile(file):
            return file
        else:
            raise FileNotFoundError("File not found: " + file)
