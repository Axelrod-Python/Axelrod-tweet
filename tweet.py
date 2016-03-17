import random
import axelrod
import tweepy
import csv

from secrets import *

rounds = 10
symbol_pairs = [["C", "D"]] * 4 + \
               [["😇 ", "😡 "]]

# Create and play the match
players = [s() for s in random.sample(axelrod.strategies, 2)]
symbols = random.choice(symbol_pairs)
match = axelrod.Match(players, rounds)
match.play()

# Write the tweet
tweet = "{} v {}:".format(players[0],
                          players[1])
tweet += "\n\n"
tweet += match.sparklines(c_symbol=symbols[0], d_symbol=symbols[1])
tweet += "\n\n"
tweet += "axelrod.readthedocs.org"

# Print tweet to screen
print(tweet)

# Authenticating
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(token, token_secret)

# Tweeting
api = tweepy.API(auth)
api.update_status(tweet)
