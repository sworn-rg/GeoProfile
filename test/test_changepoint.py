# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 10:15:49 2018
@author: roger.gill
"""
import unittest
import sys, os
import pandas as pd
from ChangePoint.ChangePoint import ChangePoint

''' add the local directory to path and read test data '''
sys.path.append("..")
dir_path = os.path.dirname(os.path.realpath(__file__))

''' Changepoint from raw data '''
filename = "{0}\data\{1}".format(dir_path, 'profile_test.csv')
df = pd.read_csv(filename)

''' Changepoint from raw data '''

config = {'time_delta_secs' : 60*60} 
changepoints = ChangePoint(raw_df = df, config = config, method = 'time_delta')
counts = {}

for changepoint in changepoints.activities:
    n = len(changepoint)
    if n in counts:
        counts[n] += 1
    else:
        counts[n] = 1


class TestUM(unittest.TestCase):
    
    
    def setUp(self):
        pass
    
    def test_n_activities(self):
        self.assertEqual(len(changepoints.activities), 2111, 'ChangePoints: Number of Activities')
    
    def test_n1_activities(self):
        self.assertEqual(counts[1], 318, 'ChangePoints: Length of Acitivites 1')
    
    def test_n2_activities(self):
        self.assertEqual(counts[2], 941, 'ChangePoints: Length of Acitivites 2')

        
if __name__ == '__main__':
    unittest.main()