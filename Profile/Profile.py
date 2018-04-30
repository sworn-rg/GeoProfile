# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 10:26:32 2018

@author: roger.gill
"""
from datetime import datetime
from geopy.distance import vincenty
import statistics as st

class Location:
    """An Activity: Base class for geo activity data event
    Attributes:
    
    """

    def __init__(self, activity_cluster, from_json = False):
        """ Basic checks and conditions for class constructors """
        self.activity_cluster = activity_cluster
        self.n_activities = len(self.activity_cluster)
        
        if len(self.activity_cluster) < 1:
            raise Exception('A location requires 1 Activities')
        
        
        self.abstract_activities()
        self.location_summary()
    
    def abstract_activities(self):
        self.datetimes = []
        self.longitudes = []
        self.latitudes = []
        self.courses = []
        for i in range(self.n_activities):
            self.datetimes.append(self.activity_cluster[i].end_datetime)
            self.latitudes.append(self.activity_cluster[i].end_latitude)
            self.longitudes.append(self.activity_cluster[i].end_longitude)

    def location_summary(self):
        self.first_activity = min(self.datetimes).strftime("%Y-%m-%d")
        self.last_activity = max(self.datetimes).strftime("%Y-%m-%d")
    
    def location_time_summary(self):
        self.n_activities = len(self.activity_cluster)
    
    def location_activity_summary(self):
        return 'blahhh'
    
    def from_json(self):
        return 'blahh'
    