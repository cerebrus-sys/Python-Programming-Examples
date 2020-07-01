'''
 ' Python program to verify <MD5/SHA1/SHA256/SHA512> hashes of a file using hashlib module.
 ' @author: Sanjan Geet Singh
'''

from hashlib import md5, sha1, sha256, sha512   # hashlib module
from sys import argv

if len(argv) != 3:      # Insufficient number of arguments supplied
      print("Usage: python \"Hash Verifier.py\" [file to hash] [hash]")
      exit()

file = argv[1]
vhash = argv[2].lower() # given hash
      
try:
      file = open(file, 'rb')
      contents = file.read()
      file.close()
except FileNotFoundError:
      print("[ERROR] File Not Found")
      exit()

vl = len(vhash)   # length of given hash

if vl == 32:      # MD5
      ghash = md5(contents)
elif vl == 40:    # SHA1
      ghash = sha1(contents)
elif vl == 64:    # SHA256
      ghash = sha256(contents)
elif vl == 128:   # SHA512
      ghash = sha512(contents)
else:
      print("[ERROR] Unknown Algorithm")
      exit()

ghash = ghash.hexdigest()     # generated hash in hex form

if ghash == vhash:
      print("Status: OK")
else:
      print("Status: ERROR")
      print("Given Hash:", vhash)
      print("Generated Hash:", ghash)
