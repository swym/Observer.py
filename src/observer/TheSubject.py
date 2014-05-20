'''
Created on May 20, 2014

@author: alexandermertens
'''
from src.observer.Subject import Subject

class TheSubject(Subject):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        Subject.__init__(self)
        self.data = 0
        
        
    def inc_data(self):
        self.data = self.data + 1
        self.notify_observers()
        
    def dec_cata(self):
        self.data = self.data - 1
        self.notify_observers(param = "dec")