from twitter import *
from gi.repository import Notify

# Initialize
Notify.init("Twitter Notifications")

# Access Token, Access Key, Consumer Secret, Consumer Key
token = "Access Token Here"
token_key = "Access Key Here"
con_secret = "Consumer Key Here"
con_secret_key = "Consumer Secret Here"

# Setup authorization OAuth connection
auth=OAuth(token, token_key, con_secret, con_secret_key)

# Setup the twitter stream - user stream
twitter_userstream = TwitterStream(auth=auth, domain='userstream.twitter.com')

# Privacy?
privacy = True

#iterate through entire list of stream input
for a in twitter_userstream.user():
    if 'unfavorite' in str(a):
        try:
            msg = a
            # We only want to show if someone favs my stuff
            if int(msg["target_object"]["user"]["id"]) == TWITTER ID HERE:
                name = msg["source"]["name"]+" unliked your tweet"
                tweet = "Tweet: "+msg["target_object"]["text"]
                Notify.Notification.new(name, tweet, "/root/Desktop/twitter-128.png").show()
        except:
            pass
    elif 'favorite' in str(a):
        try:
            msg = a
            # We only want to show if someone unfavs my stuff
            if int(msg["target_object"]["user"]["id"]) == TWITTER ID HERE:
                name = msg["source"]["name"]+" liked your tweet"
                tweet = "Tweet: "+msg["target_object"]["text"]
                Notify.Notification.new(name, tweet, "/root/Desktop/twitter-128.png").show()
        except:
            pass

    if 'retweeted_status' in str(a):
        try:
            msg = a
            # We only want to show if someone retweets my stuff
            if int(msg["retweeted_status"]["user"]["id"]) == TWITTER ID HERE:
                name = msg["user"]["name"]+" retweeted you"
                tweet = "Tweet: "+msg["text"]
                Notify.Notification.new(name, tweet, "/root/Desktop/twitter-128.png").show()
        except:
            pass

    elif 'delete' in str(a):
        try:
            msg = a
            # We only want to show if someone unfavs my stuff
            if int(msg["status"]["user_id"]) != TWITTER ID HERE:
                Notify.Notification.new(msg["status"]["user_id"]+" unretweeted you", "Tweet: UNKNOW TWEET", "/root/Desktop/twitter-128.png").show()
        except:
            pass

    if 'direct_message' in str(a):
        try:
            msg = a
            name = msg['direct_message']['sender']['name'] + " sent you a direct message"
            if privacy:
                text = "Message: EnCrPtEd MesSaGe - PrIvAcY iS oN"
            else:
                text = "Message: "+msg['direct_message']['text']
            Notify.Notification.new(name, text, "/twitter-128.png").show()
        except:
            pass
