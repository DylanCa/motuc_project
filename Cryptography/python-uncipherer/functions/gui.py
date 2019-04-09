from pathlib import Path
from functions.decryptor import Decryptor

import tkinter
import easygui
import codecs
import os


class GUI(tkinter.Frame):
    def __init__(self, master):
        super(GUI, self).__init__(master)
        self.master = master
        master.title(
            "Python Vernam Encrypter / Decrypter | https://github.com/DylanCa/motuc-project"
        )

        self.bgcolor = 'lightblue'

        self.frame_width = 1000
        self.frame_height = 400

        # Set configuration our frame
        self.config(width=self.frame_width,
                    height=self.frame_height,
                    bg=self.bgcolor)
        self.pack()

        # Create textBox for input data
        self.encrypted_file = tkinter.Text()
        self.encrypted_file.configure(state="disabled")
        self.encrypted_file.place(x=30, y=40, height=300, width=400)

        label_encrypted_file = tkinter.Label(text="Encrypted Text: ",
                                             bg=self.bgcolor)
        label_encrypted_file.place(x=30, y=20, height=15, width=120)

        self.encryptedtext = ''
        self.filename = ''
        self.filepath = ''

        self.load_button = tkinter.Button(master,
                                          text="Browse Files",
                                          command=self.openfile)
        self.load_button.place(x=170, y=350)

        # Create textBox for result
        self.decrypted_file = tkinter.Text()
        self.decrypted_file.configure(state="disabled")
        self.decrypted_file.place(x=570, y=40, height=300, width=400)

        label_decrypted_file = tkinter.Label(text="Decrypted Text: ",
                                             bg=self.bgcolor)
        label_decrypted_file.place(x=570, y=20, height=15, width=120)

        self.decrypt_button = tkinter.Button(master,
                                             text="Decrypt File",
                                             command=self.decrypt)
        self.decrypt_button.place(x=710, y=350)

        label_dropdown_menu = tkinter.Label(text="Select an encoding: ",
                                            bg=self.bgcolor)
        label_dropdown_menu.place(x=435, y=50, height=15, width=130)

        self.encoding = tkinter.StringVar(master)
        self.encoding.set("latin_1")  # default value
        self.dropdown = tkinter.OptionMenu(master, self.encoding, "latin_1",
                                           "utf-8", "iso8859_1")
        self.dropdown.place(x=455, y=70)

        label_key = tkinter.Label(text="Decrypt key: ", bg=self.bgcolor)
        label_key.place(x=435, y=170, height=15, width=130)

        self.key = tkinter.Entry(master)
        self.key.place(x=440, y=190, height=22, width=120)

        label_keysize = tkinter.Label(
            text=
            "If you do not know,\n leave the previous\n input empty and \nenter the keysize: ",
            bg=self.bgcolor)
        label_keysize.place(x=435, y=260, height=70, width=130)

        self.keysize = tkinter.Entry(master)
        self.keysize.place(x=480, y=330, height=22, width=40)

    def openfile(self):
        self.filepath = easygui.fileopenbox()
        self.filename = self.filepath.split(os.sep)[-1]

        try:
            f = codecs.open(Path(self.filepath),
                            "r",
                            encoding=self.encoding.get(),
                            errors='ignore')
            self.encryptedtext = f.read()

            self.encrypted_file.configure(state="normal")
            self.encrypted_file.delete('1.0', tkinter.END)
            self.encrypted_file.insert(tkinter.INSERT, self.encryptedtext)
            self.encrypted_file.configure(state="disabled")

            self.decrypted_file.configure(state="normal")
            self.decrypted_file.delete('1.0', tkinter.END)
            self.decrypted_file.configure(state="disabled")

            f.close()
        except:
            print("No file exists")

    def decrypt(self):
        decrypted_text = Decryptor().decryptgui(self.filename,
                                                self.encryptedtext,
                                                self.key.get(),
                                                self.keysize.get())

        self.decrypted_file.configure(state="normal")
        self.decrypted_file.delete('1.0', tkinter.END)
        self.decrypted_file.insert(tkinter.INSERT, decrypted_text[0])
        self.decrypted_file.configure(state="disabled")

        self.key.delete(0, tkinter.END)
        self.key.insert(0, decrypted_text[1])

        self.keysize.delete(0, tkinter.END)
        self.keysize.insert(0, decrypted_text[2])
