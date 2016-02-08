import socket

def main():
        host = '127.0.0.1'
        port = 5001
	server = ('127.0.0.2',5000)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind((host,port))

        msg = raw_input("Enter the String->\n")
        while msg!= 'q' :
                s.sendto(msg, server)
                data, addr = s.recvfrom(1024)
                print "Received from Server " + str(data)
                msg = raw_input('->')
        s.close()

if __name__ == '__main__':
        main()

