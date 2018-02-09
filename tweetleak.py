import twitter
import re
import time
import urllib2
import urllib
from pastebin import PastebinAPI
import datetime
import getpass
import urllib2
import schedule

def gettwitterlinks():

	api = twitter.Api(consumer_key=' ',
	consumer_secret=' ',
	access_token_key='  ',
	access_token_secret='')

	statuses = api.GetUserTimeline(screen_name='@')
	[s.text for s in statuses]
	tweets = str(statuses)
	urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', tweets)
	listofurl = urls
	now = datetime.datetime.now()
	z = now.strftime("%d_%m_%y-%H")
	print ('Tweet Time :' + z)
	for x in urls:
		xx = x
	return listofurl
	


def fetchandcreatepastes(urllist):
	now = datetime.datetime.now()
	time = now.strftime("%d_%m_%y-%H")
	filename = time+'.txt'


	for x in urllist:
		try:

			response = urllib2.urlopen(x)
			html = response.read()
			#print html
			with open(filename,"a") as file:
				file.write('\n')
				file.write(('#')*100)
				file.write('\n')
				file.write(x)
				file.write('\n')
				file.write(('#')*100)
				file.write('\n')
				file.write(html)
				file.write('\n')
		except Exception as e:
			print e
def pushtopastebin():
	api_dev_key = ' '
	password = ' '
	username = ' '
	api_results_limit = 25
	api_user_key = ' '
	x = PastebinAPI()
	details = x.user_details(' ',
							' ')


	now = datetime.datetime.now()
	time = now.strftime("%d_%m_%y-%H")
	filename = time+'.txt'
	try:
		with open(filename,"a") as file:
			content = file.read()
 		x.paste(api_dev_key, content, api_user_key = api_user_key, paste_name = filename,
 					   paste_format = None, paste_private = 'private',
 					   paste_expire_date = 'N')
 	except Exception as e:
 		print e


def main():
	gettwitterlinks()
	newlist =gettwitterlinks()
	fetchandcreatepastes(newlist)
	pushtopastebin()




schedule.every(1).minutes.do(main)
print "Script is runnning bro :)"
while True:
    schedule.run_pending()
    time.sleep(1)
    print "Script is runnning bro :)"
