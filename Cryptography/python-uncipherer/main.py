import hashlib
import itertools

md5list = []
sha1list = []

# Asks the user to enter text + the salt words
# password = input("Enter the password to hash: ").replace(' ', '')

# salt = [
#     x for x in input(
#         "Enter the salts to apply (separate with a comma, if multiple): ").
#     replace(' ', '').split(',')
# ]

password = "romain"
salt = ["exar", "julio", "sebastian"]

salted = []

for x in range(len(salt)):
    salted.append([x for x in itertools.permutations([password, salt[x]])])
    for y in range(len(salted[x])):
        salted[x][y] = ''.join(salted[x][y])

flat_salted = [item for sublist in salted for item in sublist]

for item in flat_salted:
    md5list.append(hashlib.md5(item.encode('utf-8')).hexdigest())
    sha1list.append(hashlib.sha1(item.encode('utf-8')).hexdigest())

print("MD5 hashes: {}".format(md5list))
print("SHA1 hashes: {}".format(sha1list))
