

#Importing the required modules
import snscrape.modules.twitter as sntwit
import pymongo as pm
import pandas as pd
from pymongo import MongoClient
import streamlit as st

#twitter data scrapping as per keyword or hashtag

st.header("TWITTER SCRAPING USING SN SCRAPE")
data1=[]
with st.form("my_form"):
    default_since = '2020-01-01'
    default_until = '2023-01-31'
    since = st.text_input('Enter the start_date :',default_since) 
    until = st.text_input('Enter the end_date :', default_until)
    search= st.text_input("Enter a keyword or hashtag: ")
    number_tweets=st.slider('drag the slider to scrape the no of tweets you want to scrape:', 0,1000,100)
    num_tweet=int(number_tweets)
    submit=st.form_submit_button("Submit")
    if submit:
        arguments = (f'{search} since:{since} until:{until}')
        for i,tweet in enumerate(sntwit.TwitterSearchScraper(arguments).get_items()):
            if i>num_tweet:
                break
            data1.append([tweet.date,tweet.id,tweet.url,tweet.content,tweet.user.username,tweet.replyCount,tweet.retweetCount,tweet.lang,tweet.likeCount,tweet.source])                                   
df=pd.DataFrame(data1,columns=["Date","ID","URL","Content","User_name","Reply_count","Retweet_count","Language","Likes_count","Source"])
st.write(df)
with st.form("form"):
    st.write("Press Enter to upload the data into database:")
    Enter=st.form_submit_button("Enter")
    if Enter:
        client = pm.MongoClient("mongodb://localhost:27017") 
        mydb = client["twitter_database"]   
        mycoll = mydb[f"{search}_collection"] 
        data_dict = df.to_dict("records")
        mycoll.insert_one({"index":f"{search}","data":data_dict})
        st.success("Uploaded Successfully!",icon='✅') 

st.write("Download the file in the format you want:")
st.write("Download in csv format")
#defining the funtion to conver the dataset into csv format        
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')

csv = convert_df(df)

st.download_button(
"Press to Download the Dataframe to CSV file format",
csv,
f"{search}_tweet.csv",
"text/csv",
key='download-csv'
)
#defining the funtion to conver the dataset into json format
st.write("Download in json format")
def convert_json(df):
    return df.to_json().encode('utf-8')

json = convert_json(df)
st.download_button(
"Press to Download the Dataframe to JSON file format",
json,
f"{search}_tweet.json",
"text/json",
key='download-json'
)


