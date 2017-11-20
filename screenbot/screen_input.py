"""
Implementation of class InputSequence
"""

import time
import pyautogui
from pynput import mouse, keyboard


from . import screen_threader

KEYBOARD_INPUT_SIGN = '$'
DEFAULT_TIME_DELAY = 0.25

class MouseMove:
    def __init__(self, x=None, y=None, time=0, drag=False):
        self.x = x
        self.y = y
        self.time = time
        self.drag = drag

    def end(self, x, y, time):
        self.x = x
        self.y = y
        self.time = time - self.time

    def to_string(self):
        data = ['mouse', self.x, self.y]
        if self.time > 0:
            data.append(self.time)
        if self.drag:
            data.append('drag')
        return ' '.join(map(str, data))

    def from_string(self, string_data):
        data = string_data.split()
        self.x = int(data[1])
        self.y = int(data[2])
        if len(data) > 3:
            if data[3] == 'drag':
                self.drag = True
            else:
                self.time = float(data[3])
        if len(data) > 4 and data[4] == 'drag':
            self.drag = True

    def run(self):
        if self.drag:
            pyautogui.dragTo(self.x, self.y, self.time, button='left')
        else:
            pyautogui.moveTo(self.x, self.y, self.time)


class MouseClick:
    def __init__(self, button='left', time=0, click_count=1):
        self.button = button
        self.click_count = click_count
        self.time = time

    def end(self, time):
        self.time = time - self.time

    def click(self):
        self.click_count += 1

    def to_string(self):
        return 'click{}-{} {}'.format(self.click_count, self.button, self.time)

    def from_string(self, string_data):
        data = string_data.split()
        self.time = float(data[1])
        data = data[0].split('-')
        if len(data) > 1:
            self.button = data[1]
        if len(data[0]) > 5:
            self.click_count = int(data[0][5:])

    def run(self):
        #pyautogui.click(clicks=self.click_count, interval=0.25)
        clicker = mouse.Controller()
        my_button = getattr(mouse.Button, self.button)
        time_interval = self.time / self.click_count
        for i in range(self.click_count):
            clicker.press(my_button)
            time.sleep(time_interval)
            clicker.release(my_button)


'''
class Wait:
    def __init__(self, time=0):
        self.time = time

    def end(self, end_time):
        self.time = end_time - self.time

    def to_string(self):
        return ' '.join(['wait', str(self.time)])

    def from_string(self, string_data):
        data = string_data.split()
        self.time = float(data[1])

    def run(self):
        time.sleep(self.time)
'''

class KeyboardInput:
    def __init__(self, message=None, input_sign=KEYBOARD_INPUT_SIGN):
        self.message = message
        self.input_sign = input_sign

    def to_string(self):
        return ''.join([self.input_sign, self.message])

    def from_string(self, string_data):
        if string_data[0] != self.input_sign:
            raise ValueError('Keyboard input sign undetected')
        self.message = string_data[1:]

    def run(self):
        writer = keyboard.Controller()
        message_parts = parse_message(self.message)
        is_word = True
        for msg in message_parts:
            if msg != '':
                if is_word:
                    writer.type(msg)
                else:
                    my_key = getattr(keyboard.Key, msg)
                    writer.press(my_key)
                    writer.release(my_key)
            is_word = not is_word


def parse_message(message):
    chunks = message.split('{')
    parts = [chunks[0]]
    for chunk in chunks[1:]:
        if chunk.count('}') != 1:
            raise ValueError('Failed to parse message: {}'.format(message))
        s_chunk = chunk.split('}')
        parts.extend(s_chunk)
    return parts



class InputSequence:

    def __init__(self, moves=[], filename=None):
        self.moves = moves
        self.filename = filename

        if self.filename is not None:
            self.load()

    def __add__(self, other):
        all_moves = self.moves + other.moves
        return InputSequence(all_moves)

    def add(self, move):
        self.moves.append(move)

    def save(self, filename=None):
        self.moves.sort()
        if filename is not None:
            self.filename = filename
        with open(self.filename, 'w') as f:
            for time, move in self.moves:
                print('{} {}'.format(time, move.to_string()), end='\n', file=f)

    def load(self, filename=None):
        if filename is not None:
            self.filename = filename
        self.moves = []
        with open(self.filename, 'r') as f:
            data = f.read().split('\n')
            for line in data:
                line = line.strip()
                if line == '':
                    continue
                items = line.split()
                time = float(items[0])
                if items[1].startswith('mouse'):
                    move = MouseMove()
                elif items[1].startswith('click'):
                    move = MouseClick()
                #elif items[1].startswith('wait'):
                #    move = Wait()
                elif items[1].startswith(KEYBOARD_INPUT_SIGN):
                    move = KeyboardInput()
                else:
                    continue
                move.from_string(line[len(items[0]) + 1:])
                self.moves.append((time, move))

    def run(self):
        screen_threader.threaded_run(self.moves)

