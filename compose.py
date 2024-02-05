# Author: Mehreen Naseer
# Date: 25/11/2020

from datetime import datetime, timezone

def compose_tweet(db):
    tweet_content = input("Enter tweet content: ")
    date = str(datetime.now(timezone.utc).isoformat())

    new_tweet = {
        "url": None,
        "date": date,  # assign current sys date
        "content": tweet_content,
        "renderedContent": None,
        "id": None,
        "user": {
            "username": "291user",
            "displayname": None,
            "id": None,
            "description": None,
            "rawDescription": None,
            "descriptionUrls": None,
            "verified": None,
            "created": None,
            "followersCount": None,
            "friendsCount": None,
            "statusesCount": None,
            "favouritesCount": None,
            "listedCount": None,
            "mediaCount": None,
            "location": None,
            "protected": None,
            "linkUrl": None,
            "linkTcourl": None,
            "profileImageUrl": None,
            "profileBannerUrl": None,
            "url": None,
        },
        "outlinks": None,
        "tcooutlinks": None,
        "replyCount": None,
        "retweetCount": None,
        "likeCount": None,
        "quoteCount": None,
        "conversationId": None,
        "lang": None,
        "source": None,
        "sourceUrl": None,
        "sourceLabel": None,
        "media": None,
        "retweetedTweet": None,
        "quotedTweet": None,
        "mentionedUsers": None,
    }

    db.tweets.insert_one(new_tweet)
    print("Tweet composed and added to the database.")
