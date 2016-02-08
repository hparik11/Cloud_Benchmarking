import socket
import sys
import time

def main():
	
	host = '127.0.0.1'
	port = 5000
	
	s = socket.socket()
	s.connect((host,port))
	
	#msg = raw_input("Enter the String->\n")
	f = open('64kb_file','rb')
	l = f.read(2048)
	
	start = time.time()
	while l :
		#data = str(msg)
		#print sys.getsizeof(data)
	#my_bytes = bytearray()
	#my_bytes.append(123)
	#my_bytes.append(125)
	#print sys.getsizeof(my_bytes)
	#print ''.join('{:02x}'.format(x) for x in my_bytes)
		s.send(l)
		l = f.read(2048)
		data = s.recv(1024)
		print "Received from Server..... "
		
		#print sys.getsizeof(data)
		#msg = raw_input('->')
	end = time.time()
	t = (end-start)*1000
	print "Elapsed Time for TCP is : %.2f ms" %t
	s.close()

if __name__ == '__main__':
        
	main()
