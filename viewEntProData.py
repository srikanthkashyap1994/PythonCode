myf = open("psa_with_cug.txt")
lst = list()
for line in myf:
    lst.append(line.strip())
#print lst
myf.close()


import socket
for ip in lst:
    mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        mysock.connect((ip.split()[0],8082))
        print ip.split()[0]
        url = 'GET /PSA_REQUEST/?action=viewEnterpriseProfileData&isDBUpdateRequired=no&eid=1&cug_id=' + str(ip.split()[1]) + ' HTTP/1.1\n\n'
        mysock.send(url)
        while True:
            data = mysock.recv(512)
            if((len(data)) < 1):
                break
            print data
        mysock.close()
    except:
        print "Could not connect to",ip
        continue
