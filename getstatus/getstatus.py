#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cfg
import json
import os
import twitter
import tweepy
from log import setup_logging
import logging

setup_logging()
logger = logging.getLogger(__name__)

pathin = cfg.getConfig()["settings"]["doctoctoc"]
pathout = cfg.getConfig()["settings"]["complete"]

auth = twitter.getAuth()
api = tweepy.API(auth, wait_on_rate_limit=True)
tweets= []
for filename in os.listdir(pathin):
    try:
        tweet = api.get_status(filename)
        tweets.append(tweet._json)
        print(filename)
    except tweepy.error.TweepError as e:
        logger.debug("error: %s", e)
        pass

for tweet in tweets:
    path = pathout + str(tweet["id"])
    if not os.path.exists(path):
        with open(path, mode='wt') as f:
            f.write(json.dumps(tweet))
            print("wrote {}".format(str(tweet["id"])))