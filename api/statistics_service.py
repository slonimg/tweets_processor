import time
import logging
from threading import Thread
from flask import Flask
from flask_cors import CORS

from tweet_statistics import TweetsStatistics

statistics = TweetsStatistics('http://34.67.195.184/', 'ignore_dictionary.txt')
# statistics = TweetsStatistics('http://34.67.195.184/bck', 'ignore_dictionary.txt')
start = time.time()

app = Flask(__name__)
logger = logging.getLogger()
CORS(app)


@app.route('/stats')
def get_stats():
    global statistics
    global start
    logger.info(f'server is up for {(time.time() - start) / 60} minutes')
    return {
        'words': statistics.top_words,
        'users': statistics.top_users,
        'hashtags': statistics.top_hashtags,
        'avg_tweets_per_second': statistics.get_tweets_processed_per_second(),
        'total_tweets_processed': statistics.tweets_processed,
    }


with app.app_context():
    t = Thread(target=statistics.start)
    t.start()
