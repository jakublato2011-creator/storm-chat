import socket
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(("bore.pub" , int(input("port: "))))

while True:
        while True:
                c.send(input("ty: ").encode())
                data = c.recv(9999)
                print("serwer: " + data.decode())