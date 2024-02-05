def list_top_users(db):
    n = input("Enter the number of top users to list: ")
    try:
        n = int(n)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    # Aggregate to find top n users based on the maximum followersCount
    results = db.tweets.aggregate([
        {
            "$group": {
                "_id": "$user.username",
                "displayname": {"$first": "$user.displayname"},
                "followersCount": {"$max": "$user.followersCount"}  # Use $max to get the highest followersCount
            }
        },
        {"$sort": {"followersCount": -1}},  # Sort in descending order of followersCount
        {"$limit": n},
        {
            "$project": {
                "_id": 0,
                "username": "$_id",
                "displayname": 1,
                "followersCount": 1
            }
        }
    ])

    results = list(results)
    for user in results:
        print(f"Username: {user['username']}\nDisplay Name: {user['displayname']}\nFollowers Count: {user['followersCount']}\n")

    if len(results):
        while True:
            user_id = input("Enter the username to see full information or q to exit: ").strip()
            if user_id == "q":
                return
            try:
                user = db.tweets.find_one({'user.username': user_id})["user"]
                keys = user.keys()
                print("*" * 20)
                for key in keys:
                    print(f"{key}: {user[key]}")
                print("*" * 20)
                break
            except:
                print("No user found with that username.")
    else:
        print("There are no users with such a high number of followers.")

if __name__ == "__main__":
    pass
