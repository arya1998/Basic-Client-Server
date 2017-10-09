import socket
import sys
import os

server_address = ('127.0.0.1', 5003)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)
flag = 0


def wordcount(str):
    words = str.split(" ")
    num_word = len(words)
    return num_word

try:
   while True:
      print "File Yang Tersedia :"
      for dir, subdir, files in os.walk('../server/dataset'):
         for file in files:
            print os.path.join(file)
      sys.stdout.write('>> ')
      paket =""
      data = sys.stdin.readline()
      jumlah = wordcount(data)
      print jumlah
      if jumlah == 2:
         data = data.split(" ",1)
         print data[0]
         for dir, subdir, files in os.walk('../server/dataset'):
            for file in files:
               if os.path.join(file) == data:
                  flag+=1
         client_socket.send(data[1])
         if data[0] == 'unduh':
            # file = open(data[1],'wb')
            # l = client_socket.recv(1024)
            while(1):
               print 'Menerima'
               l = client_socket.recv(2048)
               paket = paket + l
               # print paket
               if '\t\n\t\n' in paket:
                  header = paket.split("\t\n\t\n")
                  nama = header[0].split('\n')[0].split(":")[1]
                  print 'nama file :' + nama
                  size = header[0].split('\n')[1].split(":")[1]
                  print 'ukuran :' + size
                  if int(size)==len(header[1]):
                     break
            with open('downloads/' + nama, 'wb') as f:
               f.write(header[1])
            print "terima Selesai"
            # file.close()
         else:
               print 'Bukan Ketikan unduh'
      else:
         print 'Yang ada Masukan Kurang'

except KeyboardInterrupt:
    client_socket.close()
    sys.exit(0)