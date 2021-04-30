


from time import sleep
import json
from kafka import KafkaProducer
import random
from datetime import datetime

producer = KafkaProducer(bootstrap_servers=['localhost'], value_serializer=lambda x:json.dumps(x).encode('utf-8'))
print("producer ready.")

while True:
    data = dict()
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    sensor = 'LDR'
    reading =  random.randint(0,80)
    data['time'] = now
    data['sensor'] = sensor
    data['reading'] = reading
    producer.send(topic='iot', value=data)
    print(data)
    sleep(1)