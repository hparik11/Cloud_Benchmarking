import time, os, sys
import random
from sys import argv
import math
import multiprocessing
from timeit import Timer
import time
script, input1, input2, input3, input4 = argv



## This method is called when sequential write needs to perform. ##

def WriteToFileSeq(filename,mysize):
	
	mychar = "H"								## a single character of 1 byte
	writeloops = int(math.ceil(30*1024*1024/mysize))			## This loop actually gives the iterations. 
	
	try:
		f = open(filename, 'w+')
	except:
		raise
	for x in range(0, writeloops):
		f.write(mychar*mysize)						## Write characters times buffer size at a time.   
	f.close()
	
	
	#os.remove(filename)


## This method is called when Sequential Read needs to perform. ##

def FileToReadSeq(filename,mysize):
	
	f = open(filename, 'r+')
	readloops = int(math.ceil(30*1024*1024/mysize))
	for i in range(0,readloops):
		f.read(mysize)
	f.close()



## This method is called when Random write needs to perform. ##

def WriteToFileRnd(filename,mysize):
	
	mychar = 'H'
	writeloops = int(math.ceil(30*1024*1024/mysize))
	try:
		f = open(filename, 'w+')
	except:
		raise

	
	for i in range(0,writeloops):
		a = random.randint(0,writeloops)				## Randomly generate a number from a range. 
		f.seek(a)							## Put pointer at a specific location 		
		f.write('P'*mysize)						## Start writing characters from the pointer location
	
	f.close()


## This method is called when Random Read needs to perform. ##

def FileToReadRnd(filename,mysize):
	
	f = open(filename, 'r+')
	readloops = int(math.ceil(30*1024*1024/mysize))

	for i in range(0,readloops):
		a = random.randint(0,readloops)
		f.seek(a)				
		f.read(mysize)
	
	f.close()


## This function finds the Disk Write Speed.  ##

def DiskWriteSpeed(dirname):
	
	#maxtime = 0.5		# in sec
	filename = os.path.join(dirname,'30mb_file.txt')
	loopcounter = 0
	while True:
		try:
			if input2 == 'rnd':
				WriteToFileRnd(filename, buffersize)
			else:
				WriteToFileSeq(filename, buffersize)
		except:
			raise	
		
		loopcounter += 1

		diff = time.time() - start
		
		if loopcounter > 0:
			break


	
def solu1(jobs):
	
	for i in jobs:
     		i.start()
    
    	for i in jobs:
       		i.join()


## This function finds the Disk Read Speed.  ##

def DiskReadSpeed(dirname):

	#maxtime = 0.5 		# in sec
	filename = os.path.join(dirname,'30mb_file.txt')
	
	loopcounter = 0
	while True:
		try:
			if input2 == 'rnd':
				FileToReadRnd(filename,buffersize)
			else:
				FileToReadSeq(filename,buffersize)
		except:
			raise	
		
		loopcounter += 1
		diff = time.time() - start
		
		if loopcounter > 0:
			break

def solu2(jobs):
	
    	for i in jobs:
       		i.start()
    
    	for i in jobs:
       		i.join()



if __name__ == "__main__":
	

	if input3 == '1b':
		buffersize = 1   				## Buffer Size in Byte
		
	elif input3 == '1kb':
		buffersize = 1024					## Buffer size
		
	elif input3 == '1mb':
		buffersize = 1024*1024
		
	else:
		print "Please Give Input Properly..."  

	
	
	dirname = os.getcwd()    					## Using current working directory
	
	thread = int(input4)						## Number of Threads
	
	if input1 == 'Write':
		jobs = []
    		for i in range(thread):
       			p = multiprocessing.Process(target=DiskWriteSpeed,args=(dirname,))
       			jobs.append(p)

		start = time.time()
		solu1(jobs)
		tsec = time.time() - start
		latency = (tsec*buffersize)/(30000)			
		print "Latency = %.4f ms" %(latency) 
		#print loopcounter
		speed = (thread*30)/tsec				## Already created 30 MB file and working on it based on buffer size.. 
		
		print "Disk writing speed : %.3f MBytes/sec" % speed		
	
	
	elif input1 == 'Read':
		jobs = []
    		for i in range(thread):
       			p = multiprocessing.Process(target=DiskReadSpeed,args=(dirname,))
       			jobs.append(p)

		start = time.time()
		solu2(jobs)
		tsec = time.time() - start
		latency = (tsec*buffersize)/(30000)
		print "Latency = %.4f ms" %(latency) 
		#print loopcounter
		speed = (thread*30)/(tsec)
		
		print "Disk reading speed : %.3f MBytes/sec" % speed		
	
	else:
		print "You are looking for Some other thing..."
	
	
	
