#SENSE and PUB program to read DHT11 sensed data as temperature and humidity level and publish to google IOT
#author santmishra

# Import necessary Modules
import os
import json
from google.cloud import pubsub_v1
import board
import adafruit_dht
import time

# Initial the dht device, with data pin  connected to:(In our example raspberry pin 4 is connected to data of DHT11)
dhtDevice = adafruit_dht.DHT11(board.D4,use_pulseio=False )
# Define topic path
topic_path = 'projects/{project_id}/topics/{topic}'.format(
    project_id=os.getenv('PROJECT_ID'), topic=os.getenv('TOPIC_NAME'))

while True:
    try:
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        print(
            "Sensor Temp: {:.1f} F / {:.1f} C    Sensor Humidity: {}% ".format(
                temperature_f, temperature_c, humidity
            )
        )

         # topic message
        data = {}
        data['timestamp'] = int(time.time())
        data['temperature'] = temperature_f
        data['humidity'] = humidity
        msg_json_data = json.dumps(data)

        # Publish the payload to the cloud
        publisher = pubsub_v1.PublisherClient()
        publisher.publish(topic_path, data=msg_json_data.encode('utf-8'))

        print("Publishing the message : " + msg_json_data)

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
    except KeyboardInterrupt as error:
        dhtDevice.exit()
        raise error
    time.sleep(2.0)