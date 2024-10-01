import json

class JsonParser: 

    def parseData(json_object: json, key: str) -> str:
        """Tries to pull a value out of a json object. If the object
        is of type list it will take the first object in the json and try 
        and return the value of the key being passed in.

        Args:
            json_object: A json object that needs a value parsed.
            key: the key that we expect a value from.
            
        Returns:
            key: a key that will return a value. If no key is found
            returns None.
        """
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
        """Parses the path argument. If it doesn't exists it will raise an exception.
        Validation is done on the argument type property.

        Args:
            None

        Returns:
            A path to the file

        Raises:
            An error if no argument is passed in.
        """
        parser = argparse.ArgumentParser()
        parser.add_argument('--path', type=FileUtils.validateFile, 
                            help='Please define a path to a file.')
        argument = vars(parser.parse_args())
        filePath = JsonParser.parseData(argument, 'path')
        if filePath == None:
            raise Exception("Invalid argument. Please speicify a valid path to a file.")
        return filePath
    

