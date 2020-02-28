# Application to display JSON for an endpoint.

import argparse
import json
import yaml

from pkg.net import EngageNet

parser = argparse.ArgumentParser(description='Display email blast URLs for Engage')
parser.add_argument('--login', dest='loginFile', action='store',
                            help='YAML file with login credentials')

args = parser.parse_args()
if args.loginFile == None:
    print("Error: --login is REQUIRED.")
    exit(1)
cred = yaml.load(open(args.loginFile))

devHost = 'dev-api.salsalabs.org'
if 'devHost' in cred:
    host = cred['devHost']

endpoint = '/api/developer/ext/v1/activities'
# Parameters for EngageNet
params = {
    "endpoint": endpoint,
    'host': devHost,
    'token': cred['devToken'],
    'method': 'GET',
    'request': {}
}

t = EngageNet(**params).run()
j = json.dumps(t,sort_keys=True, indent=4, separators=(",", ': '))
print j

