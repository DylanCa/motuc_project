from functions.filefunctions import FileFunction
from functions.frequency_analysis import FrequencyAnalysis as FA

from itertools import cycle
from os import walk

import time


class Decryptor():
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    def decrypt(self):

        path = "../encrypted_files"

        textfiles = []
        for (dirpath, dirnames, filenames) in walk(path):
            textfiles.extend(filenames)
            break

        print("({}) Available files to decrypt: {}".format(path, 
            ' | '.join(sorted(textfiles))))

        f = input(
            "Enter the name of the file you want to decrypt (leave blank if you want to decrypt every file): "
        )
        key = input(
            "Enter the 6-char key, please (leave blank if you do not know the key): "
        )

        start = time.time()

        fa = FA()
        if not f:
            for file in textfiles:
                encrypted_file = fa.initfile(file)

                if not key:
                    key = fa.analysefrequencyandgetkey(encrypted_file)

                text = []
                for char, keyletter in zip(encrypted_file, cycle(key)):
                    text += chr(ord(char) ^ ord(keyletter))

                WriteInFileFunctions = FileFunction("DECRYPTED/decrypted_" +
                                                    file)
                decrypted_file = WriteInFileFunctions.writeinfile(
                    ''.join(text))

        else:
            encrypted_file = fa.initfile(f)

            if not key:
                key = fa.analysefrequencyandgetkey(encrypted_file)

            text = []
            for char, keyletter in zip(encrypted_file, cycle(key)):
                text += chr(ord(char) ^ ord(keyletter))

            WriteInFileFunctions = FileFunction("DECRYPTED/decrypted_" + f)
            decrypted_file = WriteInFileFunctions.writeinfile(''.join(text))

        end = time.time()
        print("All files decrypted in {} seconds ! The key was > {} <".format(
            round(end - start, 2), key))
