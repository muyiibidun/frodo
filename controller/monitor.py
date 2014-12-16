import time
import socket
import sys

class Monitor:
	def __init__(self,ip,port,duration,connectionType):
		self.ip = ip
		self.port = port 
		self.duration = duration 
		self.connectionType = connectionType
		 
	def connectTCP(self):
		self.connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		try:
        		self.connection.bind((self.ip, self.port)) # Bind to the port
        		self.connection.listen(10)  # Now wait for client (max of 10) connections.
        		print "Server %s is listening on %d"%(self.ip,self.port)
    		except socket.error, e:
        		print "Connection failed: %s"%e
       	 		sys.exit()
	def startTCP(self):
		self.connectTCP()
		now = time.time()
		end = now + self.duration + 30 #add a 30s lag just in case 			
		try:   
			while(time.time() <= end):
           			connection, remoteAddr = self.connection.accept() # Establish connection with client.
        			print 'Got connection from', addr
           			#c.send('Thank you for connecting')
    		except socket.error, e:
        		print "An error occured: %s"%e
        		sys.exit()
    		finally:
        		connection.close() # Close the connection
		#THIS CODE IS INCOMPLETE
	def startUDPConnection(self):
		try:
			self.connection = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		except socket.error, msg:
			print "Error creating a connection: %s" % msg
			sys.exit()
		
		try:
                        self.connection.bind((self.ip, self.port)) # Bind to the port
                        print "Server %s is listening on %d"%(self.ip,self.port)
                except socket.error, e:
                        print "Connection failed: %s"%e
                        sys.exit()
		
		now = time.time()
                end = now + self.duration #add a 30s lag just in case                      
                while(time.time() <= end):
			stream  = self.connection.recvfrom(1024)
			msg = stream[0]
    	        	remote_addr = stream[1]
			print "Received data: '%s' from '%s'"%(msg,remote_addr)
		
		self.connection.close() 

