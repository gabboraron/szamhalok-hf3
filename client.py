import socket
import struct
import random
import time

#import os

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 22223)

connection.connect(server_address)


searching = True
sign = ["<", ">", "="]
idx = 50
sidx = 0
lastSidx = 0
#print("LOG:\tStarting...")
while searching:
	#values = (str(input()).encode('UTF-8'), int(input()))
	greater = True
	lower = True

	delay = random.randint(1,5)
	time.sleep(delay)
	#print("LOG: \ttrying: " + str(idx))
	#os.system('spd-say "trying "'+ str(idx))

	sidx 		= 0
	value1 		= sign[0]
	value2 		= idx
	#value = (str(sign[0]), int(idx))
	packer 		= struct.Struct('1s I')
	packed_data = packer.pack(value1.encode('utf-8'), value2)
	#packed_data = packer.pack(*value)
	connection.send(packed_data)
	data = connection.recv(1024)
	#print(data.decode('UTF-8'))
	if (data.decode('UTF-8') == "Igen"):	#kisebb mint a mi ertekunk
		#print("LOG:\tLower")
		idx = idx -1
		lower = False
		lastSidx = 0


	sidx 		= 1
	values 		= (sign[sidx].encode('utf-8'), idx)
	packer 		= struct.Struct('1s I')
	packed_data = packer.pack(*values)
	connection.send(packed_data)
	data = connection.recv(1024)
	#print(data.decode('UTF-8'))	
	if (data.decode('UTF-8') == "Igen"):	#nagyobb mint a mi ertekunk
		#print("LOG:\tGreater")
		idx = idx + 1
		greater = False
		lastSidx = 1 
			


	if (greater and lower):
		#print("LOG:\tWin")
		sidx 		= 2
		values 		= (sign[sidx].encode('utf-8'), idx)
		packer 		= struct.Struct('1s I')
		packed_data = packer.pack(*values)
		connection.send(packed_data)
		data = connection.recv(1024)

		#if (data.decode('UTF-8') == "Nyertél"):	#ugyanaz mint a mi ertekunk		
			#vege
			#print("NYERTEM")
		#else:
			#vesztettem
			#print("VESZTETTEM")	
		searching = False
		connection.close()
	
	if (data.decode('UTF-8') == "Vége"):	#vege		
		searching = False
		connection.close()
	
	

