
import keyboard
from pynput.mouse import Button, Controller


mouse= Controller()
while True:
    key=keyboard.read_key()
    if key == "+":

        mouse.scroll(0, 1)
    if key == "-":

        mouse.scroll(0, -1)
