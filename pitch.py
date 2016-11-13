'''
Authors: Michael Friedman
Created: 11/12/16

Description: Represents a pitch (letter, octave, and indication of
natural/sharp/flat)
'''

from decimal import Decimal

class Pitch:
    
    PITCHES = { 'A': 0, 'B': 2, 'C': 3, 'D': 5, 'E': 7, 'F': 8, 'G': 10 }
    ACCIDENTALS = { '#': +1, 'b': -1, '?': 0 }
    
    def __init__(self, pitch, accidental, octave):
        self._pitch = Pitch.PITCHES[pitch]
        self._accidental = Pitch.ACCIDENTALS[accidental]
        self._octave = octave
        
    
    '''
    Returns the frequency for a pitch 'pitch' semitones above A2, in
    the given octave.
    '''
    def freq(self):
        freq_A2 = Decimal(110.0)
        return freq_A2 * Decimal(2**((Decimal(self._pitch + self._accidental + (12.0 * self._octave))) / Decimal(12.0)))
