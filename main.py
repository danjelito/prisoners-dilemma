import itertools
from pprint import pprint
from game import PrisonersDilemmaGame
from player import Player
from strategies import Strategies
import pandas as pd

N_ROUND = 200

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
    # get combinations of players (strategy vs another strategy)
    players_combination = list(itertools.combinations(players, 2))
    # get the match of each strategy against itself
    players_self_match = [(player, player) for player in players]

    # play matches for strategy vs strategy
    results_a = []
    for player_a, player_b in players_combination:
        # reset player coins and reset strategy before each game
        player_a.reset_coins()
        player_b.reset_coins()
        strategies.reset_strategy()
        # play game
        game = PrisonersDilemmaGame(player_a, player_b, N_ROUND)
        game.play()
        game.print_score()
        results_a.append(game.get_score())

    # play matches for strategy vs itself
    results_b = []
    for player_a, player_b in players_self_match:
        # reset player coins and reset strategy before each game
        player_a.reset_coins()
        player_b.reset_coins()
        strategies.reset_strategy()
        # play game
        game = PrisonersDilemmaGame(player_a, player_b, N_ROUND)
        game.play()
        game.print_score()
        results_b.append(game.get_score())

    # display result table
    data = []
    for match in results_a:
        for strategy, score in match.items():
            for opponent in match.keys():
                if opponent != strategy:
                    data.append([strategy, opponent, score])
    for match in results_b:
        for strategy, doubled_score in match.items():
            data.append([strategy, strategy, score // 2])

    df = pd.DataFrame(data, columns=["Strategy", "Opponent", "Score"])
    df = df.pivot(index=["Strategy"], columns=["Opponent"], values=["Score"])
    df = df.assign(Average=lambda df_: df_.mean(axis=1))
    df = df.sort_values("Average", ascending=False)

    print(df)
