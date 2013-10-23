import socket
import sys
import md5

LOGIN = ""
PASSWORD = ""
HOST, PORT = "localhost", 9999
message = ''

def menu():
	print '-----------------------------'
	print 'Choose what you want:'
	print '1) Log in'
	print '2) Sign up'
	print '3) Forgot password?'
	
	choose = raw_input()
	
	if choose == '1':
		log('LOGIN')
	elif choose == '2':
		log('SIGNUP')
	elif choose == '3':
		oooohno()
	else:
		menu()
	return
	
def send(command, login, password):
	global message
	m = md5.new()
	m.update(password)
	pass_md5 = m.digest()
	
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect((HOST, PORT))
		sock.sendall(command + ' ' + login + ' ' + pass_md5 + '\n')
		
		# Receive data from the server and shut down
		received = sock.recv(1024)
		
		if received == 'OK':
			message = sock.recv(1024)
	finally:
		sock.close()
	
	return received
	
	
def log(command):
	while 1:
		global message
		print '---------'
		print 'Login:'
		login = raw_input()
		print 'Password:'
		password = raw_input()
		
		response = send(command, login, password)
		if response == 'OK':
			print 'YES!'
			print 'Secret message is: ' + message
			break
		elif response == 'REGOK':
			print "Registered!"
			break
		elif response == 'ANS':
			print 'Wrong password. Try again.'
		elif response == 'CON':
			print "Can't connect to server."
		else:
			print 'Unknown error.'
	return
		
def oooohno():
	print 'Oh no!'
	menu()
	return

if __name__ == "__main__":
	print 'Welcome!'
	menu()
