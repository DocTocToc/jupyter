#!/usr/bin/env python
# -*- coding: utf-8 -*-

u""""
json objects collected with TweetScraper contain a "nbr_reply" field.
json objects collected with basic Twitter API lack "reply_count field.
This script adds this field.
"""

import cfg
import json
import os
from log import setup_logging
import logging
import myprettyprint

setup_logging()
logger = logging.getLogger(__name__)

path = cfg.getConfig()["settings"]["complete"]

tweets = []

for filename in os.listdir(path):
    p = path + filename
    with open(p, mode='r') as f:
        tweets.append(json.load(f))

sum = 0        
for tweet in tweets:
    sum+=tweet["reply_count"]
print(sum)