import ssd1306
import picoweb
import machine

app = picoweb.WebApp(__name__)

@app.route("/")
def index(req, resp):
    yield from picoweb.start_response(resp)
    yield from resp.awrite("Hello world from picoweb running on the ESP32")
    i2c = machine.I2C(scl=machine.Pin(4), sda=machine.Pin(5))
    oled = ssd1306.SSD1306_I2C(128, 64, i2c)
    oled.fill(0)
    oled.text("picoweb started...", 0, 0)
    oled.text("root site accessed...", 0, 10)
    oled.show()

@app.route("/button/")
def button(req, resp):
    yield from picoweb.start_response(resp)
    yield from resp.awrite("Hello world this is a button")
    i2c = machine.I2C(scl=machine.Pin(4), sda=machine.Pin(5))
    oled = ssd1306.SSD1306_I2C(128, 64, i2c)
    oled.fill(0)
    oled.text("picoweb started...", 0, 0)
    oled.text("button accessed...", 0, 10)
    oled.show()

app.run(debug=True, host = "0.0.0.0")
