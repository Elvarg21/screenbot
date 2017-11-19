"""
Script that tests recording
"""

from screenbot import recording

MOVES_FILE = 'recorded_moves.txt'


recorder = recording.Recorder()
recorder.record()
#moves.save(MOVES_FILE)
