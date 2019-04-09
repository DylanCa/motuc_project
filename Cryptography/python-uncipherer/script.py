from functions.decryptor import Decryptor
from functions.collisions import Collisions

print(
    "\n------------------------------------------------------------------------------------------------------"
)
print(
    "|           Here, you will be able to Encrypt / Decrypt your files using the Vernam Cipher           |"
)
print(
    "| Please be sure that the files you want to decrypt are in the folder located at ../encrypted_files. |"
)
print(
    "|                                                                                                    |"
)

print(
    "| This ( little ) program has been made by https://github.com/DylanCa during his 4th IT Student year |"
)
print(
    "|                             Feel free to star the project on Github !                              |"
)
print(
    "------------------------------------------------------------------------------------------------------\n"
)

Decryptor().decrypt()
