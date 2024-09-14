import random
from typing import Callable, Dict, List, Optional, Tuple

COOPERATE = "C"
DEFECT = "D"


class Strategies:

    def unconditional_cooperator(self, prev_opponent_move: Optional[str]) -> str:
        """Cooperates unconditionally."""
        return COOPERATE

    def unconditional_defector(self, prev_opponent_move: Optional[str]) -> str:
        """Defects unconditionally."""
        return DEFECT

    def random_cooperator(self, prev_opponent_move: Optional[str]) -> str:
        """Random."""
        return random.choice([COOPERATE, DEFECT])

    def probability_cooperator(
        self, prev_opponent_move: Optional[str], p_cooperate: float = 0.2
    ) -> str:
        """Cooperates with fixed probably p."""
        return random.choices(
            [COOPERATE, DEFECT], weights=[p_cooperate, 1 - p_cooperate]
        )[0]

    def tit_for_tat(self, prev_opponent_move: Optional[str]) -> str:
        """Cooperates on the first round and imitates its opponent's previous move thereafter."""
        if prev_opponent_move is None:
            return COOPERATE
        return prev_opponent_move

    def suspicious_tit_for_tat(self, prev_opponent_move: Optional[str]) -> str:
        """Defects on the first round and imitates its opponent's previous move thereafter."""
        if prev_opponent_move is None:
            return DEFECT
        return prev_opponent_move
