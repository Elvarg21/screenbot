"""
Implementation of class InputSequence
"""

import time
import pyautogui

KEYBOARD_INPUT_SIGN = '$'
DEFAULT_TIME_DELAY = 0.25

class MouseMove:
    def __init__(self, time=0, drag=False):
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
    def __init__(self):
        self.click_count = 1

    def click(self):
        self.click_count += 1

    def to_string(self):
        return ' '.join(['click', str(self.click_count)])

    def from_string(self, string_data):
        data = string_data.split()
        self.click_count = int(data[1])

    def run(self):
        pyautogui.click(clicks=self.click_count, interval=0.25)


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
class Keyboard:
    def __init__(self, time=0):
'''


class InputSequence:

    def __init__(self, moves=[]):
        self.moves = moves

    def __add__(self, other):
        all_moves = self.moves + other.moves
        return InputSequence(all_moves)

    def add(self, move):
        self.moves.append(move)

    def save(self, filename):
        with open(filename, 'w') as f:
            data = [move.to_string() for move in self.moves]
            print('\n'.join(data), end='', file=f)

    def load(self, filename):
        self.moves = []
        with open(filename, 'r') as f:
            data = f.read().split('\n')
            for line in data:
                line = line.strip()
                print(line)
                if line.startswith('mouse'):
                    move = MouseMove()
                elif line.startswith('click'):
                    move = MouseClick()
                elif line.startswith('wait'):
                    move = Wait()
                else:
                    continue
                move.from_string(line)
                self.moves.append(move)

    def run(self):
        for move in self.moves:
            move.run()
            time.sleep(DEFAULT_TIME_DELAY)
