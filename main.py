from pymongo import MongoClient
import sys
# Import the list_top_tweets function
from list_top_tweets import list_top_tweets
from search_tweets import search_tweets  # Import the search_tweets function
from search_users import search_user  # Import the search_user function
from list_top_users import list_top_users  # Import the list_top_users function
from compose import compose_tweet  # import compose function


def main(port):
    # Create a connection to MongoDB
    client = MongoClient(f"mongodb://localhost:{port}")

    # Connect to the '291db' database
    db = client['291db']

    while True:
        # Prompt the user to select an option
        print("\nPlease select an option:")
        print("1. Search tweets")
        print("2. Search users")
        print("3. List top tweets")
        print("4. List top users")
        print("5. Compose tweet")
        print("6. Exit")
        option = input("Enter an option number: ")

        if option == "1":
            # Search for tweets that match all keywords
            search_tweets(db)
        elif option == "2":
            # Search for users that match a keyword
            search_user(db)
        elif option == "3":
            # List the top n tweets based on the selected field
            list_top_tweets(db)
        elif option == "4":
            # List the top n users based on the selected field
            list_top_users(db)
        elif option == "5":
            # compose tweet
            compose_tweet(db)
        elif option == "6":
            # Exit the program
            print("Exiting program...")
            break
        else:
            # Invalid option
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    # EXAMPLE: python3 main.py 27017
    port = sys.argv[1]
    # port = 41231
    main(port)
