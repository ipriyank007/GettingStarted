import socket

s = socket.socket(socket.AF_INET)
s.connect((socket.gethostname(), 1234))

full_msg = ''
while True:
    msg = s.recv(8)
    if len(msg) <= 0:
        break
    full_msg += msg.decode('utf-8')
    # print(msg.decode("utf-8"))
print(full_msg)
