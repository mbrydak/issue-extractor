import csv
import json

import requests

import pandas as pd

parameters = {"since": "2020-04-22", "state": "all"}

response = requests.get(
    'https://api.github.com/repos/protego-safe/specs/issues', params=parameters)

data = response.json()

df = pd.read_json(data)
df.to_csv(r'result.csv', index=None)
