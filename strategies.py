import random
from typing import Optional

COOPERATE = "Cooperate"
DEFECT = "Defect"


class Strategies:

    def __init__(
        self,
    ) -> None:
        self.my_prev_move = None
        self.my_defects_in_a_row = 0
        self.opponent_defects_in_a_row = 0

    def reset_strategy(self) -> None:
        self.my_prev_move = None
        self.my_defects_in_a_row = 0
        self.opponent_defects_in_a_row = 0

    def unconditional_cooperator(self, opponent_prev_move: Optional[str]) -> str:
        """Cooperates unconditionally."""
        return COOPERATE

    def unconditional_defector(self, opponent_prev_move: Optional[str]) -> str:
        """Defects unconditionally."""
        return DEFECT

    def random_cooperator(self, opponent_prev_move: Optional[str]) -> str:
        """Random."""
        return random.choice([COOPERATE, DEFECT])

    def probability_cooperator(
        self, opponent_prev_move: Optional[str], p_cooperate: float = 0.8
    ) -> str:
        """Cooperates with fixed probably p."""
        return random.choices(
            [COOPERATE, DEFECT], weights=[p_cooperate, 1 - p_cooperate]
        )[0]

    def tit_for_tat(self, opponent_prev_move: Optional[str]) -> str:
        """Cooperates on the first round and imitates its opponent's previous move thereafter."""
        if opponent_prev_move is None:
            return COOPERATE
        return opponent_prev_move

    def suspicious_tit_for_tat(self, opponent_prev_move: Optional[str]) -> str:
        """Defects on the first round and imitates its opponent's previous move thereafter."""
        if opponent_prev_move is None:
            return DEFECT
        return opponent_prev_move

    def tit_for_two_tats(self, opponent_prev_move: Optional[str]) -> str:
        """Cooperates unless defected against twice in a row."""
        if opponent_prev_move == DEFECT:
            self.opponent_defects_in_a_row += 1
        else:
            self.opponent_defects_in_a_row = 0

        if self.opponent_defects_in_a_row >= 2:
            return DEFECT
        return COOPERATE

    def two_tits_for_tat(self, opponent_prev_move: Optional[str]) -> str:
        """Defects twice after being defected against, otherwise cooperates."""
        if opponent_prev_move is None:
            return COOPERATE

        if opponent_prev_move == DEFECT:
            self.my_defects_in_a_row = min(self.my_defects_in_a_row + 2, 2)

        if self.my_defects_in_a_row > 0:
            self.my_defects_in_a_row -= 1
            return DEFECT

        else:
            return COOPERATE

    def grim_trigger(self, opponent_prev_move) -> str:
        """Cooperates until its opponent has defected once, and then defects for the rest of the game."""
        if opponent_prev_move is None:
            return COOPERATE
        elif opponent_prev_move == DEFECT:
            self.my_defects_in_a_row += 1
            return DEFECT
        elif self.my_defects_in_a_row > 0:
            return DEFECT
        else:
            return COOPERATE

    def generous_tit_for_tat(self, opponent_prev_move: Optional[str]) -> str:
        """Cooperates on the first round and imitates its opponent's previous move thereafter, but sometimes forgo defecting."""
        if opponent_prev_move is None:
            return COOPERATE
        if opponent_prev_move == DEFECT and random.random() < 0.1:
            return COOPERATE
        return opponent_prev_move

    def pavlov(self, opponent_prev_move: Optional[str]) -> str:
        """Cooperates if the previous moves are the same and defect if they are not."""
        if opponent_prev_move is None:
            self.my_prev_move = COOPERATE
            return COOPERATE
        elif opponent_prev_move == self.my_prev_move:
            return COOPERATE
        else:
            return DEFECT

    def alternator(self, opponent_prev_move: Optional[str]) -> str:
        """Alternates between cooperating and defecting."""
        if opponent_prev_move is None:
            self.my_prev_move = COOPERATE
            return COOPERATE
        elif self.my_prev_move == COOPERATE:
            self.my_prev_move = DEFECT
            return DEFECT
        else:
            self.my_prev_move = COOPERATE
            return COOPERATE
