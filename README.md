# Prisoner's Dilemma Simulation

This project simulates a **Prisoner's Dilemma** tournament between various strategies. The goal is to evaluate how different strategies perform when paired against each other over multiple rounds. The simulation is built using Python and leverages custom strategies, each implementing its own decision logic.

## Introduction

The **Prisoner's Dilemma** is a classic game theory problem that explores cooperation and competition between two participants. Each participant can either choose to **cooperate** or **defect**, with specific payoffs based on the combination of their choices:

- Both cooperate: 3 points for both.
- One defects while the other cooperates: 5 points for the defector, and 0 points for the cooperator.
- Both defect: 1 point for both.

This project simulates multiple strategies playing the Prisoner's Dilemma game over several rounds to study how different strategies perform over time.

## Usage

To run the simulation, execute the following Python script:

```bash
python main.py
```

### Customization

- You can modify the number of rounds for each game by editing the `N_ROUND` variable in the script.
- You can add new strategies or tweak existing ones by modifying the `strategies.py` file.

## Strategies

Here are the strategies implemented in this project:

- **Unconditional Cooperator**: Always cooperates.
- **Unconditional Defector**: Always defects.
- **Random Cooperator**: Randomly cooperates or defects with equal probability.
- **Probability Cooperator**: Cooperates with a fixed probability `p`.
- **Tit-for-Tat**: Cooperates on the first round, then mimics the opponent's last move.
- **Suspicious Tit-for-Tat**: Defects on the first round, then mimics the opponent's last move.
- **Tit-for-Two-Tats**: Cooperates unless the opponent defects twice in a row.
- **Two Tits for Tat**: Defects twice after the opponent defects, then cooperates.
- **Grim Trigger**: Cooperates until the opponent defects once, then defects for the remainder of the game.
- **Generous Tit-for-Tat**: Like Tit-for-Tat, but sometimes forgives a defection.
- **Pavlov**: Cooperates if the last round was mutually cooperative or mutually defective, otherwise defects.
- **Alternator**: Alternates between cooperating and defecting every round.

## Example Output

After running the simulation, you'll get a table of results where each strategy plays against every other strategy (including itself). The output will look something like this:

| Strategy             | alternator | generous_tit_for_tat | grim_trigger | pavlov |
| -------------------- | ---------- | -------------------- | ------------ | ------ |
| grim_trigger         | 2997       | 3000                 | 2000         | 3000   |
| generous_tit_for_tat | 2380       | 2000                 | 3000         | 3000   |
| tit_for_tat          | 2498       | 3000                 | 3000         | 3000   |
| two_tits_for_tat     | 2997       | 3000                 | 3000         | 3000   |
| pavlov               | 1500       | 3000                 | 3000         | 2000   |
