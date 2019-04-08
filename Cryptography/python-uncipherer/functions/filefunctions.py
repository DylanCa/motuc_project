import codecs
import os
from pathlib import Path


class FileFunction():
    filepath = ''

    def __init__(self, filepath):
        self.filepath = filepath

    def openfile(self):
        f = codecs.open(Path("../../encrypted_files/", self.filepath),
                        "rb",
                        encoding="utf-8")
        fr = f.readlines()
        f.close()
        return fr

    def return6charwordsfromfile(self, f):
        return [
            word.strip('\n') for word in f if len(word.replace('\n', '')) == 6
        ]

    def writeinfile(self, text):
        f = codecs.open(Path("../../encrypted_files/", self.filepath),
                        "w",
                        encoding="utf-8")
        f.write(text)
