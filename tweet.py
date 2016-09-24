import random
import tweepy

from secrets import *
from numpy import median

# Mocking matplotlib
import mock
import sys

mock_modules = ['matplotlib.pyplot', 'matplotlib',
                'matplotlib.transforms', 'mpl_toolkits.axes_grid1']
for mod_name in mock_modules:
    sys.modules[mod_name] = mock.Mock()

# import the library
import axelrod


def tweet_match():
    """
    Tweet a random match
    """
    # Parameters
    rounds = 10
    symbol_pairs = [["C", "D"]] * 4 + \
                   [["😇 ", "😡 "]]
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

    return tweet

def tweet_tournament():
    """
    Tweet a random tournament
    """
    players = [s() for s in random.sample(axelrod.strategies, 3)]
    tournament = axelrod.Tournament(players)
    results = tournament.play(progress_bar=False)
    ranks = results.ranked_names
    scores = sorted(results.normalised_scores, reverse=True)

    # Write the tweet
    tweet = "3 player tournament: \n"
    tweet += "\n"
    tweet += "1st: {} (Median score: {:.2f})\n".format(ranks[0], median(scores[0]))
    tweet += "2nd: {} ({:.2f})\n".format(ranks[1], median(scores[1]))
    tweet += "3rd: {} ({:.2f})\n".format(ranks[2], median(scores[2]))

    return tweet

tweet_type = random.choice([tweet_tournament, tweet_match])
tweet = tweet_type()
# Print tweet to screen
print(tweet)

# Authenticating
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(token, token_secret)

# Tweeting
api = tweepy.API(auth)
api.update_status(tweet)
