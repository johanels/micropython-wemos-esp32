import modules.utils
import modules.picoweb
import machine

led1=Pin(0,Pin.OUT)
led2=Pin(2,Pin.OUT)
led3=Pin(12,Pin.OUT)
led4=Pin(13,Pin.OUT)
led5=Pin(14,Pin.OUT)
led6=Pin(15,Pin.OUT)
led7=Pin(16,Pin.OUT)

app = picoweb.WebApp(__name__)

@app.route("/")
def index(req, resp):
    yield from picoweb.start_response(resp)
    yield from resp.awrite("<html><head></head><body><p>Hello world from picoweb running on the ESP32</p><a href=\"/button1/\">Button 1</a><br><a href=\"/button1/\">Button 2</a><br><a href=\"/button1/\">Button 3</a><br></body></html>")

@app.route("/button1/")
def button(req, resp):
    yield from picoweb.start_response(resp)
    if pin1.value() = 0:
        led1.value(1)
    else:
        led1.value(0)

@app.route("/button2/")
def button(req, resp):
    yield from picoweb.start_response(resp)
    if pin2.value() = 0:
        led2.value(1)
    else:
        led2.value(0)

app.run(debug=True, host = "0.0.0.0")
