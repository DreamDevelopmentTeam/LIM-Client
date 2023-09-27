from socket import *
s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
n = input("Name=> ")
bd = ("255.255.255.255", 65000)
while True:
    m = input("Input> ")
    if not m: continue
    if m == "#FC":
        s.sendto(b"#FC",bd)
        continue
    m = n + ": " + m
    s.sendto(m.encode("UTF-8"), bd)