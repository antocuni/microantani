import os
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
        choices = [0]*9 + [9] # 10% of probability to have a drop
        row = [random.choice(choices) for _ in range(5)]
        self.rows.insert(0, row)
        self.rows.pop()

    def run(self):
        while True:
            self.step()
            self.show()
            sleep(300)

    def show(self):
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




r = RainDropTest() # to test on linux
#r = RainDrop()     # for micro:bit
r.run()
        
