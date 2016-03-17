import random
import axelrod
import tweepy
import csv

rounds = 10

# Create and play the match
players = [s() for s in random.sample(axelrod.strategies, 2)]
match = axelrod.Match(players, rounds)
match.play()

# Write the tweet
tweet = "{} v {}:".format(players[0],
                          players[1])
tweet += "\n\n"
tweet += match.sparklines(c_symbol="C", d_symbol="D")
tweet += "\n\n"
tweet += "axelrod.readthedocs.org"

# Print tweet to screen
print(tweet)

# Reading in credentials from file
with open('credentials', 'r') as f:
    cred = dict([row for row in csv.reader(f)])

# Authenticating
auth = tweepy.OAuthHandler(cred["consumer_key"], cred["consumer_secret"])
auth.set_access_token(cred["token"], cred["token_secret"])

# Tweeting
api = tweepy.API(auth)
api.update_status(tweet)
