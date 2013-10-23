import SocketServer
import md5
 
class MyTCPHandler(SocketServer.StreamRequestHandler):
    """
    The RequestHandler class for our server.
 
    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
 
    def handle(self):
		# self.request is the TCP socket connected to the client
		self.data = self.rfile.readline().strip()
		print 'command: ' + self.data.split(' ')[0] #command
		print 'login: ' + self.data.split(' ')[1] #login
		print 'pass: ' + self.data.split(' ')[2] #pass
			
		# send if log in is successful
		
		if self.data.split(' ')[0] == 'LOGIN':
			if self.data.split(' ')[2] == md5.new('pass').digest():
				self.request.sendall('OK')
				self.request.sendall('There is no secret message.')
			else:
				self.request.sendall('ANS')
		elif self.data.split(' ')[0] == 'SIGNUP':
			self.request.sendall('REGOK') #todo
		
        
        		
 
if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
 
    # Create the server, binding to localhost on port 9999
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
 
    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()