import json

def read_token(filename):
    with open(filename,'r') as json_file:
        data = json.load(json_file)
        return data['token']