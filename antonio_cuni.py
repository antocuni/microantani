#import os
import random
try:
    from microbit import display, accelerometer, sleep
except ImportError:
    # to test on PC
    def sleep(milliseconds):
        import time
        time.sleep(milliseconds/1000.0)

class RainDrop(object):

    def __init__(self):
        self.rows = [[0]*5 for _ in range(5)]
        
    def step(self):
        brightness = list(range(10)) # from 0 to 9, 9=brightest
        choices = [0]*89 + brightness # ~10% of probability to have a drop of any non-zero brightness
        row = [random.choice(choices) for _ in range(5)]
        self.rows.insert(0, row)
        self.rows.pop()

    def get_delay(self):
        """
        Return the delay depending on the Z accelerometer.
        """
        # Completely untested, I had to write it blindly :(
        z = accelerometer.get_z()
        delay = 1-z
        delay = delay*(800) + 200 # always generate a delay between 0.2 and 1 seconds
        return int(delay)

    def run(self):
        while True:
            self.step()
            self.show()
            sleep(self.get_delay())

    def show(self):
        # Completely untested, I had to write it blindly :(
        display.clear()
        for y, row in enumerate(self.rows):
            for x, pixel in enumerate(row):
                display.set_pixel(x, y, pixel)

class RainDropTest(RainDrop):

    def show(self):
        os.system('clear')
        for y, row in enumerate(self.rows):
            for x, pixel in enumerate(row):
                if pixel:
                    print('*', end='')
                else:
                    print('.', end='')
            print()
        print()

    def get_delay(self):
        return 300 # bah, boring :(



#r = RainDropTest() # to test on linux
r = RainDrop()     # for micro:bit
r.run()
        
