import socket
import sys


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #protocols for socket
except socket.error:
    print 'Socket can not run'
    sys.exit()
print 'Socket is run'

host = 'www.google.com';
port = 80;

try:
    remote_ip = socket.gethostbyname( host )
except socket.gaierror:

    print 'Hostname could not be resolved. Exiting'
    sys.exit()


s.connect((remote_ip , port)) #connect to www.google.com:80
print 'Socket Connected to ' + host + ' on ip ' + remote_ip


message = "GET / HTTP/1.1\r\n\r\n" #standart data for sending
try :

    s.sendall(message) #sending data message
except socket.error:

    print 'Send failed'
    sys.exit()

print 'Message send successfully'

reply = s.recv(4096)
print reply
