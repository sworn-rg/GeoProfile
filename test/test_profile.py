# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 10:15:49 2018

@author: roger.gill
"""
import unittest
import sys, os
import pandas as pd

from Activity.Activity import Activity
from Location.Location import Location
from Profile.Profile import Profile

''' add the local directory to path and read test data '''
sys.path.append("..")
dir_path = os.path.dirname(os.path.realpath(__file__))

''' location events '''
filename = "{0}\data\{1}".format(dir_path, 'profile_test.csv')
df = pd.read_csv(filename)

''' create list of Locations objects '''
locations = []
location_ids = df.cluster.unique()
for i in location_ids:
    ''' create list of Activity objects '''
    activity_cluster = []
    activities = df[df.cluster == i]
    activity_ids = activities.activity.unique()
    
    for j in activity_ids:
        
        activity_cluster.append(Activity(activities[activities.activity == j]))
    
    locations.append(Location(activity_cluster))

geo_profile = Profile(locations)

class TestUM(unittest.TestCase):
    
    
    def setUp(self):
        pass
    
    def test_n_activities(self):
        self.assertEqual(geo_profile.n_locations, 45, 'Location: Number of Elements')
            
        
if __name__ == '__main__':
    unittest.main()