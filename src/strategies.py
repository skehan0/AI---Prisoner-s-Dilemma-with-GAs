import random
from Prisoner import Prisoner

class Strategy():

    def perform_move(individual, previous_moves):
        return individual.play(previous_moves)

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
        self.last_move = 0  # Assume cooperation in the first round

    def play(self, history):
        if history:
            self.last_move = history[-1]
        return self.last_move

    def process_results(self, my_strategy, other_strategy):
        self.last_move = other_strategy

class RandomStrategy(Prisoner):
    """Randomly chooses to cooperate or defect."""
    def play(self, history=None):
        move = random.choice([0, 1])
        return move

# class GrimTrigger(Prisoner):
#     """Cooperates until the opponent defects, then defects forever."""
#     def __init__(self):
#         super().__init__()
#         self.defected = False
#
#     def play(self, history):
#         if history and 1 in history:
#             self.defected = True
#         print(f"GrimTrigger plays: {1 if self.defected else 0}")
#         return 1 if self.defected else 0
#
#     def process_results(self, my_strategy, other_strategy):
#         if other_strategy == 1:
#             self.defected = True  # Once defected, always defect

def play_round(strategy1, strategy2, history1, history2):
    move1 = strategy1.play(history2)
    move2 = strategy2.play(history1)
    strategy1.process_results(move1, move2)
    strategy2.process_results(move2, move1)

    history1.append(move1)
    history2.append(move2)

    print(f"Round Result: {strategy1.__class__.__name__} plays {move1}, {strategy2.__class__.__name__} plays {move2}")
    return move1, move2

def test_strategies():
    s1 = TitForTat()
    s2 = RandomStrategy()
    history1, history2 = [], []

    for round_num in range(5):
        m1, m2 = play_round(s1, s2, history1, history2)

if __name__ == "__main__":
    test_strategies()
