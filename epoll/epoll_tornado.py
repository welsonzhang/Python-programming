import errno
import functools
import tornado.ioloop
import socket

def handle_connection(connection,address):
    #handle connection & return data for client
    data=connection.recv(2014)
    print data
    connection.send(data)

def connection_ready(sock,fd,events):
    #event call back function,for socket readable & get socket connection
    while True:
      try:
        connection,address=sock.accept()
      except socket.error as e:
        if e.args[0] not in (errno.EWOULDBLOCK,errno.EAGAIN):
          raise
        return
      connection.setblocking(0)
      handle_connection(connection,address)

if __name__=='__main__':
   sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
   sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
   sock.setblocking(0)
   sock.bind(("",5000))
   sock.listen(128)
   #use epoll interface in tornado:IOLoop object
   io_loop=tornado.ioloop.IOLoop.current()
   callback=functools.partial(connection_ready,sock)
   #io_loop object register network io fd & call back function with io event
   io_loop.add_handler(sock.fileno(),callback,io_loop.READ)
   io_loop.start()
   

