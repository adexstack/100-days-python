from speed_twitter_bot import InternetSpeedTwitterBot

TWITTER_EMAIL = ""
TWITTER_PASSWORD = ""

speed_twitter = InternetSpeedTwitterBot()
speed_twitter.get_internet_speed()
speed_twitter.tweet_at_provider()
#speed_twitter.tweet_at_provider()