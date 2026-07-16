import socket
import time
import subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("0.0.0.0" , 5000))
s.listen()
subprocess.Popen("bore local 5000 --to bore.pub > bore.txt", shell = True)
time.sleep(2)
subprocess.run("cat bore.txt", shell = True)

while True:
        conn , addr = s.accept()
        while True:
                data = conn.recv(9999)
                print("klient: " + data.decode())
                conn.send(input("ty: ").encode())