from sys import argv

script, input1, input2 = argv
from time import sleep
from random import random
import sys
from threading import Thread, Lock, Semaphore
import threading
from timeit import Timer
import time


def IOPS(m):
    a = 10; b = 20; c = 15; d = 12 
    mutex.acquire() 
    for i in range(ITERATIONS/m):
        #a = 10; b = 20; c = 15; d = 12 
        a+=b
        a/=3
        c-=d
        """b*=c
        d+=8
        a-=2"""
        #print a, b, c, d
    mutex.release()    

def FLOPS(m):
    a = 10.2; b = 20.5; c = 15.4; d = 12.8
    mutex.acquire()    
    for i in range(ITERATIONS/m):
        
        a+=b
        a/=3
        c-=d
    mutex.release() 

def solu1():
    
    for i in range(thread):
        t = Thread(target=IOPS,args=(thread,))
        t.start()
    
    for i in range(thread):
        t.join()
    
    #print "IOPS completed"
    
def solu2():
    
    for i in range(thread):
        t = Thread(target=FLOPS,args=(thread,))
        t.start()
    
    for i in range(thread):
        t.join()
    
    #print "FLOPS completed"
    
if __name__ == '__main__':
    
    ITERATIONS = 100000
    thread = int(input2)
    #thread = int(raw_input("Enter number of Thread: "))
    Dtype = input1
    mutex = Lock()
    #Dtype = 'flops'
    
    if Dtype == 'iops':
	
	#start = time.clock
    	t1 = Timer(solu1)
	
    	print ("IOPS Time Elapsed: {:0.4f}s ".format(t1. timeit(100)/100))
	#tsec = t1.timeit(100)/100
        #print tsec	
    	#cpu_time = tsec / time.clock()
    	#print "Cpu Time: %f" %cpu_time
    	#print ("\nTime: %f ms\n",cpu_time)
    	#Iops= (ITERATIONS)/(cpu_time)
    	#print Iops
    	#gIops=Iops/(10**9)
    	#print "GIOPS : %f" %gIops
    
    elif Dtype == 'flops':
    
    	t2 = Timer(solu2)
    	print("FLOPS Time Elapsed: {:0.4f}s ".format(t2. timeit(100)/100))
	#tsec = t2.timeit(100)/100
        #print tsec	
    	#cpu_time = tsec / time.clock()
    	#print "Cpu Time: %f" %cpu_time
    	#print ("\nTime: %f ms\n",cpu_time)
    	#flops= (ITERATIONS)/(cpu_time)
    	#print flops
    	#gflops=flops/(10**9)
    	#print "GFLOPS : %f" %gflops
    
    
    


    
    
