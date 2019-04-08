import codecs

class FileFunction():
    filepath = ''

    def __init__(self, filepath):
        self.filepath = filepath

    def openfile(self, encoding="UTF-8"):
        f = codecs.open(self.filepath, "r", encoding)
        fr = f.read()
        f.close()
        return fr

    def return6charwordsfromfile(self, f):
        return [
            word.strip('\n') for word in f if len(word.replace('\n', '')) == 6
        ]
