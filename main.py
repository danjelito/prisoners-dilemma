import itertools
import random
from typing import Callable, Dict, List, Optional, Tuple
from strategies import Strategies, COOPERATE, DEFECT
from player import Player
from game import PrisonersDilemmaGame


# contestant strategies
unconditional_cooperator = Player(
    Strategies().unconditional_cooperator, "unconditional_cooperator"
)
unconditional_defector = Player(
    Strategies().unconditional_defector, "unconditional_defector"
)
random_cooperator = Player(Strategies().random_cooperator, "random_cooperator")
probability_cooperator = Player(
    Strategies().probability_cooperator, "probability_cooperator"
)
tit_for_tat = Player(Strategies().tit_for_tat, "tit_for_tat")
suspicious_tit_for_tat = Player(
    Strategies().suspicious_tit_for_tat, "suspicious_tit_for_tat"
)


# create matches
players = [
    unconditional_cooperator,
    unconditional_defector,
    random_cooperator,
    probability_cooperator,
    tit_for_tat,
    suspicious_tit_for_tat,
]
players_combination = list(itertools.combinations(players, 2))

# play matches
results = []
for player_a, player_b in players_combination:
    # reset player coins before each game
    player_a.reset_coins()
    player_b.reset_coins()
    # play game
    game = PrisonersDilemmaGame(player_a, player_b, 10)
    game.play()
    game.print_score()
    results.append(game.get_score())
