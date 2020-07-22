import json

import requests

request = requests.get('https://api.github.com/repos/protego-safe/specs/issues?state=all&since=2020-04-22')

request_json = request.json()
print(request_json)
