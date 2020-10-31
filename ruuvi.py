from ruuvitag_sensor.ruuvi_rx import RuuviTagReactive
import requests
from datetime import datetime


host = 'localhost'

params = {'db': 'temperatures'}

def send_data(data):
  mac = data[0]
  items = data[1]
  temperature = items['temperature']
  humidity = items['humidity']
  pressure = items['pressure']
  data='ruuvi,mac={} temperature={},humidity={},pressure={}'.format(mac, temperature, humidity, pressure)
  r = requests.post('http://{}:8086/write'.format(host), params=params, data=data)
  print('{} {} - {}'.format(datetime.now(), r.status_code, mac))

print('Starting RuuviChip')

ruuvi_rx = RuuviTagReactive()

ruuvi_rx.get_subject().\
  group_by(lambda x: x[0]).\
  subscribe(lambda x: x.sample(15000).subscribe(send_data))
