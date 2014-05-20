'''
Created on May 20, 2014

@author: alexandermertens
'''
from src.observer.TheSubject import TheSubject
from src.observer.TheObserver import TheObserver
if __name__ == '__main__':
    
    s = TheSubject()
    obs1 = TheObserver(s)
    obs2 = TheObserver(s)
    

    s.inc_data()  
    s.inc_data()
    s.dec_cata()
    
    s.inc_data()  
    s.inc_data()
    s.dec_cata()
    
    s.inc_data()  
    s.inc_data()
    s.dec_cata()
    
    s.inc_data()  
    s.inc_data()
    s.dec_cata()