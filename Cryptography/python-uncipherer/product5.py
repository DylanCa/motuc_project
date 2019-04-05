from itertools import product
from string import ascii_lowercase

import re

from filefunctions import FileFunction

EncryptedFileFunctions = FileFunction("../_MISC/encrypted_files/PK.txt")
WordlistFileFunctions = FileFunction(
    "../_MISC/encrypted_files/liste_francais.txt")

encrypted_file = EncryptedFileFunctions.openfile()
wordlist = WordlistFileFunctions.openfile(encoding='ISO-8859-15')


def recursivewordcheck(word=""):
    for char in ascii_lowercase:
        newword = word + char
        print("Testing >>{}<<".format(newword))
        for num, line in enumerate(wordlist):
            if re.findall(newword, line.lower()):
                print('Found >>"{}"<< at line: {}'.format(newword, num + 1))
                if len(newword) < 6:
                    newword = recursivewordcheck(newword)
                    break
    return newword


print(recursivewordcheck())

# for x in (''.join(i) for i in product(ascii_lowercase, repeat=5)):
#     print(x)