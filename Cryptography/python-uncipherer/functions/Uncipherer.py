from functions.hashandsalt import HashAndSalt


class Uncipherer:
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    def hashandsalt(self):
        password = input("Enter the password to hash: ").replace(' ', '')

        salt = [
            x for x in input(
                "Enter the salts to apply (separate with a comma, if multiple): "
            ).replace(' ', '').split(',')
        ]

        hashlist = HashAndSalt.hashandsaltpassword(HashAndSalt, password, salt)

        print("MD5 hashes: {}".format(hashlist[0]))
        print("SHA1 hashes: {}".format(hashlist[1]))

    def find6charpassword():
        pass
