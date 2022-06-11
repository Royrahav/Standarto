import pandas as pd
from Jobs.NightJob import NightJob
import os


class DataService:

    def __init__(self):
        nj = NightJob()
        self.m_ratings_df, self.m_basics_df = nj.act()
        self.filter_data_frames()
        self.create_main_data_frame()

    def get_basics_df(self):
        return self.m_basics_df

    def get_ratings_df(self):
        return self.m_ratings_df

    def get_main_dataframe(self):
        return self.m_main_df

    def filter_data_frames(self):
        self.m_ratings_df = self.m_ratings_df[self.m_ratings_df['numVotes'] > 10000]
        self.m_basics_df = self.m_basics_df[self.m_basics_df['titleType'] == 'movie']

    def create_main_data_frame(self):
        self.m_main_df = self.m_ratings_df.merge(self.m_basics_df, how="inner", on="tconst")
        self.m_main_df.drop(['titleType', 'originalTitle', 'isAdult', 'endYear', 'runtimeMinutes'], axis=1,
                            inplace=True)
        self.m_main_df.sort_values(by=['numVotes'], ascending=False, inplace=True)

    def create_csv_for_testing(self):
        if os.path.exists(r'E:\Roy\Other\readme.txt'):
            os.remove(r'E:\Roy\Other\readme.txt')

        f = open(r'E:\Roy\Other\readme.txt', "a")
        for key in self.m_main_df.keys():
            f.write(key + '\t')
        f.write('\n')
        f.close()
        self.m_main_df.to_csv(r'E:\Roy\Other\readme.txt', header=None, index=None, sep='\t', mode='a')

    # dataframes
    m_basics_df = pd.DataFrame()
    # m_akas_df = None
    m_ratings_df = pd.DataFrame()
    m_main_df = pd.DataFrame()
