from pkg.net import EngageNet
import json
import urllib2

request = {
    "header" :{"refId":"python2.7request"}, 

    "payload":{
            "modifiedFrom":"2016-05-26T11:49:24.905Z",
            "type":"FUNDRAISE",
            "offset":0,
            "count":20
    }
}
params = {
    "endpoint": "/api/integration/ext/v1/activities/search",
    'host': 'hq.uat.igniteaction.net',
    'token': 'wBTvk4rH5auTh4up8nOaVCcJBYWT3jr2Wk7QnlcOc4QnN1kWkb5hzf4Jge-_hHpaCEqwKmhH_Y953ExF9VdQ8MuR7dE3It-UwCBEnK4tUj8',
    'method': 'POST',
    'request': request
}
try:
    t = EngageNet(**params).run()
    j = json.dumps(t,sort_keys=True, indent=4, separators=(",", ': '))
    print j
except urllib2.HTTPError as e:
    print e
