from pkg.net import EngageNet
import json
import urllib2

request = {
    "header" :{"refId":"python2.7request"}, 

    "payload":{
            'types': "P2P_EVENT,TICKETED_EVENT",
            'sortField': "name",
            'sortOrder': "ASCENDING",
    }
}

params = {
    "endpoint": "/api/developer/ext/v1/activities",
    'host': 'dev-api.salsalabs.org',
    'token': '_CpaYfT4zm0FBH8y1EABHzaSUQiMlTrVwgRECvlN54hb4QmIIW4eS1iYLVTaufogFVpKsfvvMMQ-WEZRsUi4krF6x0c1rSLfGeeS56iePxHKY40Z1LE3cD8PlQqY6IhXI6Gj1NeRZ02hMohBOV0nAA',
    'method': 'GET',
    'request': request
}
try:
    t = EngageNet(**params).run()
    j = json.dumps(t,sort_keys=True, indent=4, separators=(",", ': '))
    print j
except urllib2.HTTPError as e:
    print e

