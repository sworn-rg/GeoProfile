# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 10:26:32 2018

@author: roger.gill
"""
from datetime import datetime
from geopy.distance import vincenty
import statistics as st

class Profile:
    """A Profile: Base class for geo profile
    Attributes:
    
    """

    def __init__(self, location_list):
        """ Basic checks and conditions for class constructors """
        self.location_list = location_list
        self.n_locations = len(location_list)
        
        if len(self.location_list) < 1:
            raise Exception('A location requires 1 Activities')
    
    
    def location_activity_summary(self):
        return 'blahhh'
    
    def from_json(self):
        return 'blahh'
    