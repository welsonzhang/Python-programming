import socket
import select

EOL1=b'\n\n'
EOL2=b'\n\r\n'

response=b'HTTP/1.0 200 OK\r\nDate:Mon,1 Jan 1996 01:01:01 GMT\r\n'
response+=b'Content-Type: text/plain\r\nContent-Length: 13\r\n\r\n'
response+=b'Hello,world!'

#Create socket object & bind the listened port
serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
serversocket.bind(('0.0.0.0',8080))
serversocket.listen(1)
serversocket.setblocking(0)

#creat epoll object & regsiter epoll read event
epoll=select.epoll()
epoll.register(serversocket.fileno(),select.EPOLLIN)

try:
  connections={}
  requests={}
  responses={}
  while True:
    #the main loop,once have I/O event,poll call will return.
    events=epoll.poll(1)
    #get the fd from event notify
    for fileno,event in events:
      #if socket readable,get the connect
      if fileno==serversocket.fileno():
        print 'accept():'
        connection,address=serversocket.accept()
        connection.setblocking(0)
        epoll.register(connection.fileno(),select.EPOLLIN)
        connections[connection.fileno()]=connection
        requests[connection.fileno()]=b''
        responses[connection.fileno()]=response
      elif event & select.EPOLLIN:
      #connection readable,handle the client,let the connection writable
        print 'EPOLLIN:'
        requests[fileno]+=connections[fileno].recv(1024)
        if EOL1 in requests[fileno] or EOL2 in requests[fileno]:
          epoll.modify(fileno,select.EPOLLOUT)
          print('-'*40+'\n'+requests[fileno].decode()[:-2])
      elif event & select.EPOLLOUT:
        print 'EPOLLOUT'
        byteswritten=connections[fileno].send(responses[fileno])
        responses[fileno]=responses[fileno][byteswritten:]
        if len(responses[fileno])==0:
            epoll.modify(fileno,0)
            connections[fileno].shutdown(socket.SHUT_RDWR)
      elif event & select.EPOLLHUP:
        print 'EPOLLHUP'
        epoll.unregister(fileno)
        connections[fileno].close()
        del connections[fileno]
finally:
    print 'finally'
    epoll.unregister(serversocket.fileno())
    epoll.close()
    serversocket.close()
   
