TWITTER SCRAPING USING SNSCRAPE STREAMLIT
Scraping of Data's from Twitter with mongodb, streamlit using Snscrape.

Overview of the Twitter Scraping:

Created GUI using Streamlit
•	Create any keyword or hashtag to be searched
•	Enter an option keyword Eg: "elon musk"
•	Select a start and end date
•	Number of tweet to be scraped
•	Scrape data using TwitterSearchScraper and TwitterHashtagScraper.

After Scraping the data from twitter:

•	Upload collections in database shown
•	Download CSV and JSON
•	Database collection uploaded to MongoDB
•	Displayed all tweets

LIBRARIES AND PACKAGES TO BE INSTALLED AND IMPORTED:

•	Snscrape: import snscrape.modules.twitter as sntwitter
•	Pandas: import pandas as pd
•	Pymongo: import Pymongo
•	Datetime: import Datetime
•	Streamlit: import streamlit as st

Roadmap How it works:

•	I collected keyword, start date, end date, number of tweets from the user using Streamlit
•	The above lines used for scraping data using TwitterSearchScraper and TwitterHashtagscraper.
•	Created a dataframe to store entire scraped data
•	now download the scrape data in the form of JSON and CSV
•	A new collection will be created and data is uploaded into that collection.

PLACING MY SCREENSHOT HOW IT WORKS:
![Screenshot 2023-02-20 192849](https://user-images.githubusercontent.com/115634164/220131069-0666ac08-ce11-41fa-b5d9-b4e6bd585709.png)

 MY MONGODB COMPASS UPLOADED TWEETS:
![Screenshot 2023-02-20 193031](https://user-images.githubusercontent.com/115634164/220130874-82703cdc-d586-407d-af15-2f443b7e917d.png)

LINK TO VIEW IN YOUR BROWSER:

 Local URL: http://localhost:8501
 
 Network URL: http://192.168.0.100:8501
