#!/usr/bin/python
'''
Authors: Michael Friedman
Created: 11/12/16

Description: GUI for controlling the vehicle
'''

import Tkinter
from randomwalk import RandomWalk

class App:

    def __init__(self):
        self._rw = RandomWalk('ghostbusters.txt')
    
    def randomwalk_callback(self):
        self._rw.start()
            
    def stop_callback(self):
        self._rw.stop()
    
    def run(self):
        top = Tkinter.Tk()
        
        width = 100
        height = 14
        btn_randomwalk = Tkinter.Button(top, bg='green', command=self.randomwalk_callback, width=width, height=height)
        btn_randomwalk.pack()
        btn_stop = Tkinter.Button(top, bg='red', command=self.stop_callback, width=width, height=height)
        btn_stop.pack()
        
        top.mainloop()

def main():
    App().run()
    
if __name__ == '__main__':
    main()
    
