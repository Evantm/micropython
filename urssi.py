import machine, ssd1306
import network

i2c = machine.I2C(scl=machine.Pin(4), sda=machine.Pin(5))
oled = ssd1306.SSD1306_I2C(128,64, i2c)

while True:
	sta_if = network.WLAN(network.STA_IF)
	sta_if.disconnect()
	t = [result[0].decode('utf8')[:10] + ' ' + str(result[3]) for result in sta_if.scan()]
	oled.fill(0)
	for i in range(6):
		oled.text(t[i],0,i*10)
	oled.show()