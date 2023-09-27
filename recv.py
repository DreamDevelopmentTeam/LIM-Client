from socket import *
s = socket(AF_INET, SOCK_DGRAM)
s.bind(("0.0.0.0", 65000))
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

while True:
    d, a = s.recvfrom(8192)
    if a[1] != 65500 and a[1] != 65000: continue
    if d.decode("UTF-8") == "#FC":
        s.sendto(b"#RET", (a[0], 65000))
        continue
    print(a,"=>",d.decode("UTF-8"))