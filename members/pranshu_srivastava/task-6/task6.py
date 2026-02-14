#Task 6: Smart Sensor  Classifier
import random
class Sensor:
  def __init__(self,name,low,high):
    self.name=name
    self.low=low
    self.high=high

  def classify(self,value):
    if(value<self.low):
      res = 'low'
    elif(value>self.high):
      res = 'high'
    else:
      res = 'medium'
    print(f"{self.name} Sensor Reading: {value}:{res}")

temp_sensor = Sensor("Temperature", 20, 30)
humidity_sensor = Sensor("Humidity", 40, 60)
light_sensor = Sensor("Light", 100, 200)  

for i in range(3):
  temp_sensor.classify(random.randint(10,40))
  humidity_sensor.classify(random.randint(20,80))
  light_sensor.classify(random.randint(80,220))
