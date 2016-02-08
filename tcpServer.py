
import socket

def main():
	host = '127.0.0.1'
    	port = 5000
	
	s1 = socket.socket()
	s1.bind((host,port))
	
	s1.listen(1)
	c1, addr1 = s1.accept()
	print "Connection from : " +  str(addr1)
	
	f = open('fill.bin','wb')
	while True:
		
		data = c1.recv(2048)
		#my_bytes = bytearray(data)
		
		#data = str(data)
		print data
		if not data:
			break
		
		f.write(data)
		#print ''.join('{:02x}'.format(x) for x in my_bytes)
		#print "From connected user  "
		#data = str(data).upper()
		#print "Sending: "+ str(data)
		c1.send("File Received")
	c1.close()

if __name__ == '__main__':
	#thread = int(raw_input("Enter the number of thread: "))
	main()

