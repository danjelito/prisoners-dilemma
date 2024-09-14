from typing import Dict, Optional
from strategies import COOPERATE, DEFECT
from player import Player


class PrisonersDilemmaGame:

    def __init__(self, player_a: Player, player_b: Player, num_round: int) -> None:
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

        self.moves = []

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

            self.moves.append(
                {
                    "player_a_move": player_a_move,
                    "player_b_move": player_b_move,
                }
            )

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

    def get_moves(self) -> Dict[str, str]:
        return self.moves
