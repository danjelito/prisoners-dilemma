import itertools
from typing import Callable, Dict, List, Optional, Tuple

COOPERATE = "C"
DEFECT = "D"


class PrisonersDilemmaGame:

    def __init__(self, player_a: "Player", player_b: "Player", num_round: int) -> None:
        self.player_a = player_a
        self.player_b = player_b
        self.round = num_round

    def get_coins(self, player_a_move: str, player_b_move: str):
        if player_a_move == player_b_move == COOPERATE:
            return 3, 3
        elif player_a_move == player_b_move == DEFECT:
            return 1, 1
        elif player_a_move == COOPERATE and player_b_move == DEFECT:
            return 0, 5
        elif player_a_move == DEFECT and player_b_move == COOPERATE:
            return 5, 0

    def play(self) -> None:

        # initiate player first move with None
        player_a_prev_move: Optional[str] = None
        player_b_prev_move: Optional[str] = None

        for round in range(self.round):

            # players make their move
            player_a_move = self.player_a.make_move(player_b_prev_move)
            player_b_move = self.player_b.make_move(player_a_prev_move)

            # get payoff
            player_a_coin, player_b_coin = self.get_coins(player_a_move, player_b_move)

            # update each players total coin
            self.player_a.collect_coins(player_a_coin)
            self.player_b.collect_coins(player_b_coin)

            # update each players prev move
            player_a_prev_move = player_a_move
            player_b_prev_move = player_b_move

        # after each game, reset first move
        player_a_prev_move = None
        player_b_prev_move = None

    def get_score(self) -> Dict[str, int]:
        return {
            self.player_a.name: self.player_a.coins,
            self.player_b.name: self.player_b.coins,
        }

    def print_score(self) -> None:
        # get winner
        if self.player_a.coins > self.player_b.coins:
            winner = f"Winner: {self.player_a.name}"
        elif self.player_a.coins < self.player_b.coins:
            winner = f"Winner: {self.player_b.name}"
        else:
            winner = "It's a Draw!"

        # format the output
        heading = f"{self.round}-round Prisoner's Dilemma: {self.player_a.name} vs {self.player_b.name}"
        score = f"Score: {self.player_a.name} ({self.player_a.coins}) vs {self.player_b.name} ({self.player_b.coins})"

        # print results
        print()
        print(f"{heading}\n{'=' * len(heading)}")
        print(score)
        print(winner)
        print()


class Strategies:

    def tit_for_tat(self, prev_opponent_move: Optional[str]) -> str:
        if prev_opponent_move is None:
            return COOPERATE
        return prev_opponent_move

    def always_defect(self, prev_opponent_move: Optional[str]) -> str:
        return DEFECT

    def always_cooperate(self, prev_opponent_move: Optional[str]) -> str:
        return COOPERATE


class Player:

    def __init__(self, strategy: Callable[[Optional[str]], str], name: str):
        self.strategy = strategy
        self.name = name
        self.coins = 0

    def make_move(self, prev_opponent_move: Optional[str]) -> str:
        return self.strategy(prev_opponent_move)

    def collect_coins(self, to_collect: int) -> None:
        self.coins += to_collect

    def reset_coins(self) -> None:
        self.coins = 0


# contestant strategies
tit_for_tat = Player(Strategies().tit_for_tat, "tit-for-tat")
always_defect = Player(Strategies().always_defect, "always_defect")
always_cooperate = Player(Strategies().always_cooperate, "always_cooperate")

# create matches
players = [tit_for_tat, always_cooperate, always_defect]
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
