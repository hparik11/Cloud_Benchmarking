from sys import argv

script, input1 = argv
from time import sleep
from random import random
import sys
import multiprocessing
#from threading import Thread
#import threading
from timeit import Timer
import time


def IOPS(m):
    a = 10; b = 20; c = 15; d = 12 
    
    for i in range(ITERATIONS/m):

        a+=b
        b/=4
        c-=d
	d+=3
	d-=8
	c+=5
	a+=67
	
def FLOPS(m):
    a = 10.2; b = 20.5; c = 15.4; d = 12.8
        
    for i in range(ITERATIONS/m):
        
        a+=b
        a/=3
	c-=d
	d*=4

     	
def solu1():
    jobs = []
    for i in range(thread):
        p = multiprocessing.Process(target=IOPS,args=(thread,))
        jobs.append(p)
        p.start()
    
    for i in range(len(jobs)):
        p.join()

def solu2():
    jobs = []
    for i in range(thread):
        p = multiprocessing.Process(target=FLOPS,args=(thread,))
        jobs.append(p)
        p.start()
    
    
    for i in range(len(jobs)):
        p.join()

if __name__ == '__main__':
    
    ITERATIONS = 10000000
    #thread = int(input2)
    thread = 4
    #Dtype = input1
    #mutex = Lock()
    Dtype = input1
    samp_iops = []
    samp_flops = []

    if Dtype == 'iops':
	
    	start = time.time()
	solu1()
	tsec = time.time() - start
	#print "IOPS Time Elapsed: %.3f s " %tsec
	
        #print tsec	
    	#cpu_time = tsec / time.clock()
    	#print "Cpu Time: %f s" %cpu_time
    	
    	Iops= (ITERATIONS*1000)/(tsec)
    	#print Iops
    	#gIops=Iops/(10**9)
	samp_iops.append(Iops)
    	print samp_iops

    elif Dtype == 'flops':

	start = time.time()
	solu2()
	tsec = time.time() - start
	#print "FLOPS Time Elapsed: %.3f s " %tsec
        #print tsec	
    	#cpu_time = tsec / time.clock()
    	#print "Cpu Time: %f s" %cpu_time
    	
    	flops= (ITERATIONS*1000)/(tsec)
    	#print flops
    	#gflops=flops/(10**9)
    	samp_flops.append(flops)
    	print samp_flops

