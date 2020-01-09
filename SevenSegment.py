import RPi.GPIO as GPIO
import time
import sys

class SevenSegment():

    int_to_pins = {
        0: [0, 1, 2, 3, 4, 5],
        1: [1, 2],
        2: [0, 1, 3, 4, 6],
        3: [0, 1, 2, 3, 6],
        4: [1, 2, 5, 6],
        5: [0, 2, 3, 5, 6],
        6: [2, 3, 4, 5, 6],
        7: [0, 1, 2, 5],
        8: [0, 1, 2, 3, 4, 5, 6],
        9: [0, 1, 2, 3, 5, 6]
    }

    @property
    def current(self):
        return self.__current
    
    @current.setter
    def current(self, current):
        if 0 <= current <= 9:
            __current = current
        else:
            raise ValueError("current must be int and greater than -1, less than 10")


# pins is a pin number array that used for 7 segment display.
# pins array 's order must be set 0 ~ 7 clockwise. 
# pins[0] is top of segment. pins[6] is center segment. pins[7] is dp. 
    def __init__(self, pins):
        self.pins = pins
        self.__current = 0
        GPIO.setmode(GPIO.BOARD)
        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)
        self.display()

    def set_display(self, target_index):
        for pin in self.pins:
            GPIO.output(pin, False)

        for i in target_index:
            GPIO.output(self.pins[i], True)
    
    def display(self):
        self.set_display(self.int_to_pins[self.current])

    def display_number(self, digit):
        self.current = digit
        self.set_display(self.int_to_pins[digit])
    
    def display_dp(self):
        GPIO.output(self.pins[-1], GPIO.HIGH)
    
    def destory(self):
        for pin in self.pins:
            GPIO.output(pin, False)
        GPIO.cleanup()

    def __add__(self, other):
        return self.__class__(self.current + other)
    
    def __sub__(self, other):
        return self.__class__(self.current - other)
        
    def __mul__(self, other):
        return self.__class__(self.current * other)

    def __truediv__(self, other):
        return self.__class__(self.current / other)
    
    def __mod__(self, other):
        return self.__class__(self.current % other)
    
    def __iadd__(self, other):
        self.current += other
        return self
    
    def __isub__(self, other):
        self.current -= other
        return self

    def __imul__(self, other):
        self.current *= other
        return self

    def __itruediv__(self, other):
        self.current /= other
        return self

    def __imod__(self, other):
        self.current %= other
        return self

def destroy():
    for pin in pins:
        GPIO.output(pin, GPIO.LOW)
    GPIO.cleanup()
