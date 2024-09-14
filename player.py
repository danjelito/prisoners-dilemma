from typing import Callable, Optional


class Player:

    def __init__(self, strategy: Callable[[Optional[str]], str], name: str):
        self.strategy = strategy
        self.name = name
        self.points = 0

    def make_move(self, opponent_prev_move: Optional[str]) -> str:
        return self.strategy(opponent_prev_move)

    def collect_points(self, to_collect: int) -> None:
        self.points += to_collect

    def reset_points(self) -> None:
        self.points = 0
