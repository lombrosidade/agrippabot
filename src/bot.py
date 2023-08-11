import os
import sys
import time
import logging
from os import environ
from dotenv import load_dotenv
import tweepy
from utils import read_lines, get_random_line


# Configure the logger
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Create a logger instance
logger = logging.getLogger(__name__)

# Get the parent directory of the current script (src directory)
script_directory = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)
logger.info(f"Script directory is: {script_directory}")

# Specify path with env file
dotenv_path = os.path.join(script_directory, '.env')
logger.info(f"Dotenv path is: {dotenv_path}")
# Load environment variables
is_loaded = load_dotenv(dotenv_path)
if not is_loaded:
    print(f"Couldn't find .env file in: {dotenv_path}. Make sure you they're in the root folder of the project."
          )

CONSUMER_KEY = environ.get('CONSUMER_KEY')
CONSUMER_SECRET = environ.get('CONSUMER_SECRET')
ACCESS_KEY = environ.get('ACCESS_KEY')
ACCESS_KEY_SECRET = environ.get('ACCESS_KEY_SECRET')
BEARER_TOKEN = environ.get('BEARER_TOKEN')
TEXT_PATH = environ.get('TEXT_PATH')
logger.info(f"Actual text path would be: {os.path.join(script_directory, TEXT_PATH)}")
INTERVAL = 6000  # tweets every 100 minutes


def tweet_line_from_file(path: str, max_retries: int = 1) -> None:
    count = 0
    client = tweepy.Client(
        bearer_token=BEARER_TOKEN,
        consumer_key=CONSUMER_KEY,
        consumer_secret=CONSUMER_SECRET,
        access_token=ACCESS_KEY,
        access_token_secret=ACCESS_KEY_SECRET,
    )

    # Check for credentials
    try:
        client.get_me()
        logger.info("Successfully logged in")
    except tweepy.errors.TweepyException as e:
        print(f"Couldn't authenticate: {e}")

    # Construct the absolute path to TEXT_PATH
    text_path = os.path.join(script_directory, TEXT_PATH)
    logger.debug(f"Trying to retrieve line from path: {text_path}")
    text_file = read_lines(text_path)
    logger.debug(f"Retrieved text from {TEXT_PATH}")

    # Get random line from text
    tweet = get_random_line(text_file)
    logger.debug(f"Got tweet from text: {tweet}")

    # Send tweet
    retries = 0
    while retries < max_retries:
        try:
            client.create_tweet(text=tweet)
            logging.info("Tweeting line from file...")
            logging.info(f"Sleeping for {INTERVAL} seconds...")
            time.sleep(INTERVAL)
        except tweepy.errors.TweepyException as e:
            logger.warning(f"Couldn't tweet: {e}")
        time.sleep(100)
        retries += 1

while True:
    tweet_line_from_file(TEXT_PATH)
