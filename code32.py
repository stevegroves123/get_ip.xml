# This is the 128x32 OLED version

from board import SCL, SDA
import board, time, neopixel, busio, gc, digitalio

# Import the SSD1306 module.
import adafruit_ssd1306

# Create the I2C interface.
i2c = busio.I2C(SCL, SDA)
gc.collect()

display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)
pixels.brightness = 0.3

def findData():
    global startIpAddr, endIpAddr, startMAC, endMAC
    # IP address
    try:
        startIpAddr = data.index(".ADDRESS>")
    except:
        startIpAddr = 0

    try:
        endIpAddr = data.index("</IP4-SETTINGS.ADDR")
    except:
        endIpAddr = 0

    #  MAC address
    try:
        startMAC = data.index("HWADDR")
    except:
        startMAC = 0

    try:
        endMAC = data.index("</GENERAL.HWADDR>")
    except:
        endMAC = 0

def page1Data():
    display.text("ip:" + str(data[startIpAddr+9: endIpAddr]), 1, 1, 1, size=1)
    display.text("MAC:"+str(data[startMAC+7:endMAC]), 1, 16, 1, size=1)
    display.show()
    time.sleep(10)

# clear the display
display.fill(0)
display.show()

# advert
display.text("Pinnacle Solutions", 1, 1, 1, size = 1)
display.text("Steve Groves 2023", 1, 16, 1, size = 1)
display.show()
time.sleep(2.5)
display.fill(0)
display.show()

# main code
while True:
    # look for file
    try:
        fp = open("Get_ip.xml", "r")
    # if not found show error
    except OSError:
        display.text("File not found", 1, 1, 1, size=1)
        display.show()
        for a in range(0, 5):
            pixels.fill((255, 0, 0))
            time.sleep(0.5)
            pixels.fill((0, 0, 0))
            time.sleep(0.5)
        gc.collect()
    # if found do the following
    else:
        data = fp.read()
        try:
            startGenState = data.index("disconnected")
        except ValueError:
            # if not disconnected then
            try:
                startGenState = data.index("unavailable")
            except ValueError:
                findData()
                page1Data()
		fp.close()
                gc.collect()
            else:
                display.text(str(data[startGenState: startGenState+11]), 1, 1, 1, size=1)
                display.text("unavailable", 1, 1, 1, size=1)
                display.show()
                fp.close()
                gc.collect()
        else:
            # if disconneced
            display.text(str(data[startGenState: startGenState+12]), 1, 1, 1, size=1)
            display.text("disconnected", 1, 1, 1, size=1)
            display.show()
            time.sleep(20)
            fp.close()
            gc.collect()
    display.fill(0)
    display.show()
