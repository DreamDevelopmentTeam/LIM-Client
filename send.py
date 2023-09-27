import sys
from socket import *
s = socket(AF_INET, SOCK_DGRAM)
s.bind(("0.0.0.0", 65500))
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
n = input("Name=> ")
bd = ("255.255.255.255", 65000)

id = 0
if len(sys.argv) >= 2:
    t = sys.argv[1]
    if(t.isdigit()):id = int(t)

while True:
    m = input("Input> ")
    if not m: continue
    if m == "#FC":
        s.sendto(b"#FC",bd)
        continue
    if m.startswith("#P"):
        ml = m.split(" ")
        if len(ml) > 1:
            bd = (ml[1], 65000)
            print(bd)
        elif len(ml) == 1:
            bd = ("255.255.255.255", 65000)
            print(bd)
        continue
    m = str(id)+"@ " + n + ": " + m
    s.sendto(m.encode("UTF-8"), bd)