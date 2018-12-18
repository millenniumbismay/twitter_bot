import tweepy
import time

print("Hello! This is a bot")

CONSUMER_KEY='7mxcKkE0q5kLyLExu0RkigrBf'
CONSUMER_SECRET='yaN7OnL7hcZCq1I93LghsFZaumYlbTfeFftX5yxzCca6iHSwtC'
ACCESS_KEY='774348230012252160-7zF17Mmob5Y1IfcxyVfBGjiL1ZKRZ6A'
ACCESS_SECRET='eqg8aUswlY3j3c48bgmDaFlgtT854ogHtrQ1olO50Mq4j'

auth=tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
api=tweepy.API(auth)

fname='last_seen_id.txt'

def retrieve_last_seen_id(file_name):
	f_read=open(file_name,'r')
	last_seen_id=int(f_read.read().strip())
	f_read.close()
	return last_seen_id

def store_last_seen_id(last_seen_id,file_name):
	f_write=open(file_name,'w')
	f_write.write(str(last_seen_id))
	f_write.close()
	return

def reply_to_tweets():
	print('retrieving and replyig to tweets...')
	#first tweet id = 958330714029678593

	last_seen_id=retrieve_last_seen_id(fname)

	mentions=api.mentions_timeline(last_seen_id)
	#mentions=api.mentions_timeline()

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
	time.sleep(15)