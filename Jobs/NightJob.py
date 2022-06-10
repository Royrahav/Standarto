from datetime import datetime, date, timedelta
import requests
import GlobalDefinitions.GlobalDefinitions as gd
from Jobs.Job import Job
import pandas as pd


class NightJob(Job):

    def __init__(self):
        pass

    def check_date_of_today(self) -> bool:
        return self.m_last_update == self.m_date_of_today

    @staticmethod
    def get_request_data(data):
        return requests.get(data, allow_redirects=True)

    @staticmethod
    def open_file_path(path, content):
        open(path, 'wb').write(content)

    @staticmethod
    def read_data_frame(path):
        return pd.read_csv(path, compression='gzip', header=0, sep='\t', quotechar='"', error_bad_lines=False)

    def download_gz_files(self):
        # movies_read = self.get_request_data(self.m_title_akas_tsv_gz)
        basics_read = self.get_request_data(self.m_title_basics_tsv_gz)
        ratings_read = self.get_request_data(self.m_title_ratings_tsv_gz)

        # self.open_file_path(gd.gz_files_output_path + gd.title_akas_tsv_gz_name, movies_read.content)
        self.open_file_path(gd.gz_files_output_path + gd.title_ratings_tsv_gz_name, ratings_read.content)
        self.open_file_path(gd.gz_files_output_path + gd.title_basics_tsv_gz_name, basics_read.content)

    def create_data_frames(self):
        # m_akas_df = self.read_data_frame(gd.gz_files_output_path + gd.title_akas_tsv_gz_name)
        self.m_basics_df = self.read_data_frame(gd.gz_files_output_path + gd.title_basics_tsv_gz_name)
        self.m_ratings_df = self.read_data_frame(gd.gz_files_output_path + gd.title_ratings_tsv_gz_name)

    def act(self):
        if not self.check_date_of_today()\
                and self.m_basics_df\
                and self.m_ratings_df:
            pass
        else:
            self.download_gz_files()
            self.create_data_frames()

        return self.m_ratings_df, self.m_basics_df

    # date and time definitions
    m_last_update = date(2022, 6, 21)  # TODO: take this value from DB
    m_date_of_today = date.today()

    # gz file names
    # m_title_akas_tsv_gz = gd.data_sets_base_path + gd.title_akas_tsv_gz_name
    m_title_basics_tsv_gz = gd.data_sets_base_path + gd.title_basics_tsv_gz_name
    m_title_ratings_tsv_gz = gd.data_sets_base_path + gd.title_ratings_tsv_gz_name

    # dataframes
    m_basics_df = None
    # m_akas_df = None
    m_ratings_df = None
