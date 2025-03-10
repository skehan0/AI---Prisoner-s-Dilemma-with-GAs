import random
from Prisoner import Prisoner

class Game:
    @staticmethod
    def perform_move(individual, previous_moves):
        return individual.play()

    @staticmethod
    def count_score(move1, move2):
        if move1 == 0 and move2 == 0:
            return (3, 3)  # Both cooperate
        elif move1 == 0 and move2 == 1:
            return (0, 5)  # First cooperates, second defects
        elif move1 == 1 and move2 == 0:
            return (5, 0)  # First defects, second cooperates
        else:
            return (1, 1)  # Both defect

class AlwaysCooperate(Prisoner):
    """Always cooperates."""
    def play(self, history=None):
        return 0  # Always cooperate

class AlwaysDefect(Prisoner):
    """Always defects."""
    def play(self, history=None):
        return 1  # Always defect

class TitForTat(Prisoner):
    """Always mimics the opponent's last move."""
    def __init__(self):
        super().__init__()
        self.last_strategy = 0  # Assume cooperation in the first round

    def play(self, history):
        if history:
            self.last_strategy = history[-1]
        return self.last_strategy

    def process_results(self, my_strategy, other_strategy):
        self.last_strategy = other_strategy

class RandomStrategy(Prisoner):
    """Randomly chooses to cooperate or defect."""
    def play(self, history=None):
        return random.choice([0, 1])

def play_round(strategy1, strategy2, history1, history2):
    move1 = strategy1.play(history2)
    move2 = strategy2.play(history1)
    strategy1.process_results(move1, move2)
    strategy2.process_results(move2, move1)

    history1.append(move1)
    history2.append(move2)

    return move1, move2

def test_strategies():
    s1 = TitForTat()
    s2 = RandomStrategy()
    history1, history2 = [], []

    for _ in range(5):
        m1, m2 = play_round(s1, s2, history1, history2)
        print(f"{s1.__class__.__name__}: {m1}, {s2.__class__.__name__}: {m2}")

if __name__ == "__main__":
    test_strategies()