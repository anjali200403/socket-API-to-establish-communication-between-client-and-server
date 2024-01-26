import socket

s = socket.socket()
host = "10.0.2.15"
port = 12000
k=5

s.bind((host, port))
print("Listening")
s.listen(10)
c, addr = s.accept()
print("Connected with:", addr)

while True:
    try:
        data, client_addr = c.recvfrom(1024)
        if not data:
            break

        print("Received data:", data.decode())
        c.send("Data received".encode())
    except socket.timeout:
        print("Timeout occurred. Retransmitting...")
        k=k*math.exp(time)
        time.sleep(k)  


c.close()


