import tweepy

auth = tweepy.OAuthHandler("fthFGXpbNlsYEiHV95atvZ19r", "lGCI06v9idLYM7fsfrKZzmihClq8DWdkIjqTzSU6qbxUoW4ehu")
auth.set_access_token("975540979565514752-uNy313xfu13C3zatFELPS8ZviHEfn7Q", "PLKdzn5LekDulr2X0sayAOgJGHO4a6tOvMoqJID10FOBp")

api = tweepy.API(auth)

# myStreamListener = MyStreamListener()
# myStream = tweepy.Stream(auth = api.auth, listener = myStreamListener, tweet_mode="extended")

# myStream.filter(follow=['3041956282'])

id_array = api.friends_ids("3041956282")

for i in range(1, len(id_array)):
	print "loop "+str(i)
	# status = api.show_friendship(api.me.id, id_array[i])
	if api.get_user(id_array[i]).follow_request_sent:
		print "already requested: " + str(id_array[i])
	else:
		api.create_friendship(id_array[i])

# class MyStreamListener(tweepy.StreamListener):

# 	def on_status(self, status):
# 		print(status.text)