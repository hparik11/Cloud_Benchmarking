import time, os, sys
import random
#from sys import argv

#script, input1, input2, input3, input4 = argv

def writetofileseq(filename,mysizeKB):
	
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

def filetoreadseq(filename):
	
	f = open(filename, 'rb')
	f.read()
	f.close()

def diskwritespeed(dirname):
	
	maxtime = 0.5 		# in sec
	filename = os.path.join(dirname,'WriteFile.txt')
	start = time.time()
	loopcounter = 0
	while True:
		try:
			writetofileran(filename, filesize)
		except:
			raise	
		
		loopcounter += 1
		diff = time.time() - start
		
		if diff > maxtime:
			break
	#print loopcounter
	return (loopcounter*filesize)/diff

def diskreadspeed(dirname):

	maxtime = 0.5 		# in sec
	filename = os.path.join(dirname,'WriteFile.txt')
	start = time.time()
	loopcounter = 0
	while True:
		try:
			filetoreadseq(filename)
		except:
			raise	
		
		loopcounter += 1
		diff = time.time() - start
		
		if diff > maxtime:
			break

	#print loopcounter
	
	return (loopcounter*filesize)/diff


def writetofileran(filename,mysizeKB):
	
	mychar = 'h'
	writeloops = int(1024*mysizeKB/len(mychar))
	try:
		f = open(filename, 'w')
	except:
		raise
	a = random.randint(0,mysizeKB*1000)
	f.seek(0)
	
	for x in range(0, a):
		f.write(mychar)
	
	f.seek(a)	
		
	for i in range(a,writeloops):
		f.write('a')

	f.close()




	


if __name__ == "__main__":
	

	'''if input3 == '1b':
		filesize = 0.001   #size in kb
	elif input3 == '1kb':
		filesize = 1
	elif input3 == '1mb':
		filesize = 1024
	else:
		print "Please Give Input Properly..."  '''
	
	dirname = os.getcwd()    # Using current working directory
	filesize = 1024*1024


	#if input1 == 'Write':
	speed = diskwritespeed(dirname)
	speed /= 1000
	print "Disk writing speed in random access: %.3f Mbytes per second" % speed
	
	
	#elif input1 == 'Read':
	speed1 = diskreadspeed(dirname)
	speed1 /= 1000
	print "Disk reading speed: %.3f Mbytes per second" % speed1
	
	#else:
	#print "You are looking for Some other thing..."
	
	
	#os.remove('WriteFile.txt')
	#print "Completed..."



