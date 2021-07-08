
from socket import *
#import pdb

myHost=gethostname()

global myTimeout
myTimeout = 0

def getserverhost():
    s=socket(AF_INET, SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

    print('Asking which server')

    s.sendto(b'whichserver',('192.168.2.255',12345))
    s.close()


    s=socket(AF_INET, SOCK_DGRAM)
    s.bind(('',12345))

    print('Getting answer')

    m=s.recvfrom(4096)
 
#    pdb.set_trace()
#    print('len(m)='+str(len(m)))
#    print('len(m[0])='+str(len(m[0])))
#    print(m[0])

    serverHost = m[0].decode('ascii')
    print('Server Host= ' + (serverHost))

#    print('len(m[1])='+str(len(m[1])))
#    print(m[1])

    return serverHost

  