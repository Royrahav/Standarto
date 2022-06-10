import pandas as pd
from Jobs.NightJob import NightJob

class DataService:

    def __init__(self):
        nj = NightJob()
        self.m_ratings_df, self.m_basics_df = nj.act()
        self.m_ratings_df = self.m_ratings_df[self.m_ratings_df['numVotes'] > 10000]
        m_main_df = DataFrame({"title_id": [], "title": [], "rating": [], "numVotes": []})

    def get_basics_df(self):
        return self.m_basics_df

    def get_ratings_df(self):
        return self.m_ratings_df

    # dataframes
    m_basics_df = pd.DataFrame()
    # m_akas_df = None
    m_ratings_df = pd.DataFrame()
    m_main_df = pd.DataFrame()
