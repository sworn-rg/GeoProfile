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
            if self.activity_cluster[i].end_course > 0 :
                self.courses.append(self.activity_cluster[i].end_course)
        
    def location_summary(self):
        self.first_activity = min(self.datetimes).strftime("%Y-%m-%d")
        self.last_activity = max(self.datetimes).strftime("%Y-%m-%d")
        self.med_longitude = st.median(self.longitudes)
        self.med_latitude = st.median(self.latitudes)
        self.med_course = st.median(self.courses)
    
    
    def location_time_summary(self):
        self.n_activities = len(self.activity_cluster)
    
    def location_activity_summary(self):
        return 'blahhh'
    
    def location_coord_features(self, longitude, latitude):
        return 'blahhh'
    
    def street_map_dictionary(self, course = False, pitch = False):
        heading = self.med_course if (not course) else course
        pitch = 10 if (not pitch) else pitch 
        coords = str(self.med_latitude) + ',' + str(self.med_longitude)
        street_map = {'location' : coords, 'heading'  : heading, 'pitch' : pitch}
        
        return street_map
    
    def from_json(self):
        return 'blahh'
    