"""
Testing move sequence
"""

from screenbot import moves

MOVES_FILE = 'moves.txt'
NEW_MOVES_FILE = 'moves2.txt'

sequence = moves.InputSequence()
sequence.load(MOVES_FILE)

sequence.save(NEW_MOVES_FILE)

sequence.run()
