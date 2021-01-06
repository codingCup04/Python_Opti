"""
Made by codingPro01.
Do not delete this.
"""
import time, random, math
from pynput.keyboard import Key, Controller
keyb = Controller()
a = 0
b = 0
c = 0
def delay(sec):
    time.sleep(sec)
def delayms(msec):
    time.sleep(msec / 1000)
def randnum(min, max):
    return random.randint(min, max)
def randeven(min, max):
    return random.randrange(min, max + 1 , 2)
def typeKey(text):
    keyb.type(text)
def copyKey():
    keyb.press(Key.ctrl)
    keyb.press("c")
    keyb.release(Key.ctrl)
    keyb.release("c")
def selectAll():
    keyb.press(Key.ctrl)
    keyb.press("a")
    keyb.release(Key.ctrl)
    keyb.release("a")
def pasteKey():
    keyb.press(Key.ctrl)
    keyb.press("v")
    keyb.release(Key.ctrl)
    keyb.release("v")
def delAll():
    keyb.press(Key.ctrl)
    keyb.press("a")
    keyb.press(Key.delete)
    keyb.release(Key.delete)
    keyb.release(Key.ctrl)
    keyb.release("a")
def divide(dividend, divisor):
    return dividend / divisor
def mult(fac1, fac2):
    return fac1 * fac2
def multiply(fac1, fac2):
    return fac1 * fac2
def subt(val1, val2):
    return val1 - val2
def subtract(val1, val2):
    return val1 - val2
def sum(val1, val2):
    return val1 + val2
def add(val1, val2):
    return val1 + val2
def pi():
    return math.pi

class printOut:
    def __init__():
        pass
    def randnum(min, max):
        print(random.randint(min, max))
    def randeven(min, max):
        print(random.randrange(min, max + 1 , 2))
    def divide(dividend, divisor):
        print(dividend / divisor)
    def mult(fac1, fac2):
        print(fac1 * fac2)
    def multiply(fac1, fac2):
        print(fac1 * fac2)
    def subt(val1, val2):
        print(val1 - val2)
    def subtract(val1, val2):
        print(val1 - val2)
    def sum(val1, val2):
        print(val1 + val2)
    def add(val1, val2):
        print(val1 + val2)
    def pi():
        print(math.pi)
    def countdown(min, max, delay):
        i = min
        while i != max + 1:
            print(i)
            i += 1
            time.sleep(delay)
