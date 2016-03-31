import socket,ssl,time

context=ssl.SSLContext(ssl.PROTOCOL_TLSv1)
context.load_cert_chain(certfile="cert.pem",keyfile="key.pem")

bindsocket=socket.socket()
bindsocket.bind(('191.8.1.235',10023))
bindsocket.listen(5)

def do_something(connstream,data):
    print('data length:',len(data))
    return True

def deal_with_client(connstream):
    t_recv=0
    t_send=0
    n=0
    t1=time.clock()
    data=connstream.recv(1024)
    t2=time.clock()
    print('receive time:',t2-t1)
    #empty data means the client is finished with us
    while data:
        if not do_something(connstream,data):
            #we will assume do_something returns False
            #when we are finished with client
            break
        n=n+1
        t1=time.clock()
        connstream.send(b'b'*1024)
        t2=time.clock()
        t_send+=t2-tl1
        print('send time:',t2-t1)
        t1=time.clock()
        data=connstream.recv(1024)
        t2=time.clock()
        t_recv+=t2-t1
        print("receive time:",t2-t1)
    
    print('avg send time:',t_send)
    #finished with client
    
    while True:
        newsocket, fromaddr = bindsocket.accept()
        connstream = context.wrap_socket(newsocket, server_side = True)
        try:
            deal_with_client(connstream)
        finally:
            connstream.shutdown(socket,SHUT_RDWR)
            constream.close()

