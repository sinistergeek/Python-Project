import tweepy
import csv

consumer_key=''
consumer_secret=''
access_token =''
access_token_secret = ''
hastag = ''

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
csvFile = open('tweets.csv','a')
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q=hastag,count=100,lang="en",sinc="2017-04-02").items():
    print(tweet.created_at,tweet.text)
    csvWriter.writerow([tweet.created_at,tweet.text.encode('utf-8')])
