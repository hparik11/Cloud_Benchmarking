import sys
from time import sleep
from random import random
import sys
from threading import Thread, Lock, Semaphore
import threading
from timeit import Timer
import socket

def ThreadClient(n,l,port):
	host = '127.0.0.6'
	
	s1 = socket.socket()
	s1.bind((host,port))
	
	s1.listen(1)
	c1, addr1 = s1.accept()
	print "thread %d is running" %n
	print "Connection from : " +  str(addr1)

	while True:
		data = c1.recv(2048)
		if not data:
			break
		
		print str(data)
		c1.send(data.upper())
	c1.close()


if __name__ == '__main__':
	f = open('1kb_file','rb')
	l = (f.read())
	buffer = len(l)
	#print len(l)
	t1 = Thread(target=ThreadClient,args=(1,l,5000))
        t1.start()
	t2 = Thread(target=ThreadClient,args=(2,l,5001))
        t2.start()
	
