import streamlit as st
import pandas as pd
import itertools
import snscrape.modules.twitter as sntwitter
import pymongo
import plotly.express as px

title = st.text_input('What do you want to Scrap from Twitter, Key in Value and Press Enter')
if st.button('Click Go'):

    myclient=pymongo.MongoClient("mongodb://127.0.0.1:27017")
    mydb = myclient["Twitter"]
    mycollection = mydb["TwitterCollection"]

    '# Twitter Data Scrapping'

    df = pd.DataFrame(itertools.islice(sntwitter.TwitterSearchScraper(title).get_items(),10))
    df["date"]=pd.to_datetime(df["date"])
    st.table(df[["date","replyCount","likeCount", "retweetCount", "renderedContent","source", "id", "url", "user","coordinates","place", "hashtags"]])
    df.columns
    df.reset_index(inplace=True)
    data_dict = df.to_dict("records")
    # Insert collection
    mycollection.insert_many(data_dict)