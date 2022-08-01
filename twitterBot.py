from numpy import percentile
import tweepy
import time

import authCredentials

import colorDetection

from aiModel import get_image_from_url

consumer_key = authCredentials.API_key
consumer_secret_key = authCredentials.API_secret_key
access_token = authCredentials.access_token
access_token_secret = authCredentials.access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

FILE_NAME = 'last.txt'

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

def reply():
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode="extended")
    for tweet in reversed(tweets):
        if tweet.in_reply_to_status_id:
            og_tweet = api.get_status(tweet.in_reply_to_status_id, tweet_mode="extended")
            if 'media' in og_tweet.entities:
                print(og_tweet.entities)
                for image in  og_tweet.entities['media']:
                    image_link = image['media_url'] + ":small"
                    get_image_from_url(image_link)

                print("Tweet Detected!: " + str(tweet.id) + " - " + tweet.full_text.lower())
                if (colorDetection.percent_grey > 0.636):
                    tweet_message = ' The image attached to the original tweet is fabricated or has been manipulated with a certanity of ' + str(colorDetection.percentCertanity) + '% ' + colorDetection.emoji + '\n\n' + '⚠️ This bot is still under development, please do not take any result as a concrete statement ⚠️'
                elif (colorDetection.percent_grey <= 0.636):
                    tweet_message = ' The image attached to the original tweet is authentic (minimal manipulation) with a certanity of ' + str(colorDetection.percentCertanity) + '% ' + colorDetection.emoji + '\n\n' + '⚠️ This bot is still under development, please do not take any result as a concrete statement ⚠️'
                print(tweet.id)
                api.update_status('@' + tweet.user.screen_name + tweet_message, tweet.id)

            elif 'media' not in og_tweet.entities:
                print(og_tweet.entities)
                print("No Image!: " + str(tweet.id) + " - " + tweet.full_text.lower())
                ###api.update_status('@' + tweet.user.screen_name + " This tweet doesn't include an image that can be analyzed for manipulation ⚠️", tweet.id)

        api.create_favorite(tweet.id)
        store_last_seen(FILE_NAME, tweet.id)

while True:
    try:
        reply()
        time.sleep(30)
    except: 
            continue
