from functions.decryptor import Decryptor
from functions.gui import GUI
import tkinter
from pick import pick

title = '''
\n------------------------------------------------------------------------------------------------------\n
|           Here, you will be able to Encrypt / Decrypt your files using the Vernam Cipher           |\n
| Please be sure that the files you want to decrypt are in the folder located at ../encrypted_files. |\n
|                                                                                                    |\n
| This ( little ) program has been made by https://github.com/DylanCa during his 4th IT Student year |\n
|                             Feel free to star the project on Github !                              |\n
------------------------------------------------------------------------------------------------------\n'''
options = ['Directly from the Console', 'Using the provided Python GUI']

option, index = pick(options, title)

if index == 0:
    Decryptor().decrypt()

elif index == 1:
    root = tkinter.Tk()
    my_gui = GUI(root)
    root.mainloop()
