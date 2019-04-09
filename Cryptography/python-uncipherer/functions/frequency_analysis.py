from functions.filefunctions import FileFunction
from string import ascii_lowercase

import json


class FrequencyAnalysis():
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    def initfile(self, filename):
        EncryptedFileFunctions = FileFunction(filename)
        return EncryptedFileFunctions.openfile()

    def analysefrequencyandgetkey(self, encrypted_file):
        blocks = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
        frequencytab = {0: {}, 1: {}, 2: {}, 3: {}, 4: {}, 5: {}}
        keylength = int(input("Enter the size of the key to find ( MANDATORY !!! ): "))
        while not isinstance(keylength, int):
            keylength = input("Please enter a number only. Key size: ")

        i = 0

        for char in ''.join(encrypted_file):
            blocks[i].append(char)
            i = i + 1 if i < keylength - 1 else 0

        highestEfreq = 0
        key = ""
        _tempkey = ""

        for i, block in enumerate(blocks):
            for l in ascii_lowercase:
                frequencytab[i][l] = {}
                for char in blocks[i]:
                    val = chr(ord(char) ^ ord(l))
                    frequencytab[i][l][val] = frequencytab[i][l].get(val,
                                                                     0) + 1

                for index in frequencytab[i][l]:
                    frequencytab[i][l][index] = {
                        'count': frequencytab[i][l][index],
                        'freq':
                        frequencytab[i][l][index] / len(blocks[i]) * 100
                    }
                try:
                    if frequencytab[i][l]['e']['freq'] > highestEfreq:
                        highestEfreq = frequencytab[i][l]['e']['freq']
                        _tempkey = l
                except Exception:
                    pass

            key += _tempkey
            highestEfreq = 0

        frequencytab['finalkey'] = key

        return frequencytab['finalkey']
