from twython import TwythonStreamer
import time
import zmq
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

# set up twitter and server parameters
analyser = SentimentIntensityAnalyzer()
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind('<IP>:<PORT>')
CONSUMER_KEY = '<CONSUMERKEY>'
CONSUMER_SECRET = '<CONSUMERSECRET>'
ACCESS_TOKEN = '<ACCESSTOKEN>'
ACCESS_TOKEN_SECRET = '<ACCESSTOKENSECRET>'


# Twitter Streaming class
class MyStreamer(TwythonStreamer):
    counter = 0

    def on_success(self, data):
        try:
            if data['lang'] in ['en', 'fr', 'de', 'es', 'it', 'ru']:
                MyStreamer.counter += 1
                # get sentiment of tweet
                sent = analyser.polarity_scores(data['text'])['compound']
                for name in filter_name:
                    # find which filter name is contained within tweet
                    if name in data['text'].lower():
                        # send filter name and sentiment to server
                        print('Tweet: {c} | Sent: {s} | {n} | {lang}'
                              .format(c=MyStreamer.counter, s=sent, n=name,
                                      lang=data['lang']))
                        msg = 'Tweet: {c} | Sent: {s} | {n}' \
                            .format(c=MyStreamer.counter, s=sent, n=name)
                        socket.send_string(msg)
        except:
            pass

    def on_error(self, status_code, data):
        print(status_code, data)
        self.disconnect()


stream = MyStreamer(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN,
                    ACCESS_TOKEN_SECRET)

# import words to filter on
t = pd.read_csv(r'filter_names.csv')
filter_name = t['names'].tolist()
t = ','.join(filter_name)
print(t)
timeout = time.time() + 60
# continuously filter tweets based on names defined
while True:
    if time.time() > timeout:
        break
    stream.statuses.filter(track=t)
