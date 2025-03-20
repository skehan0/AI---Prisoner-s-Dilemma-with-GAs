import random

class AlwaysCooperate:
    def __init__(self):
        self.name = "Always Cooperate"
        
    def reset(self):
        pass
    
    def move(self, round_num, my_history, opp_history):
        return 'C'

class AlwaysDefect:
    def __init__(self):
        self.name = "Always Defect"
        
    def reset(self):
        pass
    
    def move(self, round_num, my_history, opp_history):
        return 'D'

class TitForTat:
    def __init__(self):
        self.name = "Tit-for-Tat"
        
    def reset(self):
        pass
    
    def move(self, round_num, my_history, opp_history):
        if round_num == 0:
            return 'C'
        return opp_history[-1]

class GrimTrigger:
    def __init__(self):
        self.name = "Grim Trigger"
        self.triggered = False
        
    def reset(self):
        self.triggered = False
        
    def move(self, round_num, my_history, opp_history):
        if round_num == 0:
            return 'C'
        if 'D' in opp_history:
            self.triggered = True
        return 'D' if self.triggered else 'C'

class RandomStrategy:
    def __init__(self):
        self.name = "Random Strategy"
        
    def reset(self):
        pass
    
    def move(self, round_num, my_history, opp_history):
        return random.choice(['C', 'D'])

class TitForTwoTats:
    def __init__(self):
        self.name = "Tit-for-Two-Tats"

    def reset(self):
        pass

    def move(self, round_num, my_history, opp_history):
        if round_num < 2:
            return 'C'  # Start by cooperating
        if opp_history[-1] == 'D' and opp_history[-2] == 'D':  # Only defect if opponent defected twice
            return 'D'
        return 'C'

class Joss:
    def __init__(self, defect_chance=0.1):
        self.name = "Joss"
        self.defect_chance = defect_chance

    def reset(self):
        pass

    def move(self, round_num, my_history, opp_history):
        if round_num == 0:
            return 'C'
        if random.random() < self.defect_chance:
            return 'D'  # Random defection
        return opp_history[-1]  # Otherwise, Tit-for-Tat

class EvolvedStrategy:
    """
    Memory-1 strategy represented by a 5-bit genotype:
      - gene[0]: initial move (1 for 'C', 0 for 'D')
      - gene[1]: response when previous round was (C, C)
      - gene[2]: response when previous round was (C, D)
      - gene[3]: response when previous round was (D, C)
      - gene[4]: response when previous round was (D, D)
    """
    def __init__(self, genotype=None):
        if genotype is None:
            # Initialize with 5 random bits
            self.genotype = [random.choice([0, 1]) for _ in range(5)]
        else:
            self.genotype = genotype[:]
        self.name = "EvolvedStrategy"
    
    def reset(self):
        pass  # Memory-1 strategies do not maintain additional state
    
    def move(self, round_num, my_history, opp_history):
        if round_num == 0:
            return 'C' if self.genotype[0] == 1 else 'D'
        my_last = my_history[-1]
        opp_last = opp_history[-1]
        if my_last == 'C' and opp_last == 'C':
            index = 1
        elif my_last == 'C' and opp_last == 'D':
            index = 2
        elif my_last == 'D' and opp_last == 'C':
            index = 3
        elif my_last == 'D' and opp_last == 'D':
            index = 4
        return 'C' if self.genotype[index] == 1 else 'D'
    
    def __str__(self):
        # Represent the genotype as a sequence of moves (C or D)
        mapping = lambda bit: 'C' if bit == 1 else 'D'
        return "".join(mapping(bit) for bit in self.genotype)
    

class EvolvedStrategy2:
    """
    Memory-2 strategy represented by a 17-bit genotype:
      - gene[0]: initial move (1 for 'C', 0 for 'D')
      - gene[1] to gene[16]: responses for all possible combinations of the last two rounds:
        (C, C), (C, D), (D, C), (D, D) for both players.
    """
    def __init__(self, genotype=None):
        if genotype is None:
            # Initialize with 17 random bits
            self.genotype = [random.choice([0, 1]) for _ in range(17)]
        else:
            self.genotype = genotype[:]
        self.name = "EvolvedStrategy2"

    def reset(self):
        pass  # Memory-2 strategies do not maintain additional state

    def move(self, round_num, my_history, opp_history):
        if round_num == 0:
            # Use the initial move
            return 'C' if self.genotype[0] == 1 else 'D'
        elif round_num == 1:
            # If only one round has been played, fall back to Memory-1 logic
            last_round = (my_history[-1], opp_history[-1])
            if last_round == ('C', 'C'):
                index = 1
            elif last_round == ('C', 'D'):
                index = 2
            elif last_round == ('D', 'C'):
                index = 3
            elif last_round == ('D', 'D'):
                index = 4
            return 'C' if self.genotype[index] == 1 else 'D'
        else:
            # Use the last two rounds to determine the move
            last_two_rounds = ((my_history[-2], opp_history[-2]), (my_history[-1], opp_history[-1]))
            # Map the last two rounds to an index in the genotype
            index = 1 + self._get_index_from_last_two_rounds(last_two_rounds)
            return 'C' if self.genotype[index] == 1 else 'D'

    def _get_index_from_last_two_rounds(self, last_two_rounds):
        """
        Map the last two rounds to an index in the genotype.
        Each round is represented as (my_move, opp_move), where:
          - 'C' = 0, 'D' = 1
        """
        mapping = {'C': 0, 'D': 1}
        (my_last_2, opp_last_2), (my_last_1, opp_last_1) = last_two_rounds
        index = (
            (mapping[my_last_2] << 3) | (mapping[opp_last_2] << 2) |
            (mapping[my_last_1] << 1) | mapping[opp_last_1]
        )
        return index