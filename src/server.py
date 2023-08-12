import os
import sys
from os import environ

from flask import Flask

import bot


app = Flask(__name__)

@app.route("/")
def home():
    bot.tweet_line('./data/agrippa.txt')
    return "Tweeting a line from Agrippa's Occult Philosophy"


app.run(host='0.0.0.0', port=environ.get('PORT'))
