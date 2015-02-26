import socket
import udp

DPORT = 1337
DIP   = "10.0.23.62" # ipaddr of cod4_fix_server.py

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(("0.0.0.0",28960))

while True:
    try:
        data,addr = sock.recvfrom(1024)
	ipaddr = addr[0]
	port   = addr[1]
	print ipaddr, data
        msg = ipaddr + ":" + str(port) 
	sock2 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	sock2.sendto(msg, (DIP, DPORT))
    except:
        None
	
