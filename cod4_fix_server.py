import socket
import json
import udp


servers = [
	{"ip":"10.0.23.62","port":28960,"hostname":"vanilla"},
	{"ip":"10.0.23.62","port":28961,"hostname":"killtheking"},
	{"ip":"10.0.23.62","port":28962,"hostname":"gungame"},
	{"ip":"10.0.23.62","port":28963,"hostname":"leetmod19"},
]
msg = b"\xff\xff\xff\xffinfoResponse\n\\challenge\\xxx\\protocol\\6\\hostname\\COD4HOST\\mapname\\mp_cargoship\\sv_maxclients\\24\\gametype\\war\\pure\\0\\kc\\1\\hw\\2\\mod\\0\\voice\\0\\pb\\0"

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(("0.0.0.0",1337))

while True:
    try:
	data,addr = sock.recvfrom(1024)
	print data
	(ipaddr,port) = data.split(":")
	port = int(port)
	for server in servers:
		print server["hostname"]
		msg = b"\xff\xff\xff\xffinfoResponse\n\\challenge\\xxx\\protocol\\6\\hostname\\"+server["hostname"]+"\\mapname\\mp_cargoship\\sv_maxclients\\24\\gametype\\war\\pure\\0\\kc\\1\\hw\\2\\mod\\0\\voice\\0\\pb\\0"
		udp_packet = udp.Packet()
		udp_packet.sport = server["port"];
		udp_packet.dport = port;
		udp_packet.data = msg
		packet = udp.assemble(udp_packet, 0)
		print packet
		cod4client = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
		cod4client.sendto(packet, (ipaddr, 0))

    except:
        None	
