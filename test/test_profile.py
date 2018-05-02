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
    
    def test_time_profile(self):
        time_profile = {'00': 64, '01': 22, '06': 3, '07': 46, '10': 27, '11': 60, '12': 66, '13': 38, '14': 79, '15': 80, '16': 21, '17': 79, '18': 208, '19': 164, '20': 190, '21': 229, '22': 164, '23': 74}
        self.assertEqual(my_location.time_profile, time_profile, 'time_profile')
    
    def test_summary_end(self):
        self.assertEqual(my_location.first_activity, '2016-09-12', 'Start Time')
        self.assertEqual(my_location.last_activity, '2017-07-22', 'End Time')
        self.assertAlmostEqual(my_location.med_longitude, -1.160843, 5)
        self.assertAlmostEqual(my_location.med_latitude, 51.01245, 5)
        self.assertAlmostEqual(my_location.med_course, 180.3516, 4)
        
    def test_street_map(self):
        image_params = my_location.street_map_dictionary()
        self.assertEqual(image_params['location'], '51.0124514356,-1.16084307656', 'Image: coords')
        self.assertAlmostEqual(image_params['heading'], 180.3516, 4)
        self.assertEqual(image_params['pitch'], 10, 'Image: pitch')
        
        image_params = my_location.street_map_dictionary(pitch = 123.456)
        self.assertAlmostEqual(image_params['pitch'], 123.456, 3)
        
        
if __name__ == '__main__':
    unittest.main()