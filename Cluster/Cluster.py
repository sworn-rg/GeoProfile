# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 10:26:32 2018

This could be passed a data frame reference or even a pub sub.
Returns a list of dataframes...


@author: roger.gill
"""
from math import sqrt
import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

class Cluster:
    """A Profile: Base class for cluster
    Attributes:
    
    """

    def __init__(self, activity_list, config, start = True):
        """ Basic checks and conditions for class constructors """
        self.start = start
        self.activity_list = activity_list
        self.config = config
        self.create_actiuvity_df()
        self.my_clusters()
        
    
    def create_actiuvity_df(self):
        longitude = []
        latitude = []
        
        for activity in self.activity_list:
            if self.start == True:
               latitude.append(activity.start_latitude)
               longitude.append(activity.start_longitude)
            if self.start == False:
                latitude.append(activity.end_latitude)
                longitude.append(activity.end_longitude)
        
        self.activity_df = pd.DataFrame({'longitude' : longitude, 'latitude' : latitude})
            
    
    def threshold_eps(self):
        """ distance in M of one degree delta """
        delta_long = 54.6
        delta_lat  = 69
        hyp_distance_m = 1600 * sqrt((delta_long*delta_long) + (delta_lat*delta_lat))
        eps = self.config['dbscan_distance_m'] / hyp_distance_m 
        return eps
    
    def my_clusters(self):
        
        X = self.activity_df[['longitude', 'latitude']].values
        X = StandardScaler().fit_transform(X)
        eps = self.threshold_eps()
        db = DBSCAN(eps = eps, min_samples = self.config['min_samples_cluster']).fit(X)
        labels = db.labels_
        
        self.labels = labels
        
        return 1



