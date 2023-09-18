from board import SCL, SDA
import busio
import time
import gc

# Import the SSD1306 module.
import adafruit_ssd1306

# Create the I2C interface.
i2c = busio.I2C(SCL, SDA)
gc.collect()

display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

def findData():
    global startIpAddr, endIpAddr, startDNSAddr, endDNSAddr, startGatewayAddr, endGatewayAddr
    try:
        startIpAddr = data.index(".ADDRESS>")
    except:
        startIpAddr = 0

    try:
        endIpAddr = data.index("</IP4-SETTINGS.ADDR")
    except:
        endIpAddr = 0

    try:
        startGatewayAddr = data.index(".GATEWAY>")
    except:
        startGatewayAddr = 0

    try:
        endGatewayAddr = data.index("</IP4-SETTINGS.GATE")
    except:
        endGatewayAddr = 0

    try:
        startDNSAddr = data.index("1.DNS>")
    except:
        startDNSAddr = 0

    try:
        endDNSAddr = data.index("</IP4-DNS1")
    except:
        endDNSAddr = 0


# clear the display
display.fill(0)
display.show()

# main script
while True:
    # look for file - if not found show error
    try:
        fp = open("get_ip.xml", "r")
        data = fp.read()
        try:
            startGenState = data.index("disconnected")
        except ValueError:
            # if connected
            startGenState = data.index("connected")
            display.text(str(data[startGenState: startGenState+9]), 1, 1, 1, size=1)
            display.show()
            findData()
            display.text("ipAddr:" + str(data[startIpAddr+9: endIpAddr]), 1, 16, 1, size=1)
            display.line(1, 28, 127, 28, 1)
            display.text("DNS1:"+str(data[startDNSAddr+6:endDNSAddr]), 1, 32, 1, size=1)
            display.line(1, 44, 127, 44, 1)
            display.text("Gateway:"+str(data[startGatewayAddr+9:endGatewayAddr]), 1, 48, 1, size=1)
            display.show()
            gc.collect()
        else:
            # if disconneced
            display.text(str(data[startGenState: startGenState+12]), 1, 1, 1, size=1)
            display.show()
            gc.collect()
    except OSError:
        display.text("File not found", 1, 1, 1, size=1)
        display.show()
        gc.collect()
    time.sleep(30)
    display.fill(0)
    display.show()
