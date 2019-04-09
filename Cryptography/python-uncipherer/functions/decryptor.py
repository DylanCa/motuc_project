from functions.filefunctions import FileFunction
from functions.frequency_analysis import FrequencyAnalysis as FA
from functions.collisions import Collisions

from itertools import cycle
from os import walk

import time


class Decryptor():
    textfile = ''
    key = ''
    keysize = ''
    filename = ''

    def decryptfile(self):

        path = "../encrypted_files"

        textfiles = []
        for (dirpath, dirnames, filenames) in walk(path):
            textfiles.extend(filenames)
            break

        print("({}) Available files to decrypt: {}".format(
            path, ' | '.join(sorted(textfiles))))

        f = input(
            "Enter the name of the file you want to decrypt (leave blank if you want to decrypt every file): "
        )
        key = input(
            "Enter the key, please (leave blank if you do not know the key): ")

        start = time.time()

        fa = FA()
        keysize = None

        if not f:
            for file in textfiles:
                encrypted_file = fa.initfile(file)

                if not key:
                    if not keysize:
                        keysize = int(
                            input(
                                "Enter the size of the key to find ( MANDATORY !!! ): "
                            ))

                        while not isinstance(keysize, int):
                            keysize = input(
                                "Please enter a number only. Key size: ")

                    key = fa.analysefrequencyandgetkey(encrypted_file, keysize)

                text = []
                for char, keyletter in zip(encrypted_file, cycle(key)):
                    text += chr(ord(char) ^ ord(keyletter))

                WriteInFileFunctions = FileFunction("DECRYPTED/decrypted_" +
                                                    file)
                decrypted_file = WriteInFileFunctions.writeinfile(
                    ''.join(text))

                print(
                    "There's a {}% match for the file {} with the key > {} <!".
                    format(Collisions(text).checkcolissions(), file, key))
                key = ''

        else:
            encrypted_file = fa.initfile(f)

            if not key:
                if not keysize:
                    keysize = int(
                        input(
                            "Enter the size of the key to find ( MANDATORY !!! ): "
                        ))

                    while not isinstance(keysize, int):
                        keysize = input(
                            "Please enter a number only. Key size: ")

                key = fa.analysefrequencyandgetkey(encrypted_file, keysize)

            text = []
            for char, keyletter in zip(encrypted_file, cycle(key)):
                text += chr(ord(char) ^ ord(keyletter))

            WriteInFileFunctions = FileFunction("DECRYPTED/decrypted_" + f)
            decrypted_file = WriteInFileFunctions.writeinfile(''.join(text))

            print("There's a {}% match for the file {} with the key > {} <!".
                  format(Collisions(text).checkcolissions(), f, key))

        end = time.time()
        print("All files decrypted in {} seconds !".format(
            round(end - start, 2)))

    def decryptmultiplefiles(self, files=[""]):
        pass

    def decrypttext(self, filename, textfile, key='', keysize=''):
        if key is not '':
            self.keysize = len(key)
            self.key = key

        else:
            fa = FA()
            self.keysize = keysize
            self.key = fa.analysefrequencyandgetkey(textfile, int(self.keysize))

        self.filename = filename
        self.textfile = textfile

        text = []
        for char, keyletter in zip(self.textfile, cycle(self.key)):
            text += chr(ord(char) ^ ord(keyletter))

        WriteInFileFunctions = FileFunction("DECRYPTED/decrypted_" +
                                            self.filename)
        WriteInFileFunctions.writeinfile(''.join(text))

        return [''.join(text), self.key, self.keysize]