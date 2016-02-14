import sys
from time import sleep
from random import random
import sys
from sys import argv

script, input1, input2 = argv				## Command line argument
import multiprocessing
from timeit import Timer
import socket
import time

def ThreadClient(n,p,port):
	host = '172.51.31.20'				## Server IP Address
	
	s = socket.socket()				## Socket initialization
	s.connect((host,port))				## Connection establishment
	
	for i in range(p):
		f = open(packet+'_file','rb')		## File Opening
		l = f.read(1024)			## File Reading

		while l :
			s.send(l)			## Packet sending to server
			l = f.read(1024)
			data = s.recv(1024)		## Packets receive from server

		f.close()				## File Close
		
	s.close()					## Socket close

def solu1(t1):
	
        t1.start()					## Thread starts & this function is for 1 thread. 
	t1.join()

def solu2(jobs):
	
	for i in jobs:					## Threads start & this function is for 2 thread.
		i.start()
	
	for i in jobs:
		i.join()

if __name__ == '__main__':

	thread = int(input2)
	packet = input1
	f = open(packet+'_file','rb')
	l = f.read()
	buffer = len(l)
	filesize = buffer

	if buffer == 1:
		m = 10000
	elif buffer == 1024:
		m = 100
	elif buffer == 65536:
  		m = 0.0625
	else:
		print "Something went Wrong"	

	if thread == 1:
		t1 = multiprocessing.Process(target=ThreadClient,args=(1,int(m*buffer),5184))		## 
		start = time.time()
		solu1(t1)
		end = time.time()
		t = (end-start)*1000
		print "Latency for TCP is : %.3f ms" %(t)
		throughput = (1000*m*buffer*filesize*8)/(t*1024*1024)
		print "Throughput is : %.3f Mega Bits/Sec.." %throughput
	
	else:
		jobs = []
		t1 = multiprocessing.Process(target=ThreadClient,args=(1,int(m*buffer/2),6780))
		jobs.append(t1)
		t2 = multiprocessing.Process(target=ThreadClient,args=(2,int(m*buffer/2),2589))
		jobs.append(t2)
		start = time.time()
		solu2(jobs)
		end = time.time()
		t = (end-start)*1000
		print "Latency for TCP is : %.3f ms" %t
		throughput = (1000*m*buffer*filesize*8)/(t*1024*1024)
		print "Throughput is : %.3f Mega Bits/Sec.." %throughput
	
	f.close()
