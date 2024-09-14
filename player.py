import itertools
import random
from typing import Callable, Dict, List, Optional, Tuple
from strategies import Strategies, COOPERATE, DEFECT


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
