import tweepy
import time
import logging
from dotenv import load_dotenv
import os

# Load .env file to get credentials
load_dotenv("keys.env", encoding='utf-8')

# Set up logging for the script
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

def setup_env():
    """Creates keys.env file if it doesn't exist and explains setup to the user."""
    if not os.path.exists("keys.env"):
        print("Welcome to the Twitter Liker Script!")
        print("To use this script, you need to set up your Twitter API credentials.")
        print("Follow these steps:")
        print("1. Go to https://developer.twitter.com/en/apps")
        print("2. Create a new Twitter Developer App")
        print("3. Copy your API Key, API Secret, Access Token, and Access Token Secret")

        api_key = input("Enter your Twitter API Key: ")
        api_secret = input("Enter your Twitter API Secret: ")
        access_token = input("Enter your Twitter Access Token: ")
        access_token_secret = input("Enter your Twitter Access Token Secret: ")

        with open("keys.env", "w") as f:
            f.write(f"TWITTER_API_KEY=\"{api_key}\"\n")
            f.write(f"TWITTER_API_SECRET=\"{api_secret}\"\n")
            f.write(f"TWITTER_ACCESS_TOKEN=\"{access_token}\"\n")
            f.write(f"TWITTER_ACCESS_TOKEN_SECRET=\"{access_token_secret}\"\n")

        print("Setup complete! Your credentials are stored in keys.env. Restart the script.")
        exit()

# Function to authenticate Twitter API
def authenticate_twitter_api():
    try:
        # Retrieve credentials from environment variables
        api_key = os.getenv('TWITTER_API_KEY')
        api_secret = os.getenv('TWITTER_API_SECRET')
        access_token = os.getenv('TWITTER_ACCESS_TOKEN')
        access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

        # Set up the authentication
        auth = tweepy.OAuth1UserHandler(
            consumer_key=api_key,
            consumer_secret=api_secret,
            access_token=access_token,
            access_token_secret=access_token_secret
        )
        # Create the API client
        api = tweepy.API(auth, wait_on_rate_limit=True)
        logger.info("Authentication successful.")
        return api
    
    except Exception as e:
        logger.error(f"Error during authentication: {e}")
        raise

# Function to like a tweet by tweet ID
def like_tweet(api, tweet_id):
    try:
        api.create_favorite(tweet_id)
        logger.info(f"Successfully liked the tweet with ID: {tweet_id}")
    except tweepy.TooManyRequests:
        logger.error("Rate limit exceeded. Retrying after 15 minutes.")
        time.sleep(900)  # Sleep for 15 minutes before retrying
        like_tweet(api, tweet_id)
    except tweepy.Unauthorized:
        logger.error("Authentication failed. Please check your API credentials.")
    except tweepy.TweepyException as e:
        logger.error(f"Error liking the tweet: {e}")
        raise

# Main function to run the script
def main():
    # Example tweet ID to like
    tweet_id = 'YOUR_TWEET_ID'  # Replace with an actual tweet ID

    # Authenticate and interact with Twitter API
    try:
        api = authenticate_twitter_api()
        like_tweet(api, tweet_id)
    except Exception as e:
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    setup_env()  # This checks if keys.env exists
    main()
