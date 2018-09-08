from ruuvitag_sensor.ruuvitag import RuuviTag
import requests
from datetime import datetime

ruuvi1 = RuuviTag('CC:91:7E:B0:AA:8B')
ruuvi2 = RuuviTag('EC:B7:CB:36:88:76')
ruuvi3 = RuuviTag('EC:E0:0A:AC:90:3E')

# InfluxDB host
host = '10.0.0.20'

ruuvis = [ruuvi1, ruuvi2, ruuvi3]
params = {'db': 'temperatures'}

def send_data(mac, items):
  temperature = items['temperature']
  humidity = items['humidity']
  pressure = items['pressure']
  data='ruuvi,address=Kilonportti,mac={} temperature={},humidity={},pressure={}'.format(mac, temperature, humidity, pressure)
  r = requests.post('http://{}:8086/write'.format(host), params=params, data=data)
  print('{} {} - {} - {}'.format(datetime.now(), r.status_code, mac, temperature))


for ruuvi in ruuvis:
  ruuvi.update()
  mac = ruuvi.mac
  send_data(mac, ruuvi.state)