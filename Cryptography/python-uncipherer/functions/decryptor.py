from filefunctions import FileFunction
from itertools import cycle


# f = input("Enter the name of the file: ")
# key = input("Enter the 6-char key, please: ")

f = 'PB0.txt'
key = "babltq"

EncryptedFileFunctions = FileFunction(f)
encrypted_file = EncryptedFileFunctions.openfile()
WriteInFileFunctions = FileFunction("crypted_" + f)

text = []
for char, keyletter in zip(encrypted_file, cycle(key)):
    text += chr( ord(char) ^ ord(keyletter))

decrypted_file = WriteInFileFunctions.writeinfile(''.join(text))