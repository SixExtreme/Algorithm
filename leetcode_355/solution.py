from typing import Dict, List, Set


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweetMap: Dict[int, int] = dict()
        self.followMap: Dict[int, Set[int]] = dict()
        self.userTweetMap: Dict[int, List[int]] = dict()

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if userId not in self.userTweetMap:
            self.userTweetMap[userId] = []
        self.userTweetMap[userId].append(tweetId)
        self.tweetMap[tweetId] = len(self.tweetMap)

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        feed = [*self.userTweetMap.get(userId, [])]
        for followeeId in self.followMap.get(userId, set()):
            feed.extend(self.userTweetMap.get(followeeId, []))
        feed.sort(key=lambda tweetId: self.tweetMap[tweetId], reverse=True)
        return feed[:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId == followeeId:
            return
        if followerId not in self.followMap:
            self.followMap[followerId] = set()
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.followMap and followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)


def test_solution():
    twitter = Twitter()

    twitter.follow(1, 2)
    twitter.postTweet(1, 5)
    twitter.postTweet(2, 6)
    assert twitter.getNewsFeed(1) == [6, 5]

    twitter.unfollow(1, 2)
    assert twitter.getNewsFeed(1) == [5]


