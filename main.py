from SubredditPuller import SubredditPuller
import pandas as pd
from fastai import *

s = SubredditPuller()
types = ['infj', 'infp', 'intj', 'intp', 'istj', 'istp', 'isfp', 'isfj',
         'enfj', 'enfp', 'entj', 'entp', 'estj', 'estp', 'esfp', 'esfj']


def download_data():
    # Create DataFrames for each subreddit and their posts
    subreddit_df = pd.DataFrame(columns=['type', 'title', 'text'])
    for type in types:
        posts = s.pull_subreddit(type, limit=1000)

        print(type)
        for subm in posts:
            append_df = pd.DataFrame([[type, subm.title, subm.selftext,]])

            subreddit_df = pd.concat([subreddit_df, append_df])
            subreddit_df.to_csv('mbti_subreddit_data.csv')


def load_data():
    return pd.read_csv('mbti_subreddit_data.csv')


subreddit_df = load_data()

data_lm = TextLMDataBunch.from_csv
