from sys import argv

script, input1, input2 = argv
from time import sleep
from random import random
import sys
import multiprocessing
from timeit import Timer
import time



## This IOPS Function does arithmetic Integer operation ##

def IOPS(m):
    a = 10; b = 20; c = 15; d = 12 
    
    for i in range(ITERATIONS/m):

        a+=b
        b/=4
        c-=d
	#d*=3
	
## This FLOPS Function does arithmetic FLoating operations ##       	

def FLOPS(m):
    a = 10.2; b = 20.5; c = 15.4; d = 12.8
        
    for i in range(ITERATIONS/m):
        
        a+=b
        a/=3
	c-=d
    	#b*=4
        

## This function creates and starts the thread IOPS. and joins all threads for completion.   ##

def solu1():
    jobs = []
    for i in range(thread):
        p = multiprocessing.Process(target=IOPS,args=(thread,))
        jobs.append(p)
        p.start()
    
    for i in range(len(jobs)):
        p.join()
    
    #print "IOPS completed"
    
def solu2():
    jobs = []
    for i in range(thread):
        p = multiprocessing.Process(target=FLOPS,args=(thread,))
        jobs.append(p)
        p.start()
    
    
    for i in range(len(jobs)):
        p.join()
    
    #print "FLOPS completed"
    

## Main Method ##

if __name__ == '__main__':
    
    ITERATIONS = 10000000                        	## Number of Iterations 
    
    thread = int(input2)				## Number of threads a user enters as argument. 
    
    Dtype = input1
    
    
    if Dtype == 'iops':				
	
    	start = time.time()				## Start of timer. 
	solu1()						## The function of which we want to find the elapsed time. 
	tsec = time.time() - start
	print "IOPS Time Elapsed: %.3f s " %tsec        ## Total time elapsed for completion of IOPS. 
	
       
    	
    	Iops= (ITERATIONS*1000)/(tsec)			
    	#print Iops
    	gIops=Iops/(10**9)				## To get GIOPS, divide by 10^9. 
    	print "GIOPS : %f" %gIops
    
    elif Dtype == 'flops':
    
    	start = time.time()
	solu2()
	tsec = time.time() - start
	print "FLOPS Time Elapsed: %.3f s " %tsec	
       
    	
    	flops= (ITERATIONS*1000)/(tsec)
    	#print flops
    	gflops=flops/(10**9)
    	print "GFLOPS : %f" %gflops

