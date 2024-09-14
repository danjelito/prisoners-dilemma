import itertools
from pprint import pprint
from game import PrisonersDilemmaGame
from player import Player
from strategies import Strategies

# contestant strategies
stategies = Strategies()
unconditional_cooperator = Player(
    stategies.unconditional_cooperator, "unconditional_cooperator"
)
unconditional_defector = Player(
    stategies.unconditional_defector, "unconditional_defector"
)
random_cooperator = Player(stategies.random_cooperator, "random_cooperator")
probability_cooperator = Player(
    stategies.probability_cooperator, "probability_cooperator"
)
tit_for_tat = Player(stategies.tit_for_tat, "tit_for_tat")
suspicious_tit_for_tat = Player(
    stategies.suspicious_tit_for_tat, "suspicious_tit_for_tat"
)
tit_for_two_tats = Player(stategies.tit_for_two_tats, "tit_for_two_tats")
two_tits_for_tat = Player(stategies.two_tits_for_tat, "two_tits_for_tat")
grim_trigger = Player(stategies.grim_trigger, "grim_trigger")
generous_tit_for_tat = Player(stategies.generous_tit_for_tat, "generous_tit_for_tat")


# create matches
players = [
    unconditional_cooperator,
    unconditional_defector,
    random_cooperator,
    probability_cooperator,
    tit_for_tat,
    suspicious_tit_for_tat,
    tit_for_two_tats,
    two_tits_for_tat,
    grim_trigger,
    generous_tit_for_tat,
]
players_combination = list(itertools.combinations(players, 2))

# play matches
results = []
for player_a, player_b in players_combination:
    # reset player coins and reset strategy before each game
    player_a.reset_coins()
    player_b.reset_coins()
    stategies.reset_strategy()
    # play game
    game = PrisonersDilemmaGame(player_a, player_b, 10)
    game.play()
    game.print_score()
    results.append(game.get_score())

# pprint(game.get_moves())
