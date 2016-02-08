import time, os, sys
import random
from sys import argv

script, input1, input2, input3, input4 = argv

def WriteToFileSeq(filename,mysizeKB):
	
	mystring = "Hi This is Harsh Parikh."
	writeloops = int(1024*mysizeKB/len(mystring))
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
	writeloops = int(1024*mysizeKB/len(mychar))
	try:
		f = open(filename, 'wb')
	except:
		raise
	a = random.randint(0,mysizeKB*1000)
	
	
	f.seek(a)	
		
	for i in range(a,writeloops):
		f.write('P')
	
	f.seek(0)
	
	for x in range(0, a):
		f.write(mychar)

	f.close()

def FileToReadRnd(filename):
	
	f = open(filename, 'rb')
	a = random.randint(0,filesize*1000)
	f.seek(a)
	f.read()
	f.seek(0)
	f.read(a)
	f.read()
	f.close()


def DiskWriteSpeed(dirname,access):
	
	maxtime = 0.5 		# in sec
	filename = os.path.join(dirname,'WriteFile.txt')
	start = time.time()
	loopcounter = 0
	while True:
		try:
			if access == 'rnd':
				WriteToFileRnd(filename, filesize)
			else:
				WriteToFileSeq(filename, filesize)
		except:
			raise	
		
		loopcounter += 1
		diff = time.time() - start
		
		if diff > maxtime:
			break
	#print loopcounter
	return (loopcounter*filesize)/diff

def DiskReadSpeed(dirname,access):

	maxtime = 0.5 		# in sec
	filename = os.path.join(dirname,'WriteFile.txt')
	start = time.time()
	loopcounter = 0
	while True:
		try:
			if access == 'rnd':
				FileToReadRnd(filename)
			else:
				FileToReadSeq(filename)
		except:
			raise	
		
		loopcounter += 1
		diff = time.time() - start
		
		if diff > maxtime:
			break

	#print loopcounter
	
	return (loopcounter*filesize)/diff





if __name__ == "__main__":
	

	if input3 == '1b':
		filesize = 0.001   #size in kb
	elif input3 == '1kb':
		filesize = 1
	elif input3 == '1mb':
		filesize = 1024
	else:
		print "Please Give Input Properly..."  
	
	dirname = os.getcwd()    # Using current working directory
	#filesize = 0.001
	access = input2


	if input1 == 'Write':
		speed = DiskWriteSpeed(dirname,access)
		speed /= 1000
		print "Disk writing speed : %.3f Mbytes per second" % speed
	
	
	elif input1 == 'Read':
		speed1 = DiskReadSpeed(dirname,access)
		speed1 /= 1000
		print "Disk reading speed : %.3f Mbytes per second" % speed1
	
	else:
		print "You are looking for Some other thing..."
	
	
	#os.remove('WriteFile.txt')
	#print "Completed..."



