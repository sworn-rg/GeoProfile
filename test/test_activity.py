# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 10:15:49 2018

@author: roger.gill
"""
import unittest

import sys, os

import pandas as pd
from datetime import datetime
from geopy.distance import vincenty

from Activity.Activity import Activity

''' add the local directory to path and read test data '''
sys.path.append("..")
dir_path = os.path.dirname(os.path.realpath(__file__))

''' travel activity '''
filename = "{0}\data\{1}".format(dir_path, 'activity_travel_test.csv')
df = pd.read_csv(filename)
travel = Activity(df)

''' location activity '''
filename = "{0}\data\{1}".format(dir_path, 'activity_location_test.csv')
df = pd.read_csv(filename)
location = Activity(df)


class TestUM(unittest.TestCase):
    
    
    def setUp(self):
        pass
    
    def test_n_obs(self):
        self.assertEqual(travel.n_obs, 795, 'Activity : Number of Elements')
    
    def test_time_features(self):
        start_datetime = datetime.strptime('2017-05-14 03:30:34.098', '%Y-%m-%d %H:%M:%S.%f')
        end_datetime = datetime.strptime('2017-05-14 11:08:22.000', '%Y-%m-%d %H:%M:%S.%f')
        duration_seconds = (end_datetime - start_datetime).seconds
        self.assertEqual(travel.start_datetime, start_datetime, 'Activity: Time feature 1')
        self.assertEqual(travel.end_datetime, end_datetime, 'Activity: Time feature 2')
        self.assertEqual(travel.duration_secs, duration_seconds, 'Activity: Time feature 3')
    
    def test_location_features(self):
        start_longitude = -5.12614750331377
        start_latitude = 45.04940030471891
        end_longitude = 5.68948678213787
        end_latitude = 48.2277418554901
        distance_travelled_ms = round(vincenty((start_longitude, start_latitude), (end_longitude, end_latitude)).meters, 0)
        self.assertAlmostEqual(travel.start_longitude, start_longitude)
        self.assertAlmostEqual(travel.start_latitude, start_latitude)
        self.assertAlmostEqual(travel.end_longitude, end_longitude)
        self.assertAlmostEqual(travel.end_latitude, end_latitude, places = 7)
        self.assertEqual(travel.distance_travelled_ms, distance_travelled_ms)
    
    
    def test_location_category(self):
        self.assertEqual(travel.activity, 'Travel', 'Activity: Activity 1')
        self.assertEqual(location.activity, 'Location', 'Activity: Activity 2')
    
    def test_write(self):
        self.assertEqual(travel.activity_string(), 'blahhh', 'Output')

if __name__ == '__main__':
    unittest.main()