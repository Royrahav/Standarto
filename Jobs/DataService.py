import pandas as pd
from Jobs.NightJob import NightJob
import numpy as np


class DataService:

    def __init__(self):
        nj = NightJob()
        self.m_ratings_df, self.m_basics_df = nj.act()
        self.m_ratings_df = self.m_ratings_df[self.m_ratings_df['numVotes'] > 10000]
        self.m_basics_df = self.m_basics_df[self.m_basics_df['titleType'] == 'movie']
        self.m_main_df = self.m_ratings_df.merge(self.m_basics_df, how="inner", on="tconst")
        print(self.m_main_df[['primaryTitle', 'startYear', 'averageRating']])

        self.m_main_df.to_csv(r'E:\Roy\Other\readme.txt', header=None, index=None, sep='\t', mode='a')

    def get_basics_df(self):
        return self.m_basics_df

    def get_ratings_df(self):
        return self.m_ratings_df

    # dataframes
    m_basics_df = pd.DataFrame()
    # m_akas_df = None
    m_ratings_df = pd.DataFrame()
    m_main_df = pd.DataFrame()
