import sys
from socket import *
gp=65000
sp=65500
s=socket(AF_INET,SOCK_DGRAM)
s.bind(("0.0.0.0",gp))
s.setsockopt(SOL_SOCKET,SO_BROADCAST, 1)
id=0
if len(sys.argv)>=2:
    t=sys.argv[1]
    if(t.isdigit()):id=int(t)
while True:
    d,a=s.recvfrom(8192)
    dc=d.decode("UTF-8")
    if a[1]!=sp and a[1]!=gp: continue
    if not dc.startswith(str(id)+"@"): continue
    if dc=="#FC" or dc==(str(id)+"@#FC"):
        s.sendto(b"#RET", (a[0], gp))
        continue
    print(a,"=>",dc)