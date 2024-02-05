from tweets_detail_prompt import get_tweet_details
import re

def search_tweets(db):
    # Ask the user for one or more keywords
    keywords_input = input("Enter one or more keywords: ").lower()
    keywords = keywords_input.split()
    print()

    # Generate regex patterns for each keyword
    regex_patterns = [f"(\\b{re.escape(keyword)}\\b|\\W{re.escape(keyword)}\\W|\\W{re.escape(keyword)}\\b|\\b{re.escape(keyword)}\\W)" for keyword in keywords]

    # Search for tweets that match all regex patterns
    results = db.tweets.find({
        "$and": [{"content": {"$regex": pattern, "$options": "i"}} for pattern in regex_patterns]
    })
    
    results = list(results)

    seen_combinations = set()
    for tweet in results:
        # Create a composite key for each tweet
        composite_key = (tweet['id'], tweet['date'], tweet['content'], tweet['user']['username'])

        if composite_key in seen_combinations:
            continue
        seen_combinations.add(composite_key)

        print("*" * 20)
        print(f"ID: {tweet['id']}\nDate: {tweet['date']}\nContent: {tweet['content']}\nUsername: {tweet['user']['username']}")
        print("*" * 20)
        print()

    get_tweet_details(db, results)