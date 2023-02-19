#import necessary libraries and packages
import snscrape.modules.twitter as sntwitter
import pandas as pd
import streamlit as st
import datetime
import pymongo
import time

# req variables to connect mongodb
client = pymongo.MongoClient("mongodb://localhost:27017/")  #to connect mongodb
mydb = client["Twitter_Db"]    # to create db
tweets_df = pd.DataFrame()
dfm = pd.DataFrame()
st.write("# Twitter data scraping")
option = st.selectbox('How would you like the data to be searched?',('Keyword', 'Hashtag'))
word = st.text_input('Please enter a '+option, 'Example: elon musk')
start = st.date_input("Select the start date", datetime.date(2022, 1, 1),key='d1')
end = st.date_input("Select the end date", datetime.date(2023, 1, 1),key='d2')
tweet_c = st.slider('How many tweets to scrape', 0, 1000, 5)
tweets_list = []

# scraping data using TwitterSearchScrapper and TwitterHashtagScraper
if word:
    if option=='Keyword':
        for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f'{word} + since:{start} until:{end}').get_items()):
            if i>tweet_c:
                break
            tweets_list.append([ tweet.id, tweet.date,  tweet.content, tweet.lang, tweet.user.username, tweet.replyCount, tweet.retweetCount,tweet.likeCount, tweet.source, tweet.url ])
        tweets_df = pd.DataFrame(tweets_list, columns=['ID','Date','Content', 'Language', 'Username', 'ReplyCount', 'RetweetCount', 'LikeCount','Source', 'Url'])
    else:
        for i,tweet in enumerate(sntwitter.TwitterHashtagScraper(f'{word} + since:{start} until:{end}').get_items()):
            if i>tweet_c:
                break
            tweets_list.append([ tweet.id, tweet.date,  tweet.content, tweet.lang, tweet.user.username, tweet.replyCount, tweet.retweetCount,tweet.likeCount, tweet.source, tweet.url ])
        tweets_df = pd.DataFrame(tweets_list, columns=['ID','Date','Content', 'Language', 'Username', 'ReplyCount', 'RetweetCount', 'LikeCount','Source', 'Url'])
else:
    st.warning(option,' cant be empty', icon="⚠️")

# download csv
st.cache_data  #Note: Cache, the conversion  is to prevent computation on every re run
def convert_df(df):
    return df.to_csv().encode('utf-8')

if not tweets_df.empty:
    csv = convert_df(tweets_df)
    st.download_button(label="Download data as CSV",data=csv,file_name='Twitter_data.csv',mime='text/csv',)

    # download json
    json_string = tweets_df.to_json(orient ='records')
    st.download_button(label="Download data as JSON",file_name="Twitter_data.json",mime="application/json",data=json_string,)

# upload data to db
    if st.button('Upload Tweets to MONGODB'):
        coll=word
        coll=coll.replace(' ','_')+'_Tweets'
        mycoll=mydb[coll]
        dict=tweets_df.to_dict('records')
        if dict:
            mycoll.insert_many(dict)
            ts = time.time()
            mycoll.update_many({}, {"$set": {"KeyWord_or_Hashtag": word+str(ts)}}, upsert=False, array_filters=None)
            st.success('Successfully uploaded to MONGODB', icon="✅")
        else:
            st.warning('Cant upload because there are no tweets', icon="⚠️")
        # shows tweets
        if st.button('Show Tweets'):
            st.write(tweets_df)




