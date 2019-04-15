class User:
    def __init__(self, id):
        self.id = id 
        self.follow = set()
        self.followers = set()
        self.tweets = []
        self.newsfeed = []

class Tweet:
    count = 0
    @classmethod
    def create(cls, user_id, tweet_text):
         # This will create a new tweet object,
         # and auto fill id
         cls.user_id = user_id 
         cls.id = cls.count 
         cls.tweet_text = tweet_text
         return Tweet()



class MiniTwitter:
    
    def __init__(self):
        # do intialization if necessary
        self.users = {}

    """
    @param: user_id: An integer
    @param: tweet_text: a string
    @return: a tweet
    """
    def postTweet(self, user_id, tweet_text):
        # write your code here
        if user_id not in self.users:
            self.users[user_id] = User(user_id)
        user = self.users[user_id]
        tweet = Tweet(user_id, tweet_text)

        user.tweets.append(tweet)
        user.newsfeed.append(tweet)
        for follower_id in user.followers:
            follower = self.users[follower_id]
            follower.newsfeed.append(tweet)
        return tweet

    """
    @param: user_id: An integer
    @return: a list of 10 new feeds recently and sort by timeline
    """
    def getNewsFeed(self, user_id):
        # write your code here
        if user_id not in self.users:
            self.users[user_id] = User(user_id)        
        news = []
        user_news = self.users[user_id].newsfeed 
        for i in range(len(user_news) - 1, max(-1, len(user_news) - 11), -1):
            news.append(user_news[i])
        return news 
    """
    @param: user_id: An integer
    @return: a list of 10 new posts recently and sort by timeline
    """
    def getTimeline(self, user_id):
        # write your code here
        if user_id not in self.users:
            self.users[user_id] = User(user_id)
        
        
        timeline = []
        user_tweets = self.users[user_id].tweets 
        for i in range(len(user_tweets) - 1, max(-1, len(user_tweets) - 11), -1):
            timeline.append(user_tweets[i])
        return timeline 
            

    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """
    def follow(self, from_user_id, to_user_id):
        # write your code here
        if from_user_id not in self.users:
            self.users[from_user_id] = User(from_user_id)
        user = self.users[from_user_id]
        user.follow.add(to_user_id)
        
        if to_user_id not in self.users:
            self.users[to_user_id] = User(to_user_id)
        self.users[to_user_id].followers.add(from_user_id)
        
        for tweet in self.users[to_user_id].tweets:
            user.newsfeed.append(tweet)
        user.newsfeed.sort(key=lambda x:x.id)

    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """
    def unfollow(self, from_user_id, to_user_id):
        # write your code here
        self.users[from_user_id].follow.remove(to_user_id)
        self.users[to_user_id].followers.remove(from_user_id)
        
        arr = []
        for tweet in self.users[from_user_id].newsfeed:
            if tweet.user_id != to_user_id:
                arr.append(tweet)
        self.users[from_user_id].newsfeed = arr
        self.users[from_user_id].newsfeed.sort(key=lambda x:x.id)

        
        
        
        
        
        