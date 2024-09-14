import itertools
from pprint import pprint
from game import PrisonersDilemmaGame, play_game
from player import Player
from strategies import Strategies
import pandas as pd

N_ROUND = 1000

if __name__ == "__main__":

    # contestant strategies
    strategies = Strategies()
    unconditional_cooperator = Player(
        strategies.unconditional_cooperator, "unconditional_cooperator"
    )
    unconditional_defector = Player(
        strategies.unconditional_defector, "unconditional_defector"
    )
    random_cooperator = Player(strategies.random_cooperator, "random_cooperator")
    probability_cooperator = Player(
        strategies.probability_cooperator, "probability_cooperator"
    )
    tit_for_tat = Player(strategies.tit_for_tat, "tit_for_tat")
    suspicious_tit_for_tat = Player(
        strategies.suspicious_tit_for_tat, "suspicious_tit_for_tat"
    )
    tit_for_two_tats = Player(strategies.tit_for_two_tats, "tit_for_two_tats")
    two_tits_for_tat = Player(strategies.two_tits_for_tat, "two_tits_for_tat")
    grim_trigger = Player(strategies.grim_trigger, "grim_trigger")
    generous_tit_for_tat = Player(
        strategies.generous_tit_for_tat, "generous_tit_for_tat"
    )
    pavlov = Player(strategies.pavlov, "pavlov")
    alternator = Player(strategies.alternator, "alternator")

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
        pavlov,
        alternator,
    ]
    # get combinations of players (strategy vs another strategy)
    players_combination = list(itertools.combinations(players, 2))
    # get the match of each strategy against itself
    players_self_match = [(player, player) for player in players]

    # play matches for strategy vs strategy
    results_a = play_game(players_combination, strategies, N_ROUND)
    # play matches for strategy vs itself
    results_b = play_game(players_self_match, strategies, N_ROUND)

    # display result table
    data = []
    for match in results_a:
        for strategy, score in match.items():
            for opponent in match.keys():
                if opponent != strategy:
                    data.append([strategy, opponent, score])
    for match in results_b:
        for strategy, doubled_score in match.items():
            # the score of result_b is added twice because they are battling themselves in dict
            data.append([strategy, strategy, score // 2])

    df = pd.DataFrame(data, columns=["Strategy", "Opponent", "Score"])
    df = df.pivot(index=["Strategy"], columns=["Opponent"], values=["Score"])
    df = df.assign(Average=lambda df_: df_.mean(axis=1))
    df = df.sort_values("Average", ascending=False)

    print(df)
