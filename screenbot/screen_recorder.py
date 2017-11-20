"""
Module that records keyboard and mouse inputs
"""

import time
from pynput import mouse, keyboard

from .screen_input import InputSequence, MouseMove, MouseClick, KeyboardInput


DEFAULT_FREQUENCE = 1


class Recorder:

    def __init__(self, record_frequence=DEFAULT_FREQUENCE):
        self.record_frequence = DEFAULT_FREQUENCE
        self.moves = InputSequence()

        self.active = {}
        self.record_start = 0

        self.mouse = mouse.Listener(on_move=self.mouse_on_move, on_click=self.mouse_on_click,
                                    on_scroll=self.mouse_on_scroll)
        self.keyboard = keyboard.Listener(on_press=self.keyboard_on_press, on_release=self.keyboard_on_release)

    def record(self):
        self.record_start = time.time()
        self.active = {'mouse-move': MouseMove(time=self.record_start)}
        print('Recording started')
        with self.mouse as mouse_listener, self.keyboard as keyboard_listener: #try using threading for simultaneous end of recording
            mouse_listener.join()
            keyboard_listener.join()
        print('Recording stopped')

    def save(self, filename):
        self.moves.save(filename)

    def mouse_on_move(self, x, y):
        move_start = self.active['mouse-move'].time
        move_end = time.time()
        if move_end - move_start >= self.record_frequence:
            self.active['mouse-move'].end(x, y, move_end)
            self.moves.add((move_start - self.record_start, self.active['mouse-move']))
            self.active['mouse-move'] = MouseMove(time=time.time())

    def mouse_on_click(self, x, y, button, click):
        if button != mouse.Button.left:
            return # not yet supported
        move_start = self.active['mouse-move'].time
        self.active['mouse-move'].end(x, y, time.time())
        self.moves.add((move_start - self.record_start, self.active['mouse-move']))
        self.active['mouse-move'] = MouseMove(time=time.time(), drag=click)
        '''
        name = 'button-' + button.name
        if click and name not in self.active:
            self.active[name] = MouseClick(button=button.name, time=time.time())
        if not click:
            click_start = self.active[name].time
            self.active[name].end(time.time())
            self.moves.add((click_start - self.record_start, self.active[name]))
            del self.active[name]
        '''

    def mouse_on_scroll(self, x, y, horizontal_scroll, vertical_scroll):
        # print(x, y, horizontal_scroll, vertical_scroll)
        pass

    def keyboard_on_press(self, key):
        if key == keyboard.Key.esc:
            self.stop_recording()
            return False
        try:
            # print('alphanumeric key {0} pressed'.format(key))
            char = key.char
            self.moves.add((time.time() - self.record_start, KeyboardInput(char, input_type='press')))
        except AttributeError:
            #print('special key {0} pressed'.format(key))
            name = key.name
            self.moves.add((time.time() - self.record_start, KeyboardInput('{' + name + '}', input_type='press')))
        self.active['mouse-move'].time = time.time()

    def keyboard_on_release(self, key):
        # print('{0} released'.format(key))
        try:
            # print('alphanumeric key {0} pressed'.format(key))
            char = key.char
            self.moves.add((time.time() - self.record_start, KeyboardInput(char, input_type='release')))
        except AttributeError:
            #print('special key {0} pressed'.format(key))
            name = key.name
            self.moves.add((time.time() - self.record_start, KeyboardInput('{' + name + '}', input_type='release')))
        self.active['mouse-move'].time = time.time()

    def stop_recording(self):
        keyboard.Listener.stop(self.keyboard)
        mouse.Listener.stop(self.mouse)


