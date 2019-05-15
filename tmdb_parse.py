import json


f = open("json_files/tmdb602561.json", "r")
json_data = json.load(f)
print(json_data['id'])
