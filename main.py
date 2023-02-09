import re

def countLetters(word:str, counter: dict[str,int]):
    for letter in word:
        if not letter.isalpha():
            continue
        if letter not in counter.keys():
            counter[letter] = 1
        else:
            counter[letter] = counter[letter] + 1

def printLetters(letters:dict[str,int]):
    for key in letters.keys():
        print("The '{}' character occurs {} times".format(key,letters[key]))

file = input("Give the directory of text that will be analyzed: ")

#read the file to a string
try:
    with open(file) as f:
        file_contents = f.read()
#in case of supplied file directory is not valid
except(FileNotFoundError):
    print("You must supply file directory that exists and valid!")
    exit()

#split the string to words
words = re.split(r" |\n",file_contents)
letters = {}

#count letters total in text
for word in words:
    countLetters(word.lower(),letters)

print("\n--- Begin report of " + file + " ---")
print(str(len(words)) + " words found in the document\n")
printLetters(letters)
print("\n--- End report ---")