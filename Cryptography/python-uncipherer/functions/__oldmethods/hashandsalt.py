import hashlib
import itertools


class HashAndSalt:
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    def hashandsaltpassword(self, password, salt):
        salted = []
        md5list = []
        sha1list = []

        for x in range(len(salt)):
            salted.append(
                [x for x in itertools.permutations([password, salt[x]])])
            for y in range(len(salted[x])):
                salted[x][y] = ''.join(salted[x][y])

        flat_salted = [item for sublist in salted for item in sublist]

        for item in flat_salted:
            md5list.append(
                [item, hashlib.md5(item.encode('utf-8')).hexdigest()])
            sha1list.append(
                [item, hashlib.sha1(item.encode('utf-8')).hexdigest()])

        return [md5list, sha1list]
