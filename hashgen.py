'''
 ' Python program to generate <MD5/SHA1/SHA256/SHA512> hashes of a file using hashlib module
 ' @author: Sanjan Geet Singh
'''

from hashlib import md5, sha1, sha256, sha512   # hashlib module
from sys import argv

if len(argv) != 3:      # Insufficient number of arguments supplied
      print("Usage: python \"Hash Generator.py\" [Algorithm] [File to Hash]")
      print("Algorithms Avaliable: md5, sha1, sha256, sha512")
      exit()

algorithm = argv[1].lower()
file_to_hash = argv[2]

try:
      file = open(file_to_hash, 'rb')
      contents = file.read()
      file.close()
except FileNotFoundError:
      print("[ERROR] File Not Found")
      exit()

if algorithm == 'md5':
      ghash = md5(contents)
elif algorithm == 'sha1':
      ghash = sha1(contents)
elif algorithm == 'sha256':
      ghash = sha256(contents)
elif algorithm == 'sha512':
      ghash = sha512(contents)
else:
      print("[ERROR] Unknown Hashing Algorithm")
      exit()

ghash = ghash.hexdigest()     # convert generated hash to hex form
print(ghash)
