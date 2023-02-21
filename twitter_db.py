#import necessary libraries and packages
import snscrape.modules.twitter as sntwitter
import pandas as pd
import pymongo
import streamlit as st
import datetime
import time

# required variables to connect MONGODB
client = pymongo.MongoClient("mongodb://localhost:27017/")  #to connect MONGODB
mydb = client["Twitter_user"]  # to create database
tweets_df = pd.DataFrame()
dfm = pd.DataFrame()
st.write("#Twitter Data Scraping")
option = st.selectbox("How would you like the data to be searched ?",("Keyword","Hashtag"))
word = st.text_input("Please enter a "+option, "elon musk")
start = st.date_input("select the start date",datetime.date(2022,1,1),key= "d1")
end = st.date_input("select the end date",datetime.date(2023,2,15),key= "d2")
tweet_s = st.slider("How many tweets to be scrape", 0, 1000, 5)
tweets_list = []


#the above variable fed to TwitterSearchScraper and twitterHashtagScraper
if word:
    if option =='Keyword':
       for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f'{word},since:{start} until:{end}').get_items()):
           if i>tweet_s:
               break
           tweets_list.append([tweet.id, tweet.date, tweet.content, tweet.lang, tweet.user.username, tweet.replyCount, tweet.retweetCount, tweet.likeCount, tweet.source, tweet.url])
           tweets_df = pd.DataFrame(tweets_list, columns=['ID', 'Date', 'Content', 'Language', 'Username', 'ReplyCount','RetweetCount', 'LikeCount', 'Source', 'Url'])
    else:
       for i, tweet in enumerate(sntwitter.TwitterHashtagScraper(f'{word},since:{start} until:{end}').get_items()):
           if i > tweet_s:
              break
           tweets_list.append([tweet.id, tweet.date, tweet.content, tweet.lang, tweet.user.username, tweet.replycount, tweet.retweetCount,tweet.likecount, tweet.source, tweet.url])
       tweets_df = pd.DataFrame(tweets_list,columns=["ID", "Date", "Content", "Language", "Username", "ReplyCount", "RetweetCount","LikeCount", "Source", "Url"])
else:
    st.warning(option,"cannot be empty",icon = "⚠️")

# DOWNLOAD AS CSV
st.cache_data # note: Cache the conversion to prevent computation on every rerun
def convert_df(df):
    return df.to_csv().encode("utf-8")

if not tweets_df.empty:
    csv = convert_df(tweets_df)
    st.download_button(label= "Download data as CSV", data= "csv", file_name= "Twitter_user.csv",mime= "text/csv",)

    # DOWNLOAD AS JSON
    json_string = tweets_df.to_json(orient= "records")
    st.download_button(label= "Download data as JSON", data = "json_string", file_name= "twitter_user.json",mime= "application/json",)

#upload data to MONGODB
if st.button('Upload Tweets to MONGODB'):
        coll=word
        coll=coll.replace(' ','_')+'_Tweets'
        mycoll=mydb[coll]
        dict=tweets_df.to_dict("records")
        if dict:
            mycoll.insert_many(dict)
            ts = time.time()
            mycoll.update_many({}, {"$set": {"Keyword_or_Hashtag": word+str(ts)}}, upsert= False, array_filters= None)
            st.success('Successfully uploaded to database', icon="✅")
        else:
            st.warning('Cant upload because there are no tweets', icon="⚠️")

# shows tweets
if st.button('shows Tweets'):
       st.write(tweets_df)


#display the documents in selected collection
if not dfm.empty:
    st.write(len(dfm),"Records Found")
    st.write(dfm)





