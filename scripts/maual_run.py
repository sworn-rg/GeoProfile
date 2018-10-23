# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 10:46:19 2018

Will need to put config into the parameters.

@author: roger.gill
"""

BUCKET = 'sworn-installs'

import logging
import pandas as pd
logging.basicConfig(filename='load.log', level=logging.INFO)

""" this is the order in which we need to run from statics files """
from ChangePoint.ChangePoint import ChangePoint
from Activity.Activity import Activity
from Cluseter.Cluster import Cluster
from Location.Location import Location
from Profile.Profile import Profile

import numpy as np
from google.cloud import storage
storage_client = storage.Client()
sojourn_bucket = storage_client.bucket(BUCKET)
blobs = sojourn_bucket.list_blobs()

""" get the largest blob first """installs = {}
for blob in blobs:
    installs[blob.name]= blob.size


installs = sorted(installs, key=installs.get, reverse=True)

""" now loop through """
from io import StringIO

config = {'time_delta_secs' : 360}
config['dbscan_distance_m'] = 50
config['min_samples_cluster'] = 5

for i in range(len(installs)):
    if i==0:
        continue#
    
    print(installs[i])
    blob = sojourn_bucket.blob(installs[i])
    data_str = blob.download_as_string().decode("utf-8")
    df = pd.read_csv(StringIO(data_str), sep=",")
    change_ob = ChangePoint(df, config, method = 'time_delta')
    activities = []
    for activity in change_ob.activities:
        act = Activity(activity)
        if act.active:
            activities.append(act)
    """ now loop through """
    out = Cluster(activities, config)
    n = len(np.unique(out.labels[out.labels!=-1]))
    print(n)




