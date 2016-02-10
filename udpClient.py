import sys
from time import sleep
from random import random
import sys
from sys import argv

#script, input1, input2 = argv
import multiprocessing
from timeit import Timer
import socket
import time


def ThreadClient(n,p,c_port,s_port):
        host = '127.0.0.1'
        
	server = ('127.0.0.2',s_port)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind((host,c_port))

        #start = time.time()
	for i in range(10):
		f = open(packet+'_file','rb')
		l = f.read(1024)
		while l :
		        s.sendto(l, server)
			l = f.read(512)
		        data, addr = s.recvfrom(1024)
		        #print "Received from Server " + str(data)
                
        
	s.close()

def solu1():
	t1 = multiprocessing.Process(target=ThreadClient,args=(1,int(m*buffer),5006,5184))
        t1.start()
	t1.join()

def solu2():
	t1 = multiprocessing.Process(target=ThreadClient,args=(1,int(m*buffer/2),5988,6780))
	t1.start()
	t2 = multiprocessing.Process(target=ThreadClient,args=(2,int(m*buffer/2),6588,2589))
	t2.start()

	t1.join()
	t2.join()


if __name__ == '__main__':
        
	thread = 2 #int(input2)
	packet = '1kb' #input1
	f = open(packet+'_file','rb')
	l = f.read()
	buffer = len(l)
	#print buffer

	if buffer == 1:
		m = 100000
	elif buffer == 1024:
		m = 100
	elif buffer == 65536:
  		m = 0.0625
	else:
		print "Something went Wrong"	

	if thread == 1:
		start = time.time()
		solu1()
		end = time.time()
		t = (end-start)*1000
		print "Elapsed Time for UDP is : %.3f ms" %(t)
		throughput = (1000*m*buffer*buffer*8)/(t*1024*1024)
		print "Throughput is : %.3f Mega Bits/Sec.." %throughput
	
	else:
		start = time.time()
		solu2()
		end = time.time()
		t = (end-start)*1000
		print "Elapsed Time for UDP is : %.3f ms" %t
		throughput = (1000*m*buffer*buffer*8)/(t*1024*1024)
		print "Throughput is : %.3f Mega Bits/Sec.." %throughput
	
	f.close()

