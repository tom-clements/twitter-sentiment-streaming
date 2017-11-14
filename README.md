# Twitter Streaming Sentiment

[![GitHub latest](https://img.shields.io/github/tag/tom-clements/twitter-sentiment-streaming.svg)](https://github.com/tom-clements/twitter-sentiment-streaming/)
[![MIT license](https://img.shields.io/github/license/mashape/apistatus.svg)](http://opensource.org/licenses/MIT)

### Requirements

packages:
```
pip install -r requirements.txt
```
Also needed:
- Twitter Account
- Plotly Account

### Twitter Server

Choose a host to scrape live tweets. For local host use 127.0.0.1:5555.
Create a new twitter app at https://apps.twitter.com/.
From there, click on (manage keys and access tokens) to get all four keys required below.

On lines 11-15 on the server python script, add these keys to the code:

```python
socket.bind('<IP>:<PORT>')
CONSUMER_KEY = '<CONSUMERKEY>'
CONSUMER_SECRET = '<CONSUMERSECRET>'
ACCESS_TOKEN = '<ACCESSTOKEN>'
ACCESS_TOKEN_SECRET = '<ACCESSTOKENSECRET>'
```
### Twitter Client
Add the connection IP and port
```python
socket.connect('<IP>:<PORT>')
```

### Plotly Stream
On your plotly account, go into settings and API keys. You'll need as many API streaming tokens as data traces you want to stream.
Add these to
```
User\.plotly\.credentials
```
as a list format.
### Executing
Inside filter_names.csv specify which words are to be scraped from twitter
```
python twitter_stream_server.py
```
in a new command instance execute the Client
```
python twitter_stream_client.py
```
plotly should then open with the streaming data.
