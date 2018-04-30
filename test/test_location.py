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


''' add the local directory to path and read test data '''
sys.path.append("..")
dir_path = os.path.dirname(os.path.realpath(__file__))

''' location events '''
filename = "{0}\data\{1}".format(dir_path, 'location_activity_test.csv')
df = pd.read_csv(filename)
travel = Activity(df)

''' create list of Activity objects '''
activity_cluster = []

event_ids = df.event_id.unique()
for i in event_ids:
    activity_cluster.append(Activity(df[df.event_id == i]))

my_location = Location(activity_cluster)

class TestUM(unittest.TestCase):
    
    
    def setUp(self):
        pass
    
    def test_n_activities(self):
        self.assertEqual(my_location.n_activities, 31, 'Location: Number of Elements')
    
    def test_summary_end(self):
        self.assertEqual(my_location.first_activity, '2016-09-12', 'Start Time')
        self.assertEqual(my_location.last_activity, '2017-07-22', 'End Time')

if __name__ == '__main__':
    unittest.main()