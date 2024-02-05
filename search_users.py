import re
from pymongo import MongoClient

def search_user(db):
    keyword = input("Enter a keyword: ").strip()
    print()

    # Sanitize the keyword to escape special regex characters
    sanitized_keyword = re.escape(keyword)

    # Regular expression pattern to match the keyword with punctuation on both sides or no punctuation
    regex_pattern = f"(\\b{sanitized_keyword}\\b|\\W{sanitized_keyword}\\W|\\W{sanitized_keyword}\\b|\\b{sanitized_keyword}\\W)"

    # Search for tweets using regex
    results = db.tweets.aggregate([
        {
            "$match": {
                "$or": [
                    {"user.displayname": {"$regex": regex_pattern, "$options": "i"}},
                    {"user.location": {"$regex": regex_pattern, "$options": "i"}}
                ]
            }
        },
        {
            "$group": {
                "_id": "$user.username",
                "displayname": {"$first": "$user.displayname"},
                "location": {"$first": "$user.location"}
            }
        },
        {
            "$project": {
                "_id": 0,
                "username": "$_id",
                "displayname": 1,
                "location": 1
            }
        }
    ])

    results = list(results)
    for tweet in results:
        print(f"Username: {tweet['username']}\nDisplay Name: {tweet['displayname']}\nLocation: {tweet['location']}\n")

    if not results:
        print("No users found with the provided keyword.")
        return

    while True:
        user_id = input("Enter the username to see all fields or q to exit: ").strip()
        if user_id.lower() == "q":
            return

        user = db.tweets.find_one({'user.username': user_id}, {'user': 1})
        if user:
            print("*" * 20)
            for key, value in user['user'].items():
                print(f"{key}: {value}")
            print("*" * 20)
        else:
            print("No user found with the username:", user_id)

if __name__ == "__main__":
    # Connect to MongoDB (example: MongoClient('mongodb://localhost:27017/'))
    client = MongoClient('your_connection_string')
    db = client.your_database

    search_user(db)
