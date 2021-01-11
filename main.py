import machine, ssd1306
import network

i2c = machine.I2C(scl=machine.Pin(4), sda=machine.Pin(5))


sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
    print('connecting to network...')
    sta_if.active(True)
    sta_if.connect('REPLACE_ME', 'REPLACE_ME')
    while not sta_if.isconnected():
        pass
    print(sta_if.ifconfig())    
oled = ssd1306.SSD1306_I2C(128,64, i2c)
oled.fill(0)
oled.text('MicroPython', 10, 10)
oled.text(sta_if.ifconfig()[0], 10, 30)
oled.show()
