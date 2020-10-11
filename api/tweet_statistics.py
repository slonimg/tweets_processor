import json
import traceback
from collections import Counter
import time
import logging
import requests

logger = logging.getLogger()


def load_ignore_terms(filename):
    ignore_set = set()
    with open(filename, 'r') as f:
        for word in f:
            ignore_set.add(word.strip().lower())
    return ignore_set


class TweetsStatistics:
    def __init__(self, url, ignore_dictionary_filename=None):
        self._words, self._users, self._hashtags = Counter(), Counter(), Counter()
        self.top_words, self.top_users, self.top_hashtags = [], [], []
        self.tweets_processed = 0
        self.top_refresh_interval = 50
        self._start_time = None
        self.url = url
        self.ignore_set = set() if not ignore_dictionary_filename else load_ignore_terms(ignore_dictionary_filename)

    def start(self):
        self._start_time = time.time()
        response = requests.get(self.url, stream=True)
        for data in response.iter_lines(chunk_size=10240):
            try:
                if len(data) == 0:
                    logger.warning(f'data received is empty')
                    continue
                self.process_tweet(json.loads(data))
            except Exception:
                logger.error(traceback.format_exc())
                logger.error(f'failed to process {data}')

    def update_words(self, text):
        counter = Counter(text.lower().split())
        for word in self.ignore_set:
            if counter[word] > 0:
                counter.pop(word, None)

        self._words.update(counter)

    def update_users(self, username):
        d = {username: 1}
        self._users.update(d)

    def update_hashtags(self, hashtags_text):
        hashtags = {h['text']: 1 for h in hashtags_text}
        self._hashtags.update(hashtags)

    def process_tweet(self, tweet_json):
        if 'text' not in tweet_json:
            return

        text = tweet_json['text']
        self.update_words(text)
        self.update_users(tweet_json['user']['screen_name'])
        self.update_hashtags(tweet_json['entities']['hashtags'])
        self.tweets_processed += 1

        if self.tweets_processed % self.top_refresh_interval == 0:
            self.top_hashtags = self._hashtags.most_common(10)
            self.top_users = self._users.most_common(10)
            self.top_words = self._words.most_common(10)

    def get_tweets_processed_per_second(self):
        seconds_passed = time.time() - self._start_time
        return self.tweets_processed // seconds_passed
