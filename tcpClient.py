import socket
import sys
import time

def main():
	
	host = '127.0.0.1'
	port = 5000
	
	s = socket.socket()
	s.connect((host,port))
	
	#msg = raw_input("Enter the String->\n")
	
	start = time.time()
	for i in range(100):
		f = open('1b_file','rb')
		l = f.read(512)
		while l :
			s.send(l)
			l = f.read(512)
			data = s.recv(1024)
			print "Received from Server..... "
		f.close()
		
	end = time.time()
	t = (end-start)*1000
	print "Elapsed Time for TCP is : %.3f ms" %t
	throughput = 0.001*1024*1000*100/(t*10**6)
	print "Through put is : %.3f Mega Bytes/Sec.." %throughput
	s.close()

if __name__ == '__main__':
        
	main()
