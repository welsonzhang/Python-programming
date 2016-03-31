import socket,ssl,pprint,time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#require a certificate from the server
ssl_sock = ssl.wrap_socket(s, ca_certs="cert.pem", cert_reqs=ssl.CERT_REQUIRED)

ssl_sock.connect(('191.8.1.235', 10023))

pprint.pprint(ssl_sock.getpeercert())

#note that closing the SSLSocket will also close the underlying socket
n = 0
t_send = 0
t_recv = 0
while n < 1000:
    n = n+1
    t1 = time.clock()
    ssl_sock.send(b'a'*100)
    t2 = time.clock()
    t_send += t2-t1
    print("send time:", t2-t1)
    t1 = time.clock()
    data = ssl_sock.recv(1024)
    t2 = time.clock()
    t_recv += t2-t1
    print("receive time:", t2-t1)
    print(len(data))
    print("avg send time:", t_send/n, "avg receive time:", t_recv/n)
    ssl_sock.send(b'')
    ssl_sock.close()
