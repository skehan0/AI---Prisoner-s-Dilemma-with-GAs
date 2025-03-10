import random
from strategies import AlwaysDefect, AlwaysCooperate, TitForTat, RandomStrategy

# Variables
population_size = 50
tournament_size = 5
genotype_length = 3
generations = 100
mutation_rate = 0.05
strategies = [AlwaysCooperate, AlwaysDefect, TitForTat, RandomStrategy]

def random_genome(length):
    """Generate a random genome representing a strategy."""
    return [random.choice(['C', 'D']) for _ in range(length)]

def init_population(size):
    """Initialize a population with random genomes."""
    return [random_genome(genotype_length) for _ in range(size)]

def play_game(strategy1, strategy2, rounds=10):
    """Simulate a game between two strategies and return scores."""
    score1, score2 = 0, 0
    history1, history2 = [], []

    for _ in range(rounds):
        move1 = strategy1(history2)
        move2 = strategy2(history1)

        if move1 == 'C' and move2 == 'C':
            score1 += 3; score2 += 3
        elif move1 == 'C' and move2 == 'D':
            score1 += 0; score2 += 5
        elif move1 == 'D' and move2 == 'C':
            score1 += 5; score2 += 0
        else:
            score1 += 1; score2 += 1

        history1.append(move1)
        history2.append(move2)

    return score1, score2

def fitness(strategy):
    """Evaluate fitness by playing against fixed strategies."""
    total_score = 0
    for opponent in strategies:
        score, _ = play_game(
            lambda history: strategy[0] if not history else (strategy[1] if history[-1] == 'C' else strategy[2]),
            lambda history: opponent().play(history)
        )
        total_score += score
    return total_score

def fitness_population(population):
    """Compute fitness scores for entire population."""
    return [fitness(ind) for ind in population]

def tournament_selection(population, fitness_values):
    """Select individuals using tournament selection."""
    selected = []
    for _ in range(len(population)):
        tournament = random.sample(list(enumerate(fitness_values)), tournament_size)
        winner = max(tournament, key=lambda x: x[1])[0]  # Select best
        selected.append(population[winner])
    return selected

def crossover(parent1, parent2):
    """Perform one-point crossover."""
    point = random.randint(1, genotype_length - 1)
    return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]

def mutate(individual):
    """Mutate an individual with a small probability."""
    if random.random() < mutation_rate:
        index = random.randint(0, len(individual) - 1)
        individual[index] = 'C' if individual[index] == 'D' else 'D'
    return individual

def evolution():
    """Run the genetic algorithm for multiple generations."""
    population = init_population(population_size)
    for gen in range(generations):
        fitness_scores = fitness_population(population)
        selected = tournament_selection(population, fitness_scores)
        offspring = []

        for i in range(0, len(selected), 2):
            if i + 1 < len(selected):
                child1, child2 = crossover(selected[i], selected[i + 1])
                offspring.extend([mutate(child1), mutate(child2)])
            else:
                offspring.append(mutate(selected[i]))

        population = offspring  # Replace old population

        if gen % 10 == 0:
            print(f"Generation {gen}: Best fitness = {max(fitness_scores)}")

    best_strategy = max(population, key=fitness)
    print("Best evolved strategy:", best_strategy)

if __name__ == "__main__":
    evolution()