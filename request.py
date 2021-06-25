# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 00:21:17 2021

@author: Nidhi
"""

import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'experience':2, 'test_score':9, 'interview_score':6})

print(r.json())