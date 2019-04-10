from functions.filefunctions import FileFunction
import re


class Collisions():

    frenchdict = "liste_francais.txt"

    def __init__(self, file):
        self.file = file

    def checkcolissions(self):

        counter = 0
        match = 0
        for word in self.file:
            counter += 1
            if re.sub(r'\W+', '', word) in self.frenchdict:
                match += 1

        return round(match / counter * 100)