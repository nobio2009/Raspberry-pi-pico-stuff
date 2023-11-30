try:
    # Imports
    import time
    import random
    from machine import Pin, ADC
    from neopixel import NeoPixel

    # Define the strip pin number (28) and number of LEDs (15)
    strip = NeoPixel(Pin(28), 15)

    # Set up the potentiometer on ADC pin 26
    potentiometer = ADC(Pin(26))

    # Colour variables
    red = 255,0,0
    green = 0,255,0
    white = 255,255,255
    yellow = 255,255,0
    pink = 255,20,147
    lblue = 0,0,128
    orange = 255,69,0
    
    
    # Define colour list
    colours = [red, green, white, yellow, pink, lblue, orange]

    while True: # Run forever

        # Iterate over the colours
        for j in colours:
            
            # Then iterate over 15 leds
            for i in range(15):
                
                # Set the next LED in the range to light with a colour
                strip[i] = (j)
                
                # Read the potentiometer
                # Divide the reading to make it more usable as a time delay
                mydelay = potentiometer.read_u16() / 50000
                
                # Delay - the speed of the chaser
                time.sleep(mydelay)
                
                # Send the data to the strip
                strip.write()
except KeyboardInterrupt:
    strip = NeoPixel(Pin(28), 15)
    
    for p in range(15):
        strip.fill((0, 0, 0))



