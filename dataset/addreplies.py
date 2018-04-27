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

pathin = cfg.getConfig()["settings"]["doctoctoc"]
pathout = cfg.getConfig()["settings"]["complete"]

partial_tweets = []
complete_tweets = []

for filename in os.listdir(pathin):
    path = pathin + filename
    with open(path, mode='r') as f:
        partial_tweets.append(json.load(f))
        
for filename in os.listdir(pathout):
    path = pathout + filename
    with open(path, mode='r') as f:
        complete_tweets.append(json.load(f))
        
for ptweet in partial_tweets:
    #myprettyprint.MyPrettyPrinter().pprint(ptweet)
    reply_count = ptweet["nbr_reply"]
    for ctweet in complete_tweets:
        if ptweet["ID"] == str(ctweet["id"]):
            ctweet["reply_count"]= reply_count
            
for ctweet in complete_tweets:
    path = pathout + str(ctweet["id"])
    with open(path, mode="w") as f:
        json.dump(ctweet, f)