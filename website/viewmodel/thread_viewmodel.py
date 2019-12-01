class ThreadView:

    def __init__(self):
        self.tweet = None
        self.replies = [None]

    def get_tweet(self):
        return self.tweet

    def get_replies(self):
        return self.replies

    def set_tweet(self, tweet):
        self.tweet = tweet

    def set_replies(self, replies):
        self.replies = replies
