import DFRobot_DHT20
import time
from flask import Flask, Response
from prometheus_client import Counter, Gauge, start_http_server, generate_latest

# https://github.com/DFRobot/DFRobot_DHT20
IIC_MODE         = 0x01            # default use IIC1
IIC_ADDRESS      = 0x38           # default i2c device address
'''
   # The first  parameter is to select iic0 or iic1
   # The second parameter is the iic device address
'''
dht20 = DFRobot_DHT20(IIC_MODE ,IIC_ADDRESS)
"""
     @brief Initialize function
"""
dht20.begin()

content_type = str('text/plain; version=0.0.4; charset=utf-8')

def get_temperature_readings():
    temperature = dht20.get_temperature()
    # Convert Celsius to Fahrenheit Formula: (°C * 1.8) + 32 = °F
    temperature = (temperature * 1.8) + 32
    humidity = dht20.get_humidity()
    humidity = format(humidity, ".2f")
    temperature = format(temperature, ".2f")
    if all(v is not None for v in [humidity, temperature]):
        response = {"temperature": temperature, "humidity": humidity}
        return response
    else:
        time.sleep(0.2)
        temperature = dht20.get_temperature()
        humidity = dht20.get_humidity()
        temperature = format(temperature, ".2f")
        response = {"temperature": temperature, "humidity": humidity}
        return response

app = Flask(__name__)

current_humidity = Gauge(
        'current_humidity',
        'the current humidity percentage, this is a gauge as the value can increase or decrease',
        ['room']
)

current_temperature = Gauge(
        'current_temperature',
        'the current temperature in celsius, this is a gauge as the value can increase or decrease',
        ['room']
)

@app.route('/metrics')
def metrics():
    metrics = get_temperature_readings()
    current_humidity.labels('study').set(metrics['humidity'])
    current_temperature.labels('study').set(metrics['temperature'])
    return Response(generate_latest(), mimetype=content_type)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
