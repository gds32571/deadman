dmversion = "1.4"

myTimeout=0

import socket

def getport(serverHost,myHost):
    global myTimeout
    global dmversion
    
    print("deadman version:" + dmversion)
    print(myHost)

    print("Asking which port")


    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#    host = 'ha32163'
    host=serverHost
    port = 2999

    try:
       s.settimeout(5.0)
       s.connect((host, port))

       # Receive no more than 1024 bytes
       s.sendall(b'host' + myHost)
       msg = s.recv(1024)
       s.close()

#       pdb.set_trace()

       print(msg.decode('ascii')) 
       myPort=int(msg.decode('ascii')[6:])

       print("Using port: " + str(myPort)) 
       
       return myPort

    except:
          myTimeout += 1
          print('couldnt connect getport' + str(myTimeout) )

