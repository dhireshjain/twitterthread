import os
import twitter


TWITTER_KEY = os.environ["TWITTER_KEY"]
TWITTER_SECRET = os.environ["TWITTER_SECRET"]
TWITTER_TOKEN = os.environ["TWITTER_TOKEN"]
TWITTER_TOKEN_SECRET = os.environ["TWITTER_TOKEN_SECRET"]

api = twitter.Api(
    consumer_key=TWITTER_KEY,
    consumer_secret=TWITTER_SECRET,
    access_token_key=TWITTER_TOKEN,
    access_token_secret=TWITTER_TOKEN_SECRET,
    sleep_on_rate_limit=True,
    tweet_mode="extended",
)


def get_tweet(tweet_id):
    return api.GetStatus(status_id=tweet_id, include_entities=True)


def get_replies(tweet):
    username = tweet.user.screen_name
    replies = api.GetSearch(
        term=f"to:{username}", since_id=tweet.id, count=100
    )
    return list(filter(lambda t: t.in_reply_to_status_id == tweet.id, replies))
