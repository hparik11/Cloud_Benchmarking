from sys import argv

script, input1 = argv
from time import sleep
from random import random
import sys
import multiprocessing

from timeit import Timer
import time


def IOPS(m):
    a = 10; b = 20; c = 15; d = 12 
    
    for i in range(ITERATIONS/m):				## Loop would be Number of iteration/no. of threads.

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
    thread = 4						## Putting thread value as fixed one. 
    
    Dtype = input1
    
    
    if Dtype == 'iops':
	
    	start = time.time()
	solu1()
	tsec = time.time() - start
		
    	Iops= (ITERATIONS*1000)/(tsec)		
    	
    	#gIops=Iops/(10**9)
	
    	print Iops

    elif Dtype == 'flops':

	start = time.time()
	solu2()
	tsec = time.time() - start
	
    	
    	flops= (ITERATIONS*1000)/(tsec)
    	
    	
    	print flops

