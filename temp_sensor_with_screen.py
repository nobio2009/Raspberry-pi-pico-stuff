# Imports
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import onewire, ds18x20
import time

# Set up I2C and the pins we're using for it
i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)

# Short delay to stop I2C falling over
time.sleep(1) 

# Define the display and size (128x32)
display = SSD1306_I2C(128, 32, i2c)

#Temp sensor
# Set the data pin for the sensor
SensorPin = Pin(26, Pin.IN)
 
# Tell MicroPython we're using a DS18B20 sensor, and which pin it's on
sensor = ds18x20.DS18X20(onewire.OneWire(SensorPin))
 
# Look for DS18B20 sensors (each contains a unique rom code)
roms = sensor.scan()

#scan/show
while True: # Run forever
 
    sensor.convert_temp() # Convert the sensor units to centigrade
 
    time.sleep(2) # Wait 2 seconds (you must wait at least 1 second before taking a reading)
 
    for rom in roms: # For each sensor found (just 1 in our case)
 
        print((sensor.read_temp(rom)),"°C") # Print the temperature reading with °C after it
        
        # Clear the display first
        display.fill(0) 

        # Write a line of text to the display
        display.text(f"{(sensor.read_temp(rom))} C",0,0)

        # Update the display
        display.show()
 
        time.sleep(0.5) # Wait 5 seconds before starting the loop again

    
