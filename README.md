
# TWITTER SCRAPING WITH MONGODB AND STREAMLIT

Scraping of Data's from Twitter with mongodb, streamlit using Snscrape.

Overview of the Twitter Scraping:

created GUI using Streamlit

1.create any keyword or hashtag to be searched

2.enter an option keyword Eg: "elon musk"

3.select a start and end date

4.number of tweet to be scraped

5.scrape data using TwitterSearchScraper and TwitterHashtagScraper.

After Scraping the data from twitter:

1.upload collections in database shown 

2.download CSV nad JSON

3.displayed all tweets

LIBRARIES AND PACKAGES TO BE INSTALLED AND IMPORTED:

Snscrape: import snscrape.modules.twitter as sntwitter

Pandas: import pandas as pandas

Pymongo: import Pymongo

Datetime: import Datetime     

Streamlit: import streamlit as st





## Roadmap How it works:
1. I collected keyword , Start date, end date, number of tweets from the user using Streamlit
2. The above lines used for scraping data using TwitterSearchScraper and TwitterHashtagscraper.
3. Created a dataframe to store entire scraped data
4. now download the scrape data in the form of JSON and CSV
5. A new collection will be created and data is uploaded into that collection.
## Screenshots

![App Screenshot](https://paste.pics/70488a0bf5897728ac9a55452f29649e)



## LINK TO VIEW IN YOUR BROWSER
Local URL: http://localhost:8501

Network URL: http://192.168.0.102:8501
