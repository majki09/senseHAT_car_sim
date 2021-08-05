from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.clear()

class Pixel():
  def __init__(self, x, y, color=(255, 255, 255)):
    self.x = x
    self.y = y
    self.color = color
    
class Blinker():
  def __init__(self, x1, y1, x2, y2):
    self.is_blinking = False
    self.color = (255, 50, 0)
    self.lights = [Pixel(x1, y1, self.color),
                   Pixel(x2, y2, self.color)]
                   
  def turn_on(self):
    self.is_blinking = True
    for light in self.lights:
      sense.set_pixel(light.x, light.y, light.color)
      
    sleep(0.5)
    
    for light in self.lights:
      sense.set_pixel(light.x, light.y, (0, 0, 0))
      
    sleep(0.5)
    
  def turn_off(self):
    self.is_blinking = False
    sense.set_pixel(light.x, light.y, (0, 0, 0))
    
class StopLight():
  def __init__(self):
    self.is_on = False
    self.color = (255, 0, 0)
    self.stop_pixels = [Pixel(2, 7, self.color),
                        Pixel(3, 7, self.color),
                        Pixel(4, 7, self.color),
                        Pixel(5, 7, self.color)]
    
  def turn_on(self):
    self.is_on = True
    self.color = (255, 0, 0)
    
    for pixel in self.stop_pixels:
      sense.set_pixel(pixel.x, pixel.y, self.color)
      
  def turn_off(self):
    self.is_on = False
    self.color = (0, 0, 0)
    
    for pixel in self.stop_pixels:
      sense.set_pixel(pixel.x, pixel.y, self.color)
    
class CarSim():
  def __init__(self):
    self.blinker_l = Blinker(x1=1, y1=0, x2=1, y2=7)
    self.blinker_r = Blinker(x1=6, y1=0, x2=6, y2=7)
    
    self.stop_light = StopLight()
  
  
car_sim = CarSim()
  
while True:
  # car_sim.blinker_r.blink()
  # car_sim.blinker_l.blink()
  # sleep(1)
  # car_sim.stop_light.on()
  # sleep(1)
  # car_sim.stop_light.off()
  
  for event in sense.stick.get_events():
    if event.action == "pressed":
      if event.direction == "down":
        car_sim.stop_light.turn_on()
        
    if event.action == "released":
      if event.direction == "down":
        car_sim.stop_light.turn_off()
      if event.direction == "left":
        if car_sim.blinker_r.is_blinking is True:
          car_sim.blinker_r.is_blinking = False
        car_sim.blinker_l.turn_on()

