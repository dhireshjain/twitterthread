from flask import Blueprint, render_template

from website.bo import twitter_thread

mod = Blueprint('general', __name__, url_prefix='/')


@mod.route('/')
def home():
    return render_template('home.html', )


@mod.route('/tweet/<tweet_id>')
def thread(tweet_id):
    tweet = twitter_thread.get_tweet(tweet_id)
    tree = twitter_thread.build_tree(tweet)
    return render_template(
        'tweet.html',
        tweet=tweet,
        tree=tree
    )
