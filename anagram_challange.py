from parsers import ArgumentParser
from file_utils import FileUtils

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
                continue
            if sorted(userInput) == value:
                found = True
                print(f"Anagram found for {userInput} with word in dictionary {key}")
        if found == False:
            print("No anagram found.")

if __name__ == "__main__":
    main()