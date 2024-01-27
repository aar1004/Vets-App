# encryptying data
# hello -> encrypt() -> 456789hwgdjk -> one way encryption cannot be decrypted

import hashlib

password = input("enter your password:")
# encode password to utf 8
password = password.encode("utf-8")
# generate the secure SHA 256 hash
password = hashlib.sha256(password).hexdigest
print(password)
