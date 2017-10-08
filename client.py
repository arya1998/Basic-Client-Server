import socket
import sys
import os

server_address = ('127.0.0.1',5000)
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(server_address)


try:
	while True:
		print "File Yang Tersedia :"
		for dir, subdir, files in os.walk('dataset'):
			for file in files:
				print os.path.join(file)
		sys.stdout.write('>> ')
		paket =""
		data = sys.stdin.readline().split(" ",1)
		client_socket.send(data[1])
		if data[0] == 'unduh':
			file = open(data[1],'wb')
			# l = client_socket.recv(1024)

			while(1):
				print 'Menerima'
				l = client_socket.recv(1024)
				paket = paket + l
				# print paket
				if '\t\n\t\n' in paket:
					header = paket.split("\t\n\t\n")
					nama = header[0].split('\n')[0].split(":")[1]
					print nama
					size = header[0].split('\n')[1].split(":")[1]
					print size
					if int(size)==len(header[1]):
						break
			file.close()
			with open('download/'+nama, 'wb') as f:
				f.write(header[1])
			print "terima Selesai"

		client_socket.close()



except KeyboardInterrupt:
	client_socket.close()
	sys.exit(0)
