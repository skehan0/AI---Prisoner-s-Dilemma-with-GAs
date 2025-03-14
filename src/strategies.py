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