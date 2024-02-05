def get_tweet_details(db, results):
    if len(results):
        while True:
            # Ask the user to select a tweet
            tweed_id = input("Enter the tweet id to see all fields or q to exit: ")
            print()

            if tweed_id == "q":
                return
            
            try:
                tweed_id = int(tweed_id)
            except ValueError:
                print("Tweed id format is invalid")
                print()
                continue


            try:
                # Retrieve and print all fields of the selected user
                tweet = db.tweets.find_one({'id': tweed_id})
                keys = tweet.keys()

                print("="*50)
                for key in keys:
                    if key == "user":
                        for user_key in tweet[key].keys():
                            print('  '+f"{user_key}: {tweet[key][user_key]}")
                        continue
                    print(f"{key}: {tweet[key]}")
                print("="*50)
                break
            except:
                print("There are no tweets with such tweet id.")
    else:
        print("There are no tweets that contain the word(s) searched")
