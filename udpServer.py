import socket

def main():
        host = '127.0.0.2'
        port = 5000

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind((host,port))
	print "Server Started"

        while True:
                data, addr = s.recvfrom(1024)
		print "Connection from : " +  str(addr)
                if not data:
                        break
                print "From connected user "+ str(data)
                data = str(data).upper()
 		print "Sending :" +str(data)
		s.sendto(data,addr)
	s.close()

if __name__ == '__main__':
	main()

