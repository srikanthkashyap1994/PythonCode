myf = open("psa.txt")
lst = list()
for line in myf:
    lst.append(line.strip())
print lst
myf.close()

import socket
for ip in lst:
    mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        mysock.connect((ip,8082))
        mysock.send('GET /PSA_REQUEST/?action=isPSAAlive HTTP/1.1\n\n')
        while True:
            data = mysock.recv(512)
            if((len(data)) < 1):
                break
            print data
        mysock.close()
    except:
        print "Could not connect to",ip
        continue

socket.create_connection(address,timeout,source_address)
socket.socket(family,type,protocol)
