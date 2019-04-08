from filefunctions import FileFunction
from itertools import cycle

# f = input("Enter the name of the file: ")
# key = input("Enter the 6-char key, please: ")

f = '1.txt'
key = "fabqtl"

EncryptedFileFunctions = FileFunction("./../encrypted_files/" + f)
encrypted_file = EncryptedFileFunctions.openfile()

# text = []
# for char, keyletter in zip(encrypted_file, cycle(key)):
#     text += chr(ord(char) ^ ord(keyletter))


def vernam(message, key):
    return "".join([
        chr(ord(char) ^ ord(keyletter))
        for (char, keyletter) in zip(message, cycle(key))
    ])


print(vernam("".join(encrypted_file), key))
