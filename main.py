from Src.Jobs.NightJob import NightJob
# import requests
# import patoolib
# import pandas as pd
# import json
# from imdb import Cinemagoer
#
##BASE = "https://imdb-api.com/API/"
##API_KEY = "k_bz2twne3"
##TYPE = "AdvancedSearch/"
##lastPage = 251
# COUNT = 250
# movieList = []
##ia = Cinemagoer()
##response = requests.get(BASE + TYPE + API_KEY +"?title_type=feature,tv_movie&user_rating=8.0,&release_date=1970-01-01,&num_votes=49999,&count=" + str(COUNT))
##while (len(response.json ()['results'])):
##    movieList.extend(response.json()['results'])
##    response = requests.get(BASE + TYPE + API_KEY + "?title_type=feature,tv_movie&user_rating=8.0,&release_date=1970-01-01,&num_votes=49999,&count=" + str(COUNT) + ",&start=" + str(lastPage) + "&ref_=adv_nxt")
##    lastPage += COUNT
##
##my_json = response.json()
##print(len(my_json['results']))
##for x in movieList:
##    print(x['imDbRating'] + '->' + x['imDbRatingVotes'])
#
# ratingsurl = 'https://datasets.imdbws.com/title.ratings.tsv.gz'
##moviessurl = 'https://datasets.imdbws.com/title.akas.tsv.gz'
# basicsurl = 'https://datasets.imdbws.com/title.basics.tsv.gz'

# ratingsRead = requests.get(ratingsurl, allow_redirects=True)
# moviesRead = requests.get(moviessurl, allow_redirects=True)
# basicsRead = requests.get(basicsurl, allow_redirects=True)

# open('E:\\Roy\\Other\\title.ratings.tsv.gz', 'wb').write(ratingsRead.content)
# ratingsDf = pd.read_csv('E:\\Roy\\Other\\title.ratings.tsv.gz', compression='gzip', header=0, sep='\t', quotechar='"', error_bad_lines=False)

# open('E:\\Roy\\Other\\title.akas.tsv.gz', 'wb').write(moviesRead.content)
# moviesDf = pd.read_csv('E:\\Roy\\Other\\title.akas.tsv.gz', compression='gzip', header=0, sep='\t', quotechar='"', error_bad_lines=False)

# open('E:\\Roy\\Other\\title.basics.tsv.gz', 'wb').write(basicsRead.content)
# basicsDf = pd.read_csv('E:\\Roy\\Other\\title.basics.tsv.gz', compression='gzip', header=0, sep='\t', quotechar='"', error_bad_lines=False)
#
# rslt_df = ratingsDf[(ratingsDf['averageRating'] > 7.0) & (ratingsDf['numVotes'] > 50000)]
#
# moviesList = []
# for titleId in rslt_df['tconst']:
#    moviesList.append((basicsDf['tconst'] == titleId) & (moviesDf['region'] == 'US') & (basicsDf['year'] > )]['title'])
# print('\nResult dataframe :\n', rslt_df)
# print('\nMovies List :\n', moviesList)
# print (df.head(10))

nightJob = NightJob()
print(nightJob.CheckDateOfToday())
