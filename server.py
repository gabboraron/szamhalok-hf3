import socket
import struct
import random

#import os

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 22223)
sock.bind(server_address)

sock.listen(1)
connection, client_address = sock.accept()
number = random.randint(1,100)

#print("LOG:\tStarting...")
#print("number: " + str(number))
guessed = False
#os.system('spd-say "Startin, the base is "'+ str(number))
while True:
	while (guessed == False):
		data = connection.recv(1024)
		unpacker = struct.Struct('1s I')
		unpacked_data = unpacker.unpack(data)

		#print("LOG: \t guess: " + str(unpacked_data[1]))
		if unpacked_data[0].decode('UTF-8') == ">":
			if eval(str(number) + str(unpacked_data[0].decode('UTF-8')) + str(unpacked_data[1])):
				#print(">")
				reply = str("Igen")
			else:
				#print("<")
				reply = str("Nem")
			
		elif unpacked_data[0].decode('UTF-8') == "<":
			if eval(str(number) + str(unpacked_data[0].decode('UTF-8')) + str(unpacked_data[1])):
				#print("<")
				reply = str("Igen")
			else:
				#print(">")
				reply = str("Nem")

		elif unpacked_data[0].decode('UTF-8') == "=":
			if eval(str(number) + str("==") + str(unpacked_data[1])):
				#print("=")
				reply = str("Nyertél")
			else:
				#print("!=")
				reply = str("Kiestél")
			guessed = True

		#reply = str(unpacked_data[0].decode('UTF-8')) + str(unpacked_data[1])

		connection.send(str(reply).encode('UTF-8'))
	reply = "Vége"
	connection.send(str(reply).encode('UTF-8'))

#connection.close()