import random
import tweepy
import csv

from secrets import *

# Mocking matplotlib
import mock
import sys

mock_modules = ['matplotlib.pyplot', 'matplotlib',
                'matplotlib.transforms', 'mpl_toolkits.axes_grid1']
for mod_name in mock_modules:
    sys.modules[mod_name] = mock.Mock()

# import the library
import axelrod

# Parameters
rounds = 10
symbol_pairs = [["C", "D"]] * 4 + \
               [["😇 ", "😡 "]]

# Create and play the match
players = [s() for s in random.sample(axelrod.strategies, 2)]
symbols = random.choice(symbol_pairs)
match = axelrod.Match(players, rounds)
match.play()
scores = [sum([score[i] for score in match.scores()]) for i in range(2)]

# Write the tweet
tweet = "{} v {}:".format(players[0],
                          players[1])
tweet += "\n\n"
tweet += match.sparklines(c_symbol=symbols[0], d_symbol=symbols[1])
tweet += "\n\n"
tweet += "Score: ({}, {})".format(*scores)
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
