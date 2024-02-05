# Author: Nick Shan
# Date: 16/11/2020

from tweets_detail_prompt import get_tweet_details

def list_top_tweets(db):
    while True:
        print("\nHow you would like to sort: ")
        print("1. Retweet Count")
        print("2. Like Count")
        print("3. Quote Count")
        print("4. Exit")
        field = input("Enter an option number: ")

        if field == "1":
            field = "retweetCount"
            break
        if field == "2":
            field = "likeCount"
            break
        if field == "3":
            field = "quoteCount"
            break
        if field == "4":
            return
        else:
            print("Invalid option. Please try again.")


    n = int(input("Enter the number of tweets: "))

    # Find the top n tweets based on the selected field
    results = db.tweets.find().sort([(field, -1)]).limit(n)
    results = list(results)

    # Print the id, date, content, and username of each matching tweet
    for tweet in results:
        print("*"*20)
        print(f"ID: {tweet['id']}\nDate: {tweet['date']}\nContent: {tweet['content']}\nUsername: {tweet['user']['username']}\n{field}: {tweet[f'{field}']}")
        print("*"*20)
        print()
    
    get_tweet_details(db, results)