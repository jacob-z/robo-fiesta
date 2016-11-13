'''
Authors: Michael Friedman
Created: 11/12/16

Description: Tests the buzzer by playing a few notes.
'''

from buzzer import Buzzer

'''
Plays a few notes on a buzzer.
'''
def main():
    buzzer = Buzzer(2)
    buzzer.play('A', '?', 2, 2, 60)
    

if __name__ == '__main__':
    main()
