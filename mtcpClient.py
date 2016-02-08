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
	
	s = socket.socket()
	s.connect((host,port))
	print "thread %d is running" %n
	msg = raw_input("enter the string ")
	while msg != 'q':
		data = str(msg)
		s.send(data)
		data1 = s.recv(1024)
		print str(data1)
		
		#print "Received from Server..... "
		msg = raw_input("enter the string ")
	s.close()


if __name__ == '__main__':
	f = open('1kb_file','rb')
	l = (f.read())
	buffer = len(l)
	#print len(l)
	t1 = Thread(target=ThreadClient,args=(1,l,5000))
        t1.start()
	t2 = Thread(target=ThreadClient,args=(2,l,5001))
        t2.start()
	
