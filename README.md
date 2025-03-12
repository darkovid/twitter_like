# Twitter API Automation Script

## Overview
This script interacts with the Twitter API to authenticate a user and like a tweet using its Tweet ID. It demonstrates API authentication, error handling, and rate limit management.

## Features
- Authenticates with Twitter API using OAuth 1.0a.
- Likes a tweet by its Tweet ID.
- Handles API rate limits and authentication errors.
- Uses a `.env` file for securely storing API credentials.
- Includes logging for execution status.

## Requirements
- Python 3.x
- Twitter Developer Account with API access
- The following Python packages:
  - `tweepy`
  - `python-dotenv`
  
## Installation
1. Clone this repository or download the script.
2. Install the required dependencies:
   ```sh
   pip install tweepy python-dotenv
   ```
3. Create a `.env` file in the project directory and add your API credentials:
   ```ini
   API_KEY=your_api_key_here
   API_SECRET_KEY=your_api_secret_here
   ACCESS_TOKEN=your_access_token_here
   ACCESS_TOKEN_SECRET=your_access_token_secret_here
   ```

## Usage
1. Run the script with a Tweet ID:
   ```sh
   python twitter_like.py <tweet_id>
   ```
2. The script will authenticate and attempt to like the specified tweet.
3. Logs will indicate success or any errors encountered.

## Error Handling
- **Invalid Credentials**: The script will notify if API credentials are incorrect.
- **Rate Limits**: If the API rate limit is reached, the script will handle the error gracefully and retry after the required cooldown period.
- **Other Errors**: Any unexpected API errors will be logged and displayed.

## Notes
- Ensure your Twitter app has `Read and Write` permissions to like tweets.
- Never share your API credentials publicly.

## Author
Darko Vidanovski

## License
This script is for demonstration purposes only.

