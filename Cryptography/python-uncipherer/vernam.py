from itertools import product
from string import ascii_lowercase

from filefunctions import FileFunction

EncryptedFileFunctions = FileFunction("../_MISC/encrypted_files/PK.txt")
WordlistFileFunctions = FileFunction(
    "../_MISC/encrypted_files/liste_francais.txt")

encrypted_file = EncryptedFileFunctions.openfile()
wordlist = WordlistFileFunctions.openfile(encoding='ISO-8859-15')

sixchar_wordlist = WordlistFileFunctions.return6charwordsfromfile(wordlist)

result = ""
ptr = 0

for key in (''.join(i) for i in product(ascii_lowercase, repeat=6)):
    for word in encrypted_file:
        for char in word:
            result = result + chr(ord(char) ^ ord(key[ptr]))
            ptr = ptr + 1
            if ptr == len(key):
                ptr = 0
                break
        break
    print("Key: {} - Result: {}".format(key, result))
    result = ""

    if result in sixchar_wordlist:
        print("MATCH")
        break
