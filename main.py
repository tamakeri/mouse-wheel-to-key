import keyboard
from pynput.mouse import Button, Controller


mouse= Controller()
while True:
    if keyboard.read_key() == "+":

        mouse.scroll(0, 1)
    if keyboard.read_key() == "-":

        mouse.scroll(0, -1)

 
