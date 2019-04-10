from functions.filefunctions import FileFunction as FA
import re


class Collisions():

    frenchdict = FA("liste_francais.txt").openfile()

    def checkcollisions(self, file):

        counter = 0
        match = 0
        for word in file:
            counter += 1
            if self.frenchdict.find(word) is not -1:
                match += 1

        return round(match / counter * 100)
