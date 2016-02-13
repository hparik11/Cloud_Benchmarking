import sys
from time import sleep
from random import random
import sys
from sys import argv

script, input1 = argv
import multiprocessing
from timeit import Timer
import socket

def ThreadServer(n,port):
	host = ''						## put a host at server side as '' so that it can accepts the requests from 
								## other clients 
	
	s1 = socket.socket()
	s1.bind((host,port))					
	
	s1.listen(1)						## listening on port
	c1, addr1 = s1.accept()					## accept requests from client.
	print "Thread %d is running" %n
	print "Connection from : " +  str(addr1)
	
	f = open('fill.bin','wb')
	while True:
		
		data = c1.recv(1024)				## This loop runs until there is no data coming from client side. 
		if not data:
			break
		
		f.write(data)
		c1.send("File Received...")

	f.close()
	c1.close()
	s1.close()



## Main method  ##

if __name__ == '__main__':

	thread = int(input1)									## Thread input
	
	if thread == 1:
	
		t1 = multiprocessing.Process(target=ThreadServer,args=(1,5184))			## Create a process	
		t1.start()									## Start a process
		t1.join()									## at last joining a process
	else:
		t1 = multiprocessing.Process(target=ThreadServer,args=(1,6780))
		t1.start()
		t2 = multiprocessing.Process(target=ThreadServer,args=(2,2589))
		t2.start()
		t1.join()
		t2.join()
	
