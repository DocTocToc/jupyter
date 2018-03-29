from TwitterAPI import TwitterAPI, constants
import json
import cfg

# Uses TwitterAPI to generate a twarc by monkeypatching in Twitter's private conversation API.

constants.ENDPOINTS.update({'conversation/show/:PARAM': ('GET', 'api')})
api = TwitterAPI(cfg.getConfig()["twitter"]["consumer_key"],
                 cfg.getConfig()["twitter"]["consumer_secret"],
                 cfg.getConfig()["twitter"]["access_token"],
                 cfg.getConfig()["twitter"]["access_token_secret"])

twid = 210290960695959553

r = api.request('conversation/show/:%d' % twid, {"count":100})

for item in r:
    print(json.dumps(item))