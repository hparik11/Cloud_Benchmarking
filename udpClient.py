import sys
from time import sleep
from random import random
import sys
from sys import argv

script, input1, input2 = argv
import multiprocessing
from timeit import Timer
import socket
import time,math


def ThreadClient(n,p,c_port,s_port):
        host = '127.0.0.4'
        
	server = ('127.0.0.2',s_port)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind((host,c_port))

        
	for i in range(2*p):
		f = open(packet+'_file','rb')
		l = f.read(1024)
		
		while l :
		        s.sendto(l, server)
			l = f.read(1024)
		        data, addr = s.recvfrom(1024)
		        #print "Received from Server " + str(data)
                f.close()
        
	s.close()

def solu1(t1):

	t1.start()
	t1.join()

def solu2(jobs):

	for i in jobs:
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
	#print buffer

	if buffer == 1:
		m = 100
	elif buffer == 1024:
		m = 0.01
	elif buffer == 65536:
  		m = 0.0001
	else:
		print "Something went Wrong"	

	if thread == 1:
		t1 = multiprocessing.Process(target=ThreadClient,args=(1,int(m*buffer),5017,8988))
		start = time.time()
		solu1(t1)
		end = time.time()

		t = (end-start)*1000
		print "Elapsed Time for UDP is : %.3f ms" %(t)
		throughput = (10000*thread*m*buffer*filesize*8)/(t*1024*1024)
		print "Throughput is : %.3f Mega Bits/Sec.." %throughput
		
	
	elif thread == 2:
		jobs = []
		t1 = multiprocessing.Process(target=ThreadClient,args=(1,int(math.ceil(m*buffer/2)),5988,6889))
		jobs.append(t1)
		t2 = multiprocessing.Process(target=ThreadClient,args=(2,int(math.ceil(m*buffer/2)),6588,2899))
		jobs.append(t2)

		start = time.time()
		solu2(jobs)
		end = time.time()

		t = (end-start)*1000
		print "Elapsed Time for UDP is : %.3f ms" %t
		throughput = (10000*thread*m*buffer*filesize*8)/(t*1024*1024)
		print "Throughput is : %.3f Mega Bits/Sec.." %throughput
		

	f.close()

