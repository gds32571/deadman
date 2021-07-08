## deadman 

On the client:

   At startup, the deadman program sends a UDP broadcast looking for the watchdog server.
The response is a UDP packet with the host name directed to the querying computer.  The 
deadman client then queries that host for the port number the deadman should use.

The deadman program runs on a client computer to:
   1. Signals the attending Uninterruptible Power Supply (UPS) that it is up and going, avoiding an UPS controlled reboot.
   2. Makes a TCP connection to its listening watchdog, for status display in Home Assistant.
 
### dm.sh 

   This script runs the deadman python program.  It restarts it when it crashes and stores the return code
   in a log file and also counts those restarts.

### deadman.py

   The main program.  It has two functions:

      1. It toggles a GPIO signal connected to the UPS that supports it. This lets the UPS know that the computer is still running.
      2. It makes a connection to the watchdog instance running on the watchdog server computer. That program sends an MQTT message 
      to the Home Assistant so it can show the client computer is still running. 

### getwd.py

   This program uses a UDP broadcast to identify the host computer running the watchdog.

### getport.py

   This program uses a UDP packet to find the port it is supposed to use.  This port number is mapped by the watchdog to a MQTT message that identifies the client host or application. 

### updateall

   The RPi computer rp5 holds the master copy of these programs.  After making a change to one of them, this script is used to copy the deadman files to all of the lcient computers.  It also restarts the deadman program so that it runs the latest copy. 

### deadmanrestart

   The script used to kill the deadman program so that dm.sh can restart it using the new image copy.
   
