import socket
import time

s = socket.socket()
host = "10.0.2.15"
port = 12000
k=5
s.settimeout(5) 

try:
    s.connect((host, port))
    messages = ["message 1", "message 2", "message 3","message 4"]

    for message in messages:
        while True:
            try:
                s.send(message.encode())
                response = s.recv(1024).decode()
                print("Server response:", response)
                break  
            except socket.timeout:
                print("Timeout occurred. Retrying...")
                k=k*math.exp(time)
                time.sleep(k)  

except socket.error as e:
    print(f"Error: {e}")

finally:
    s.close()

