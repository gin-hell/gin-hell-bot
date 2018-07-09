
import tweepy
import markovify

auth = tweepy.OAuthHandler("fthFGXpbNlsYEiHV95atvZ19r", "lGCI06v9idLYM7fsfrKZzmihClq8DWdkIjqTzSU6qbxUoW4ehu")
auth.set_access_token("975540979565514752-uNy313xfu13C3zatFELPS8ZviHEfn7Q", "PLKdzn5LekDulr2X0sayAOgJGHO4a6tOvMoqJID10FOBp")

api = tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):

	def on_status(self, status):
		print(status.text)
		with open("tweets.txt", "a") as text_file:
			text_file.write("\n"+status.text.encode("utf8"))
		with open("tweets.txt") as f:
			text = f.read()

		text_model = markovify.Text(text)
		tweet_text = text_model.make_short_sentence(140)
		
		if tweet_text.split()[0] != "@":
			print(tweet_text)
			api.update_status(""+tweet_text+"")

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener = myStreamListener, tweet_mode="extended")

myStream.filter(follow=['3041956282'])