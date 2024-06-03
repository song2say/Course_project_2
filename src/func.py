import json
from datetime import datetime

def get_json(path='operations.json'):
    with open(path, encoding='utf-8') as file:
        data = json.load(file)
    return data

