import json
import pandas as pd 
import os

if not os.path.exists("parsed_files"):
	os.mkdir("parsed_files")

df = pd.DataFrame()

f = open("json_files/tmdb602561.json", "r")
json_data = json.load(f)

df = df.append({
	'adult': json_data['adult'],
	'backdrop_path': json_data['backdrop_path'],
	'belongs_to_collection': json_data['belongs_to_collection'],
	'budget': json_data['budget'],
	'genres': json_data['genres'],
	'homepage': json_data['homepage'],
	'id': json_data['id'],
	'imdb_id': json_data['imdb_id'],
	'original_language': json_data['original_language'],
	'original_title': json_data['original_title'],
	'overview': json_data['overview'],
	'popularity': json_data['popularity'],
	'poster_path': json_data['poster_path'],
	'production_companies': json_data['production_companies'],
	'production_countries': json_data['production_countries'],
	'release_date': json_data['release_date'],
	'revenue': json_data['revenue'],
	'runtime': json_data['runtime'],
	'spoken_languages': json_data['spoken_languages'],
	'status': json_data['status'],
	'tagline': json_data['tagline'],
	'title': json_data['title'],
	'video': json_data['video'],
	'vote_average': json_data['vote_average'],
	'vote_count': json_data['vote_count']
	}, ignore_index=True)

df.to_csv("parsed_files/tmdb_dataset.csv")

# print(json_data['adult'])
# print(json_data['backdrop_path'])
# print(json_data['belongs_to_collection'])
# print(json_data['budget'])
# print(json_data['genres'])
# print(json_data['homepage'])
# print(json_data['id'])
# print(json_data['imdb_id'])
# print(json_data['original_language'])
# print(json_data['original_title'])
# print(json_data['overview'])
# print(json_data['popularity'])
# print(json_data['poster_path'])
# print(json_data['production_companies'])
# print(json_data['production_countries'])
# print(json_data['release_date'])
# print(json_data['revenue'])
# print(json_data['runtime'])
# print(json_data['spoken_languages'])
# print(json_data['status'])
# print(json_data['tagline'])
# print(json_data['title'])
# print(json_data['video'])
# print(json_data['vote_average'])
# print(json_data['vote_count'])



