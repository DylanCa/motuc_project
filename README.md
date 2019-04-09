# MOTUC Project 
## Description of the Program

This program is a "Vernam Uncipherer" developped with Python 3. It encrypts and decrypts files encoded in UTF-8, Latin_1 or ISO8859_1.

You will need to either provide the Encryption Key, or to enter the size of the Key to find, and the program will automatically find it via a Frequency Analysis.

Feel free to `pull request` if you find anything !
## Description of the Project

In order to validate a 4th year IT Engineering school project, we had to help a company whihc had its files encrypted by a hacker. The only hint we had was a riddle (un rébus), which you can find in the `Documents\A4 - Projet Management des risques 2019.pdf` file.

After decoding it, we found the following sentence:

>Je viens d'appliquer un algorithme de cryptage XOR sur tous vos fichiers. Je vous laisse une semaine pour trouver la clé de 6 caractères alpha minuscule maxi. Le texte est codé lettre par lettre avec la clé caractère par caractère.

This text is stating that the encryption key is 6-char long, lowercase letters, and the files have been encrypted using a XOR Cipher, most certainly Vernam Cipher.

Starting from that, we decided to implement the Vernam Cipher using Python 3, and we are going to explain you how to use this project to encrypt / decrypt your own files, and even find the encryption key starting from scratch.

## Requirements

> This program has been tested with Ubuntu 18.04 and Windows 10 64-bits.

You will need `Python 3` on your computer, as well as `pip`.


## Installation

- `git clone https://github.com/DylanCa/motuc_project.git`
- `cd motuc_project/Cryptography/python-uncipherer`
- `python3 -m pip install requirements.txt` - This will install 3 dependancies: `easygui`, `pick` and `windows-curses` (feel free to remove this line from the `requirements.txt` file if you are not on Windows).

- Right after, from the same folder (**this is important, always launch the script from the `python-uncipherer` folder**), do a `python3 script.py` and voilà.


(Last point: to guess the key, the program does a frequency analysis. Since I'm French, the analysis is based on the French language and the French Dictionnary, which means the top letter of the french alphabet is `e`, which should be the same for many languages. But feel free to change the dictionnary (`/encrypted_files/liste_francais.txt`) to one of your language)


## How can I decrypt or encrypt things ?

From there, you will be welcomed by a beautiful terminal prompt asking you several things. First, you will have to put your encrypted files (or the files you want to encrypt) in `motuc_project/Cryptography/encrypted_files`

You will have two choices: either use the Console or the GUI.

### Directly from the Console

If you choose this option, you will be welcomed by a list of all the files you put in the `encrypted_files` folder. 

Then you will be asked to either enter the name of the file you want to encrypt / decrypt, **or** you can leave it blank and the program will process all the files within the folder.

After confirming, you will be prompted to enter the encryption key if you know it. If you don't, no worries, leave it blank and press enter.

Finally, last prompt, if you didn't enter the encryption key, you will be asked to enter the size of the key to find. Sadly, the program cannot guess its size (yet?).

**And here we are**, the program does the magic. For each file, it will guess the key of `n` length based on a frequency analysis of the several possibilities (`n*26`). Then, the program will do a Collision Check on the provided dictionnary, and it will display a line for each file: `There's a {n}% match for the file {FILE} with the key > {key} <!`, and it will save a copy of the decrypted file under `/encrypted_files/DECRYPTED/decrypted_` followed by the name of the file.

### Using the provided Python GUI

If you select this option, you will be welcomed by the following screen:

![Main Python GUI](https://i.imgur.com/4toCRzx.png)

The left part will hold the *Encrypted Text*, with a *Browse Files* button, which prompts you to open the file you want to encrypt / decrypt, while the right part will display the *Decrypted Text*. 

In the middle, you can choose the *Encoding* for the files (currently supported: `latin_1`, `utf-8` and `iso8859_1`). 

Then you can enter the *Decrypt Key* if you got it, otherwise you can enter the *size of the encryption key*. 

Finally, the *Decrypt File* button will simply *decrypt* the file and fill the *Decrypt Key* and *Keysize* inputs according to what has been found. Same as before, a copy of the decrypted file will be saved under `/encrypted_files/DECRYPTED/decrypted_` followed by the name of the file.

Here's an example after a decryption:

![Decrypted Message GUI](https://i.imgur.com/psVVbZJ.png)

### How does it work ?

If you provide the key, it is pretty simple. Here's the recipe:

- First, we open the encrypted file with the proper encoding and store it in a string variable
- After that, it's a simple **XOR** applied like that: `for char in string: char ^ key[i]` where `i` cycles between `0` and `len(key)`
- The **XOR** method compares bytes between the two values, and returns a code, which we can get the character from by doing `chr(code)`.
- And that's it. By doing this, we can decrypt a whole file and make it readable.

Here's the actual snippet:

```python
text = []
for char, keyletter in zip(self.textfile, cycle(self.key)):
    text += chr(ord(char) ^ ord(keyletter))
```

However, it is way harder to find the encryption key. As we said before, we used a Frequency Analysis of the text while decrypting it arbitrarily. Here's the recipe:

- We separated the text in `n` blocks where `n == len(key)`. To do so, the 1st character goes to the 1st block, the 2nd to the 2nd block ... the 7th to the 1st block, the 8th to the 2nd block etc..
- After that, for each character per block and for each letter of the alphabet, we did a **XOR** operation on them: `character ^ letter`, and we incremented the counter of the result letter (if any).
- After doing that for every character of the file, we calculated the frequence of the letter `e` for each letter of the alphabet used, and we managed to have a result displaying a 6-char key with the highest chance of being the key.

And finally, we did a **Collision Check** with the French Dictionnary to be sure the words we found were actual words - **and they were**. We also found that if the result is above 70% match, then the key is right, otherwise the key has at least one wrong char.


## Credits

- [Dylan Cattelan](https://github.com/DylanCa)
- [Julien Mazzia](https://github.com/julienmazzia)
- [Ludwig Maurin-Jollis--Gally](https://github.com/Lmaurinjollis)
- [Roberto Leon Montes](https://github.com/RobertoLeonMontes)
- Pierre-Laurent Cristille (Github link coming Soon)