"""
Script that tests recording
"""

from screenbot.screen_recorder import Recorder
from screenbot.screen_input import InputSequence

MOVES_FILE = 'recorded_moves.txt'
RECORD = False

if RECORD:
    recorder = Recorder()
    recorder.record()
    recorder.save(MOVES_FILE)
else:
    inputs = InputSequence()
    inputs.load(MOVES_FILE)
    inputs.run()


