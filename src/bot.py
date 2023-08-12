import os
import time
import logging
from os import environ
from dotenv import load_dotenv
import tweepy
from utils import read_lines, get_random_line, get_script_directory, get_text_file


# Configure the logger
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Create a logger instance
logger = logging.getLogger(__name__)

# Get the parent directory of the current script (src directory)
script_directory = get_script_directory()

# Specify path with env file
dotenv_path = os.path.join(script_directory, '.env')
# Load environment variables
IS_LOADED = load_dotenv(dotenv_path)
if not IS_LOADED:
    print(f"Couldn't find .env file in: {dotenv_path}. "
          "Make sure you they're in the root folder of the project."
          )

CONSUMER_KEY = environ.get('CONSUMER_KEY')
CONSUMER_SECRET = environ.get('CONSUMER_SECRET')
ACCESS_KEY = environ.get('ACCESS_KEY')
ACCESS_KEY_SECRET = environ.get('ACCESS_KEY_SECRET')
BEARER_TOKEN = environ.get('BEARER_TOKEN')
TEXT_PATH = environ.get('TEXT_PATH')
if TEXT_PATH is not None:
    TEXT_FILE = get_text_file(script_directory, TEXT_PATH)
else:
    TEXT_FILE = get_text_file(script_directory, 'data/agrippa.txt')


def tweet_line_from_file(path: str, interval: int = 3600) -> None:
    """
    Tweets a random line from a text file using Tweepy V2 API.

    Args:
        path (str): The path to the text file containing tweetable lines.
        max_retries (int, optional): The maximum number of retries for tweeting. Default is 1.
        interval (int, optional): The interval between tweet attempts in seconds. Default is 100 seconds.
    """
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
    except tweepy.errors.TweepyException as tweepy_error:
        print(f"Couldn't authenticate: {tweepy_error}")

    # Construct the absolute path to TEXT_PATH
    text_path = os.path.join(script_directory, path)
    assert os.path.isfile(text_path)
    logger.debug("Trying to retrieve line from path: %s", path)
    text_file = read_lines(text_path)
    assert isinstance(text_file, list)
    logger.debug("Retrieved text from %s", text_path)


    # Main loop
    while True:
      try:
          # Get random line from text
          tweet = get_random_line(text_file)
          logger.debug("Got tweet from text: %s", tweet)
          assert isinstance(tweet, str)
          client.create_tweet(text=tweet)
          logging.info("Tweeting line from file...")
          logging.info("Sleeping for %s seconds...", interval)
          time.sleep(interval)
          continue
    except tweepy.errors.TweepyException as tweepy_exception:
        logger.warning("Couldn't tweet: %s", tweepy_exception)
        time.sleep(interval)
        break


tweet_line_from_file(TEXT_FILE)
