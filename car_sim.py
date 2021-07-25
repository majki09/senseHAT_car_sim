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
                   
  def blink(self):
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
    
  def on(self):
    self.is_on = True
    self.color = (255, 0, 0)
    
    for pixel in self.stop_pixels:
      sense.set_pixel(pixel.x, pixel.y, self.color)
      
  def off(self):
    self.is_on = False
    self.color = (0, 0, 0)
    
    for pixel in self.stop_pixels:
      sense.set_pixel(pixel.x, pixel.y, self.color)
    
class CarSim():
  def __init__(self):
    self.blinker_l = Blinker(1, 0, 1, 7)
    self.blinker_r = Blinker(6, 0, 6, 7)
    
    self.stop_light = StopLight()
  
  
car_sim = CarSim()
  
while True:
  #car_sim.blinker_r.blink()
  car_sim.blinker_l.blink()
  sleep(1)
  car_sim.stop_light.on()
  sleep(1)
  car_sim.stop_light.off()
