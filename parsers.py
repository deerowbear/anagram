import json

class JsonParser: 

    def parseData(json_object: json, key: str) -> str:
        try:
            if isinstance(json_object, list):
                return json_object[0][key]
            else:
                return json_object[key]
        except:
            return None
        

import argparse
from file_utils import FileUtils

class ArgumentParser:

    def parseArguments() -> str:
        parser = argparse.ArgumentParser()
        parser.add_argument('--path', type=FileUtils.validateFile, 
                            help='Please define a path to a file.')
        argument = vars(parser.parse_args());
        filePath = JsonParser.parseData(argument, 'path')
        if filePath == None:
            raise Exception("Invalid argument. Please speicify a valid path to a file.")
        return filePath
    

