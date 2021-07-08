## deadman.py 

On the client:

At startup, the deadman program sends a UDP broadcast lookng for the watchdog server.  The response is a UDP packet with the host name directed to the querying computer.  The deadman client then queries that host for the port number the deadman should use.

The deadman program runs on a client computer to:
   1. Signals the attending Uninterruptible Power Supply (UPS) that it is up and going, avoiding an UPS controlled reboot.
   2. Makes a TCP connection to its listening watchdog, for status display in Home Assistant.
 
