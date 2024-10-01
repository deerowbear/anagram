from parsers import ArgumentParser
from file_utils import FileUtils
import logging

logging.basicConfig(filename='anagram.log',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)

logger = logging.getLogger(__name__) 


def main():
    filePath = ArgumentParser.parseArguments()
    if filePath == None:
        print("Error can't be none")
    dictionary: dict = FileUtils.fileToDictionary(filePath)
    while True:
        userInput = input("Enter a word (or '.quit' to exit): ").strip()
        if userInput == '.quit':
            break
        found: bool = False
        for key, value in dictionary.items():
            if userInput == key:
                found = True
                logger.info("Word found in the dictionary, but %s is not an anagram.", userInput)
                continue
            if sorted(userInput) == value:
                found = True
                logger.info("Anagram found for %s in dictionary with word %s", userInput, key)
        if found == False:
            logger.info("No anagram found for %s.", userInput)

if __name__ == "__main__":
    main()