# get_ip.xml
CircuitPython script to read and display IP and MAC address

There are two versions, one for a 128x64 oled and one for a 128x32 oled.

The idea behind this project is a device that I plug into a medical device, driven by a Linux operating system.
it will read the ip address and the MAC address of the device so we know which vlan it is on.

My colleagues used a memory stick with a blank file titled Get_ip.xml.  They would reboot the medical device and then wait for it to reconnect to the network. The device would see the file and populate it with various network information including the ip and MAC addresses. They would then plug this into a laptop and read off the information they needed.  I felt this was too slow and cumbersome so set about creating a "memory stick" sized device that would show the various details.

I have various Seeeed Xiao Sam51 and RPi2040 devices and decided these should be used due to their very small footprint and their incredible power.  I also had various cheap 128x64 OLED displays laying around the workshop.  My initial prototype was created usung a micro-board inside a mint tin, this restricted the size and gave a good deal of protection while in use.

The project hinged on creating a device that appeared to be a memory stick. Reviewing the various operating systems that fit on these microcontrollers the Adafruit CircuitPython appeared to be the easiest to us and it gave me an excuse to have a play with it.
While testing the first iteration it became apparent I needed to increase the complexity of the code to take into account the various errors that could occur.

I'm not a coder / programmer, just an old guy who likes to play with microcontrollers and a desire to build, so please forgive the randomness of the code. If you feel you could do something with it then please feel free to copy and improve, I'm not precious about whatI create, I do it for fun.

The prototype worked well and did exactly what we wanted it to to; however, I started thinking about a more robust verson that was smaller and only displayed the information we needed, ip and MAC addresses.  I reduced the display to a 128x32 OLED and encased it all in an old memory stick; I want to change it by adding a usb connector to directly plug into the medical device rather than using a lead.

