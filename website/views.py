from flask import Flask, render_template
from .bo import twitter_thread

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html', )


@app.route('/tweet/<tweet_id>')
def thread(tweet_id):
    tweet = twitter_thread.get_tweet(tweet_id)
    tree = twitter_thread.build_tree(tweet)
    return render_template(
        'tweet.html',
        tweet=tweet,
        tree=tree
    )
