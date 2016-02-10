import time, os, sys
import random
from sys import argv
import math
import multiprocessing
from timeit import Timer
import time
script, input1, input2, input3, input4 = argv

def WriteToFileSeq(filename,mysizeKB):
	
	mystring = "Hi This is Harsh Parikh."
	writeloops = int(math.ceil(1024*mysizeKB/len(mystring)))
	#print "loops : %d " %writeloops
	try:
		f = open(filename, 'w')
	except:
		raise
	for x in range(0, writeloops):
		f.write(mystring)
	f.close()
	
	
	#os.remove(filename)

def FileToReadSeq(filename):
	
	f = open(filename, 'rb')
	f.read()
	f.close()

def WriteToFileRnd(filename,mysizeKB):
	
	mychar = 'H'
	writeloops = int(math.ceil(1024*mysizeKB/len(mychar)))
	try:
		f = open(filename, 'wb')
	except:
		raise
	a = random.randint(0,int(math.ceil(mysizeKB*1024)))
	
	
	f.seek(a)	
		
	for i in range(a,writeloops):
		f.write('P')
	
	f.seek(0)
	
	for x in range(0, a):
		f.write(mychar)

	f.close()

def FileToReadRnd(filename,mysizeKB):
	
	f = open(filename, 'rb')
	a = random.randint(0,int(math.ceil(mysizeKB*1024)))
	f.seek(a)
	f.read()
	f.seek(0)
	f.read(a)
	f.read()
	f.close()


def DiskWriteSpeed(dirname):
	
	#maxtime = 10 		# in sec
	filename = os.path.join(dirname,'WriteFile.txt')
	start = time.time()
	loopcounter = 0
	while True:
		try:
			if input2 == 'rnd':
				WriteToFileRnd(filename, filesize)
			else:
				WriteToFileSeq(filename, filesize)
		except:
			raise	
		
		loopcounter += 1

		diff = time.time() - start
		
		if loopcounter > (bs/thread):
			break

	
	

def solu1():
	jobs = []
    	for i in range(thread):
       		p = multiprocessing.Process(target=DiskWriteSpeed,args=(dirname,))
       		jobs.append(p)
       		p.start()
    
    
    	for i in range(len(jobs)):
       		p.join()



def DiskReadSpeed(dirname):

	#maxtime = 0.5 		# in sec
	filename = os.path.join(dirname,'WriteFile.txt')
	start = time.time()
	loopcounter = 0
	while True:
		try:
			if input2 == 'rnd':
				FileToReadRnd(filename,filesize)
			else:
				FileToReadSeq(filename)
		except:
			raise	
		
		loopcounter += 1
		diff = time.time() - start
		
		if loopcounter > (bs/thread):
			break

	

def solu2():
	jobs = []
    	for i in range(thread):
       		p = multiprocessing.Process(target=DiskReadSpeed,args=(dirname,))
       		jobs.append(p)
       		p.start()
    
    
    	for i in range(len(jobs)):
       		p.join()



if __name__ == "__main__":
	

	if input3 == '1b':
		filesize = 0.001   #Size in kb
		bs = 100000

	elif input3 == '1kb':
		filesize = 1
		bs = 10000
	elif input3 == '1mb':
		filesize = 1024
		bs = 100
	else:
		print "Please Give Input Properly..."  

	
	
	dirname = os.getcwd()    # Using current working directory
	#filesize = 1024      # Size in KB
	#access = input2
	#thread = int(raw_input("Enter no of threads: "))
	thread = int(input4)	
	#bs = 100
	#input2 = 'seqn'
	#input1 = 'Write'
	
	if input1 == 'Write':
		start = time.time()
		solu1()
		tsec = time.time() - start
		latency = (tsec*1000)/(filesize*bs*1024)
		print "Latency = %.4f ms" %(tsec*1000/bs) 
		#print loopcounter
		speed = (bs*filesize)/tsec
		speed /= 1000
		print "Disk writing speed : %.3f MBytes/sec" % speed		
	
	
	elif input1 == 'Read':
		start = time.time()
		solu2()
		tsec = time.time() - start
		latency = (tsec*1000)/(filesize*bs*1024)
		print "Latency = %.4f ms" %(tsec*1000/bs) 
		#print loopcounter
		speed = (bs*filesize)/tsec
		speed /= 1000
		print "Disk reading speed : %.3f MBytes/sec" % speed	
	
	else:
		print "You are looking for Some other thing..."
	
	
	#os.remove('WriteFile.txt')
	#print "Completed..."

