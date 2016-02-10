import sys
from time import sleep
from random import random
import sys
from sys import argv

#script, input1 = argv
import multiprocessing
from timeit import Timer
import socket


def ThreadServer(n,port):
        host = '127.0.0.2'
	
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind((host,port))
	print "Server %d Started" %n

        f = open('fill.bin','wb')
	while True:
		
                data, addr = s.recvfrom(1024)
		print "Connection from : " +  str(addr)
                if not data:
                        break
                print "From connected user "+ str(data)
                f.write(data)
 		print "Sending :" +str(data)
		s.sendto(data,addr)
	f.close()
	s.close()

if __name__ == '__main__':

	thread = 2 #int(input1)
	
	if thread == 1:
	
		t1 = multiprocessing.Process(target=ThreadServer,args=(1,5184))
		t1.start()
		t1.join()
	else:
		t1 = multiprocessing.Process(target=ThreadServer,args=(1,6780))
		t1.start()
		t2 = multiprocessing.Process(target=ThreadServer,args=(2,2589))
		t2.start()
		t1.join()
		t2.join()
	

