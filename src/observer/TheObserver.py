'''
Created on May 20, 2014

@author: alexandermertens
'''
from src.observer.Observer import Observer


class TheObserver(Observer):
    '''
    classdocs
    '''


    def __init__(self, subject):
        '''
        Constructor
        '''
        self._my_subject = subject
        self._my_subject.attach(self)
        pass
    
    def update(self, subject, param):
        print(self._my_subject.data)
  
        if(param):
            print("param", param)
            print("subject", subject)

