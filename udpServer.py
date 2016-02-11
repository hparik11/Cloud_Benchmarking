import sys
from time import sleep
from random import random
import sys
from sys import argv
from socket import *

script, input1 = argv
import multiprocessing
from timeit import Timer
import socket


def ThreadServer(n,port):
        host = '127.0.0.2'
	
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind((host,port))
	print "Server %d Started" %n

        f = open('fill.bin','wb')
	try:
		while True:
			
		        data, addr = s.recvfrom(1024)
			print "Connection from : " +  str(addr)
		        if not data:
				
		        	break
			s.settimeout(2)
		        print "From connected user "+ str(data)
		        f.write(data)
	 		print "Sending :" +str(data)
			s.sendto(data,addr)
	except timeout:
		f.close()
		
		s.close()

if __name__ == '__main__':

	thread = int(input1)
	
	if thread == 1:
	
		t1 = multiprocessing.Process(target=ThreadServer,args=(1,8988))
		t1.start()
		t1.join()
	
	else:
		t1 = multiprocessing.Process(target=ThreadServer,args=(1,6889))
		t1.start()
		t2 = multiprocessing.Process(target=ThreadServer,args=(2,2899))
		t2.start()
		t1.join()
		t2.join()
	
