import os
import sys
child_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(child_dir, '..'))
sys.path.append(parent_dir)
import base64
import json
import tmeapi
import urllib.error
import urllib.request

input = json.loads(base64.standard_b64decode(sys.argv[1]))
input['data']['Token'] = input['credentials']['token']

client = tmeapi.Client(input['credentials']['token'], input['credentials']['secret'])
print(client.calculate_signature(input['uri'], input['data']).decode("utf-8"))
