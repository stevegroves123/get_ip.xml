# get_ip.xml
CircuitPython script to read and display IP and MAC address

There are two versions, one for a 128x64 oled and one for a 128x32 oled.

The idea behind this project is a device that I plug into a medical device that is driven by a Linux operationg system.
it will read the ip address and the MAC address of the device so we know which vlan it is on.

My colleagues used a memory stick with a blank file titled Get_ip.xml.  They would reboot the medical device and then wait for it to reconnect to the network. The device would see the file and populate it with various network information including the ip and MAC addresses. They wouldthen plug this into a laptop and read off the information they needed.  I felt this was too slow aand cumberson so set about creating a "memory stick" sized device that would show the various details.


