import codecs
import os
from pathlib import Path


class FileFunction():
    path = "../encrypted_files/"
    filepath = ''
    encoding = "latin_1"

    def __init__(self, filepath):
        self.filepath = self.path + filepath

    def openfile(self):
        f = codecs.open(
            Path(self.filepath), "r", encoding=self.encoding, errors='ignore')
        fr = f.read()
        f.close()
        return fr

    def return6charwordsfromfile(self, f):
        return [
            word.strip('\n') for word in f if len(word.replace('\n', '')) == 6
        ]

    def writeinfile(self, text):
        f = codecs.open(
            Path(self.filepath), "w", encoding=self.encoding, errors='ignore')
        f.write(text)
        f.close()
