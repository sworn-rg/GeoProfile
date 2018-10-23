# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 10:26:32 2018

This could be passed a data frame reference or even a pub sub.
Returns a list of dataframes...

@author: roger.gill
"""
from datetime import datetime
import statistics as st
import pandas as pd

class ChangePoint:
    """A Profile: Base class for geo profile
    Attributes:
    
    """

    def __init__(self, raw_df, config, method):
        """ Basic checks and conditions for class constructors """
        self.raw_df = raw_df
        self.config = config
        self.raw_df['datetime'] = pd.to_datetime(self.raw_df['timestamp'])
        
        if len(self.raw_df) < 1:
            raise Exception('Raw data requires at least 1 data point')
        
        if method == 'time_delta':
            self.time_delta()
    
    
    def time_delta(self):
        start = 0
        delta = 0
        activities = []
        for i in range(1, len(self.raw_df)):
            delta = self.raw_df['datetime'][i] - self.raw_df['datetime'][i - 1]
            if delta.total_seconds() <= self.config['time_delta_secs']:
                continue
            
            activities.append(self.raw_df.iloc[range(start, i+1)])
            start = i+1
        
        # need to check if the last point was a singleton
        if delta.total_seconds() <= self.config['time_delta_secs']:
            activities.append(self.raw_df.iloc[range(start, len(self.raw_df))])
            
        self.activities = activities
    
