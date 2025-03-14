

# Define the payoff matrix
PAYOFF_MATRIX = {
    ('C', 'C'): (3, 3),
    ('C', 'D'): (0, 5),
    ('D', 'C'): (5, 0),
    ('D', 'D'): (1, 1)
}

def simulate_match(player1, player2, rounds=100):
    """
    Simulate an Iterated Prisoner's Dilemma match between two strategies.
    Returns the total scores for player1 and player2.
    """
    # Reset state if applicable
    if hasattr(player1, "reset"):
        player1.reset()
    if hasattr(player2, "reset"):
        player2.reset()
        
    history1, history2 = [], []
    score1, score2 = 0, 0

    for round_num in range(rounds):
        move1 = player1.move(round_num, history1, history2)
        move2 = player2.move(round_num, history2, history1)
        payoff1, payoff2 = PAYOFF_MATRIX[(move1, move2)]
        score1 += payoff1
        score2 += payoff2
        history1.append(move1)
        history2.append(move2)
    
    return score1, score2

def evaluate_fitness(individual, fixed_strategies, rounds=100):
    """
    Evaluate the fitness of an individual evolved strategy.
    The fitness is the total score accumulated when playing against all fixed strategies.
    """
    total_score = 0
    for opponent in fixed_strategies:
        score, _ = simulate_match(individual, opponent, rounds)
        total_score += score
    return total_score
