import random
import axelrod

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

print(tweet)
