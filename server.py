import socket
import select
import sys
import os


server_address = ('127.0.0.1',5003)
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server_socket.bind(server_address)
server_socket.listen(5)

input_socket=[server_socket]
print 'Server Listening...'

try:
   while True:
         read_ready,write_ready,exception = select.select(input_socket,[],[])

         for sock in read_ready:
            if sock ==server_socket:
               client_socket,client_address = server_socket.accept()
               input_socket.append(client_socket)

            else:
               data = sock.recv(2048)
               if data:
                  print sock.getpeername()
                  data2 = data.replace("\n","")
                  print 'nama data yang di unduh adalah: '+ data2
                  tempat = 'dataset/'+data2
                  with open(tempat, 'rb') as file:
                     data1 = file.read()
                     # print data1
                  header = "name:"+data2+"\nsize:" + str(len(data1)) +'\t\n\t\n'
                  paket = header+data1
                  sock.sendall(paket)
                  print "sudah dikirim"
               else:
                  sock.close()
                  input_socket.remove(sock)

except KeyboardInterrupt:
   server_socket.close
   sys.exit(0)