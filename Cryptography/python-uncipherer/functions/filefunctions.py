class FileFunction():
    filepath = ''

    def __init__(self, filepath):
        self.filepath = filepath

    def openfile(self, encoding="utf-8"):
        f = open(self.filepath, encoding=encoding)
        return f.readlines()

    def return6charwordsfromfile(self, f):
        return [
            word.strip('\n') for word in f if len(word.replace('\n', '')) == 6
        ]
