import machine, ssd1306
import network

i2c = machine.I2C(scl=machine.Pin(4), sda=machine.Pin(5))
oled = ssd1306.SSD1306_I2C(128,64, i2c)


sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
    print('connecting to network...')
    sta_if.active(True)
    sta_if.connect('', '')
    while not sta_if.isconnected():
        pass
    print(sta_if.ifconfig())   
    print(sta_if.scan())

import sys, io, urequests2
from time import time
import re
def speed_test():
    resp = urequests2.get('https://api.fast.com/netflix/speedtest?https=%s&token=REPALCE_ME&urlCount=%s' % ('true',5))
    urls = [i['url'] for i in resp.json()]

    for url in urls:
        start = time()
        r = urequests2.get(url, stream=True)
        dl = 0
        iterator = r.iter_content(128)
        for chunk in iterator:
            dl += 1
            next(iterator)
            sys.stdout.write("\r%s Mbps" % ((128*dl)//(time() - start) / 100000))
            oled.fill(0)
            oled.text('MicroPython', 10, 10)
            oled.text(sta_if.ifconfig()[0], 10, 30)
            oled.text("%s Mbps" % ((128*dl)//(time() - start) / 100000), 10, 50)
            oled.show()
            break
speed_test()
