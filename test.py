import requests

BASE = "https://imdb-api.com/API/"
API_KEY = "k_bz2twne3"
TYPE = "AdvancedSearch/"

response = requests.get(BASE + TYPE +API_KEY+"?title_type=feature,tv_movie&user_rating=8.0,&release_date=1970-01-01,&num_votes=49999,")
print(response.json())