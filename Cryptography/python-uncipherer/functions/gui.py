from pathlib import Path
from decryptor import Decryptor

import tkinter
import easygui
import codecs


class GUI(tkinter.Frame):
    def __init__(self, master):
        super(GUI, self).__init__(master)
        self.master = master
        master.title("Python Vernam Encrypter / Decrypter")

        self.bgcolor = 'lightblue'

        self.label = tkinter.Label(
            master, text="Python Vernam Encrypter / Decrypter")
        self.label.pack()

        self.load_button = tkinter.Button(
            master, text="Browse Files", command=self.openfile)
        self.load_button.pack()

        self.frame_width = 1000
        self.frame_height = 500

        # Set configuration our frame
        self.config(
            width=self.frame_width, height=self.frame_height, bg=self.bgcolor)
        self.pack()

        # Create textBox for input data
        self.encrypted_file = tkinter.Text()
        self.encrypted_file.configure(state="disabled")
        self.encrypted_file.place(x=30, y=170, height=300, width=400)

        # Create textBox for result
        self.textbox_two = tkinter.Text()
        self.textbox_two.place(x=570, y=170, height=300, width=400)

        label_input_text = tkinter.Label(
            text="Encrypted Text: ", bg=self.bgcolor)
        label_input_text.place(x=30, y=155, height=15, width=120)

        self.variable = tkinter.StringVar(master)
        self.variable.set("latin_1")  # default value

        self.w = tkinter.OptionMenu(master, self.variable, "latin_1", "UTF-8",
                                    "ISO8859_1")
        self.w.pack()

        self.filetext = ''

    def openfile(self):
        filepath = easygui.fileopenbox()

        try:
            f = codecs.open(
                Path(filepath), "r", encoding='latin_1', errors='ignore')
            self.filetext = f.read()

            self.encrypted_file.configure(state="normal")
            self.encrypted_file.insert(tkinter.INSERT, self.filetext)
            self.encrypted_file.configure(state="disabled")

            f.close()
        except:
            print("No file exists")

    def decrypt(self):
        Decryptor().decrypt()

root = tkinter.Tk()
my_gui = GUI(root)
root.mainloop()
