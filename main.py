import requests
import json
from imdb import Cinemagoer
import urllib

BASE = "https://imdb-api.com/API/"
API_KEY = "k_bz2twne3"
TYPE = "AdvancedSearch/"
lastPage = 251
COUNT = 250
movieList = []
ia = Cinemagoer()
response = requests.get(BASE + TYPE + API_KEY +"?title_type=feature,tv_movie&user_rating=8.0,&release_date=1970-01-01,&num_votes=49999,&count=" + str(COUNT))
while (len(response.json ()['results'])):
    movieList.extend(response.json()['results'])
    response = requests.get(BASE + TYPE + API_KEY + "?title_type=feature,tv_movie&user_rating=8.0,&release_date=1970-01-01,&num_votes=49999,&count=" + str(COUNT) + ",&start=" + str(lastPage) + "&ref_=adv_nxt")
    lastPage += COUNT

my_json = response.json()
print(len(my_json['results']))
for x in movieList:
    print(x['imDbRating'] + '->' + x['imDbRatingVotes'])

