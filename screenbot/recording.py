"""
Module that records keyboard and mouse inputs
"""

import pyautogui
import time
from pynput import mouse, keyboard

from . import moves


WAIT_TIME = 1

'''def get_mouse_state(start_time=0):
    state = {
        'position': pyautogui.position(),
        'time': time.time() - start_time
    }
    return state


def recorder():
    stack = []
    start_time = time.time()
    mouse_state = get_mouse_state(start_time)
    stack.append(mouse_state)
    try:
        while True:
            if mouse_state['position'] != pyautogui.position(start_time) and time.time() - mouse_state['time'] >= WAIT_TIME:
                stack.append(mouse_state)
                mouse_state = get_mouse_state(start_time)


    except KeyboardInterrupt:
        pass
'''

class Recorder:

    def __init__(self):
        self.moves = moves.InputSequence()

    def record(self):
        self.time = time.time()
        self.mouse = mouse.Listener(on_move=self.on_move, on_click=self.on_click, on_scroll=self.on_scroll)
        '''with self.mouse as listener:
            listener.join()'''
        self.mouse.start()
        print('ok')

    def on_move(self, x, y):
        print(x, y)

    def on_click(self, x, y, button, click):
        print(x, y, button, click)

    def on_scroll(self, x, y, horizontal_scroll, vertical_scroll):
        print(x, y, horizontal_scroll, vertical_scroll)
        mouse.Listener.stop(self.mouse)
