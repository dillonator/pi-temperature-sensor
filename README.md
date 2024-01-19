# pi-temperature-sensor
Raspberry Pi Temperature Sensor and Graphing (maybe alerting too)

Grafana code started from here https://grafana.com/blog/2023/10/23/monitor-temperature-and-humidity-with-grafana-and-raspberry-pi/

Adapted DHT20 Sensor data gathering from here https://github.com/DFRobot/DFRobot_DHT20/tree/master/python/raspberrypi

Notes:
  * Needed to modify sensor-flask.service file:
    * sudo nano /etc/systemd/system/sensor-flask.service
     ```
     [Unit]
     Description=A service that will keep temperature-grafana app running in the background
     After=multi-user.target
     [Service]
     Type=simple
     Restart=always
     WorkingDirectory=/home/pi/temperature-grafana
     User=pi
     ExecStart=/usr/bin/python3 /home/pi/temperature-grafana/app.py
     [Install]
     WantedBy=multi-user.target
     ```
  * Installed grafana for arm6 raspberry pi from here (2nd section from top) https://grafana.com/grafana/download/9.3.6?edition=enterprise&platform=arm - grafana-enterprise-rpi_9.3.6_armhf.deb
  * Need ARM6 prometheus for Raspberry Pi Zero - https://opensource.com/article/21/3/raspberry-pi-grafana-cloud
    ```
    wget https://github.com/prometheus/prometheus/releases/download/v2.24.0/prometheus-2.24.0.linux-armv6.tar.gz
    tar -xvzf prometheus-2.24.0.linux-armv6.tar.gz
    cd ./ prometheus-2.24.0.linux-armv6
    ```
  * create a service, we need to create a new file within the “/etc/systemd/system/” directory.

  This directory is where services are handled by default.
  To create this file, we will be using the nano text editor.
  Begin writing the new service file by running the following command on your Pi.
  ```
  sudo nano /etc/systemd/system/prometheus.service
  ```
  2. Within this file, enter the following text.
  The text defines how the service works and how it should run the Prometheus software.
  ```
  [Unit]
  Description=Prometheus Server
  Documentation=https://prometheus.io/docs/introduction/overview/
  After=network-online.target
  
  [Service]
  User=pi
  Restart=on-failure
  
  ExecStart=/home/pi/prometheus-2.24.0.linux-armv6/prometheus \
    --config.file=/home/pi/prometheus/prometheus.yml \
    --storage.tsdb.path=/home/pi/prometheus/data

  [Install]
  WantedBy=multi-user.target
  ```
