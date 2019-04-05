from itertools import product
from string import ascii_lowercase

import re

from filefunctions import FileFunction

EncryptedFileFunctions = FileFunction("../_MISC/encrypted_files/PK.txt")
WordlistFileFunctions = FileFunction(
    "../_MISC/encrypted_files/liste_francais.txt")

encrypted_file = EncryptedFileFunctions.openfile()
wordlist = WordlistFileFunctions.openfile(encoding='ISO-8859-15')

encrypted_6char_word = ''.join(list(encrypted_file[0][0:6]))

print([ord(x) for x in encrypted_6char_word])


def recursivewordcheck(password=""):

    for letter in ascii_lowercase:
        newpass = password + letter

        result = ""
        ptr = 0
        for char in encrypted_6char_word:
            result = result + chr(ord(char) ^ ord(newpass[ptr]))
            ptr = ptr + 1
            if ptr > len(newpass) - 1:
                ptr = 0
                break
        result = re.sub('[^a-zA-Z\'":;!?. ]+', 'XXX', result)
        for num, line in enumerate(wordlist):
            if re.findall(r'^{}'.format(result), line.lower()):
                if len(newpass) < 6:
                    newpass = recursivewordcheck(newpass)
                    break

                elif len(newpass) == 6:
                    print('(KEY: "{}") - Found >>"{}"<< at line: {}'.format(
                        newpass, result, num + 1))
                    break

    return newpass


recursivewordcheck()

# for x in (''.join(i) for i in product(ascii_lowercase, repeat=5)):
#     print(x)