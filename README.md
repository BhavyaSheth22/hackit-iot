# Hackit-IOT
## Problem statement: Data Relay using MQTT Protocol

This project involves 50 bots pushing different data streams at a frequency of 500 ms (using multithreading), and a system which accepts this data and can segregate the data into different containers of the database.
Meanwhile, every five minutes, the system compresses the entire dataset and relays it to a cloud infrastructure without any loss of data.
If internet connection fails, the dataset is stored locally, and pushed to the cloud when internet connection is restored.

## Contents
* MQTT communication and Data Segregation
* Data compression

### MQTT Communication and Data Segregation
#### Publishers:
  Using multithreading, 50 bots publish messages at 0.5s intervals, to a single topic that is subscribed to by a central computer. The messages are in the form of JSON strings. For example,
  ```
  msg = {
            'id': deviceID,
            'timestamp': datetime.now().timestamp(),
            'temp': temp,
            'humidity': humidity,
            'air_pressure': air_pressure,
            'ph': ph
        }
  ```
      
  This project uses the Mosquitto MQTT broker and the Paho MQTT client in python.
  
#### Subscriber:
  A central computer subscribes to the single topic and segregates the incoming data by device by appending data corresponding to a particular device and the physical quantity to a text file. Messages from different devices are recognized by the 'id' key of the messages received with the data itself.
  
 ### Data compression:
  
  
