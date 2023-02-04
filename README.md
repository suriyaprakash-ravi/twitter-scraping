# twitter-scraping
Scraping the details from twitter using snscraping

To run the following code:

Go to anaconda cmd in windows

type cd {file path where the script is saved}

type streamlit run twitter_scrape.py

The whole code contains the details of scraping the data from twitter using sncrape,then uploading the scraped data into mongodb,then downloading the dataset in csv and json format

The first block contains importing the modules which are all required to scrape the data.

st.header used to give a header to the webpage

The second block of code is a function for twiterscraping.we are passing the three inputs which is given by the user into one argument,then we are passing the arguments into the snscrape module to scrape the data,then storing the data into one dataframe using pandas,by providing the column names.

The third block is for establishing connection with mongodb database and store all the data from the above function in tweet database in twiter collection. The data is only uploaded if the user clicks enter button.

The fourth block of code is about to download the dataset in the format of csv and json.


