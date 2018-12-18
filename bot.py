'''
Twitter Bot
Author : Millennium Bismay
NIT Rourkela

'''

import tweepy#version 3.6
import time

print("Hello! This is a bot")

#These can be found on Twitter Developers API account

CONSUMER_KEY='7mxcKkE0q5kLyLEda0RkigrBf'
CONSUMER_SECRET='yaN7OnL7hcZCq1I93LghsFZaumYlbTfeFadDWtX5yxzCca6iHSwtC'
ACCESS_KEY='774348230012252160-7zF17Mmob5Y1IfcxySASDSAVfBGjiL1ZKRZ6A'
ACCESS_SECRET='eqg8aUswlY3j3c48bgmDaFlgtTdadW1d54ogHtrQ1olO50Mq4j'

auth=tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
api=tweepy.API(auth)

#we need to store the id of the last checked tweet. This needs to be updated each time a tweet is checked.
fname='last_seen_id.txt'

def retrieve_last_seen_id(file_name):
	#This function retrieves the last seen id t=each time this program starts
	f_read=open(file_name,'r')
	last_seen_id=int(f_read.read().strip())
	f_read.close()
	return last_seen_id

def store_last_seen_id(last_seen_id,file_name):
	#This function stores the id of the current tweet
	f_write=open(file_name,'w')
	f_write.write(str(last_seen_id))
	f_write.close()
	return

def reply_to_tweets():
	print('retrieving and replyig to tweets...')
	#first tweet id = 958330714029678593 -- different for each individual

	last_seen_id=retrieve_last_seen_id(fname)

	mentions=api.mentions_timeline(last_seen_id)#this argument starts the checking from the last checked tweet id stored in the last_seen_id.txt file
	#mentions=api.mentions_timeline()#gives all the tweets done by the account

	#reversed list is used in order to respond in the upside down order as the oldest tweet should be responded first
	for mention in reversed(mentions):
		print(str(mention.id)+" : "+mention.text)

		last_seen_id=mention.id
		store_last_seen_id(last_seen_id,fname)

		if 'congratulations' in mention.text.lower():
			print('found congratulations!')
			print('responding back...')
			api.update_status('@'+mention.user.screen_name+' Thank you!!',mention.id)

while True:
	reply_to_tweets()
	time.sleep(15)#checks the twitter handle each 15 second
