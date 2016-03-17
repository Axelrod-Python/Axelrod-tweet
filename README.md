# A twitter bot for the Axelrod library.

https://twitter.com/AxelrodPython

Tweets out results from 10 round matches between two random strategies from the
library.

# Credentials

Stored in `secrets.py`:

```
consumer_key = "XXXX"
consumer_secret = "XXXX"
token = "XXXX"
token_secret = "XXXX"
```

# Schedule

To schedule tweets, use crontab:

```
crontab -e # This edits your crontab
```

add the following line:

```
0 08,15 * * * python3 /home/vince/src/Axelrod-tweet.py
```

Above will tweet every hour at 0800 and 1500.

