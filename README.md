# pi-temperature-sensor
Raspberry Pi Temperature Sensor and Graphing (maybe alerting too)

Grafana code started from here https://grafana.com/blog/2023/10/23/monitor-temperature-and-humidity-with-grafana-and-raspberry-pi/

Adapted DHT20 Sensor data gathering from here https://github.com/DFRobot/DFRobot_DHT20/tree/master/python/raspberrypi

Notes:
  Needed to modify sensor-flask.service file:
    sudo nano /etc/systemd/system/sensor-flask.service
    add
    WorkingDirectory=/home/pi/temperature-grafana
    User=pi

  Installed grafana for arm6 raspberry pi from here (2nd section from top) https://grafana.com/grafana/download/9.3.6?edition=enterprise&platform=arm
