# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 10:26:32 2018

@author: roger.gill
"""
from datetime import datetime
from geopy.distance import vincenty

class Activity:
    """An Activity: Base class for geo activity data event
    Attributes:
    
    """

    def __init__(self, raw_data_frame):
        """ Basic checks and conditions for class constructors """
        if len(raw_data_frame) < 2:
            raise Exception('An Activity requires at least 2 data points')
        
        self.df = raw_data_frame
        self.activity_summary()
        self.activity_time_features()
        self.activity_location_features()
        self.activity_classification()

    def activity_summary(self):
        self.n_obs = len(self.df)
     
    def activity_time_features(self):
        self.start_datetime = datetime.strptime(min(self.df.timestamp), '%Y-%m-%d %H:%M:%S.%f')
        self.end_datetime = datetime.strptime(max(self.df.timestamp), '%Y-%m-%d %H:%M:%S.%f')
        self.duration_secs = (self.end_datetime - self.start_datetime).seconds

    def activity_location_features(self):
        self.start_longitude = self.df['longitude'].iloc[0]
        self.start_latitude = self.df['latitude'].iloc[0]
        self.end_longitude = self.df['longitude'].iloc[-1]
        self.end_latitude = self.df['latitude'].iloc[-1]
        self.distance_travelled_ms = round(vincenty( (self.start_longitude, self.start_latitude) , (self.end_longitude, self.end_latitude)).meters, 0)
    
    def activity_classification(self, max_distance_ms = 100, number_of_points = 2):
        self.activity = 'Travel'
        if((self.n_obs == number_of_points) & (self.distance_travelled_ms < max_distance_ms)):
            self.activity = 'Location'
    
    def activity_string(self):
        return 'blahhh'
        