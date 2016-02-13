
import socket

def main():
	host = '127.0.0.1'
    	port = 5001
	
	s1 = socket.socket()
	s1.bind((host,port))
	
	s1.listen(1)
	c1, addr1 = s1.accept()
	print "Connection from : " +  str(addr1)
	
	f = open('fill.bin','wb')
	while True:
		
		data = c1.recv(512)
		if not data:
			break
		
		f.write(data)
		c1.send("File Received...")
	f.close()
	c1.close()

if __name__ == '__main__':
	#thread = int(raw_input("Enter the number of thread: "))
	main()

