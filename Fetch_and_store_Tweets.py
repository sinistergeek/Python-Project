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
