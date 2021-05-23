from multiping import MultiPing
import socket
ip = socket.gethostbyname('6.tcp.ngrok.io:11504')
ip = socket.create_connection(ip, timeout=timeout)
       #$ self.socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
mp = MultiPing([ip, ip])
mp.send()
no_responses = mp.recieve(1)