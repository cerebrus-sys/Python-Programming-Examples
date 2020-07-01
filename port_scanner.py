'''
 ' Python program to scan ports of a web server
 ' @author: Sanjan Geet Singh
'''

from socket import socket

host = input("Enter Target's IP Address (or Domain Name): ")

min_port = input("Enter Lower Port Range (default: 1): ")
if min_port == '':
      min_port = 1
else:
      min_port = int(min_port)

max_port = input("Enter Upper Port Range (default: 65535): ")
if max_port == '':
      max_port = 65536
else:
      max_port = int(max_port)

timeout = input("Enter Timeout (in seconds): ")
if timeout == '':
      timeout = 2
else:
      timeout = int(timeout)

mode = input("Enter Mode ('A' for short mode, 'B' for long mode): ").upper()

if mode == 'A':
      for port in range(min_port, max_port):
            s = socket()
            s.settimeout(timeout)
            if s.connect_ex((host, port)) == 0:
                  print("[OPEN]", port)
            s.close()
elif mode == 'B':
      for port in range(min_port, max_port):
            s = socket()
            s.settimeout(timeout)
            print(port, s.connect_ex((host, port)))
            s.close()
else:
      print("[ERROR] Unknown Mode")
