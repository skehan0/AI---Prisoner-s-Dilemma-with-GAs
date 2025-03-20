import random
import numpy as np
from Prisoner import evaluate_fitness
from strategies import AlwaysDefect, AlwaysCooperate, TitForTat, RandomStrategy, GrimTrigger, TitForTwoTats, Joss, EvolvedStrategy

strategies = [AlwaysCooperate, AlwaysDefect, TitForTat, RandomStrategy, GrimTrigger, TitForTwoTats, Joss, EvolvedStrategy]

def tournament_selection(population, fitnesses, tournament_size=6):
    """
    Perform tournament selection by choosing 'tournament_size' random individuals,
    then returning the one with the highest fitness.
    """
    selected_indices = random.sample(range(len(population)), tournament_size)
    selected = [(i, fitnesses[i]) for i in selected_indices]
    selected.sort(key=lambda x: x[1], reverse=True)
    return population[selected[0][0]]

def crossover(parent1, parent2):
    """
    Perform one-point crossover on two parent genotypes.
    """
    point = random.randint(1, len(parent1.genotype) - 1)
    child1_genotype = parent1.genotype[:point] + parent2.genotype[point:]
    child2_genotype = parent2.genotype[:point] + parent1.genotype[point:]
    return EvolvedStrategy(child1_genotype), EvolvedStrategy(child2_genotype)

def mutate(individual, mutation_rate=0.02):
    """
    Mutate an individual's genotype by flipping each bit with probability 'mutation_rate'.
    """
    new_genotype = individual.genotype[:]
    for i in range(len(new_genotype)):
        if random.random() < mutation_rate:
            new_genotype[i] = 1 - new_genotype[i]
    return EvolvedStrategy(new_genotype)

def evolution(fixed_strategies, generations=100, population_size=100, rounds=100,
              tournament_size=6, crossover_rate=0.8, mutation_rate=0.02, elitism=True, noise=0.1):
    """
    Run the genetic algorithm to evolve strategies against fixed opponents with noise.
    Returns the best evolved strategy along with fitness history.
    """
    # Initialize population with random evolved strategies
    population = [EvolvedStrategy() for _ in range(population_size)]
    best_fitness_history = []
    avg_fitness_history = []

    for gen in range(generations):
        fitnesses = [evaluate_fitness(ind, fixed_strategies, rounds, noise) for ind in population]
        best_fitness = max(fitnesses)
        avg_fitness = sum(fitnesses) / len(fitnesses)
        best_fitness_history.append(best_fitness)
        avg_fitness_history.append(avg_fitness)

        if gen % 10 == 0:
            print(f"Generation {gen}: Best Fitness = {best_fitness}, Average Fitness = {avg_fitness:.2f}")

        new_population = []

        # Elitism: Carry over the best individual to the next generation
        if elitism:
            best_index = np.argmax(fitnesses)
            best_individual = population[best_index]
            new_population.append(best_individual)

        while len(new_population) < population_size:
            parent1 = tournament_selection(population, fitnesses, tournament_size)
            parent2 = tournament_selection(population, fitnesses, tournament_size)
            if random.random() < crossover_rate:
                child1, child2 = crossover(parent1, parent2)
            else:
                child1 = EvolvedStrategy(parent1.genotype)
                child2 = EvolvedStrategy(parent2.genotype)
            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)
            new_population.extend([child1, child2])

        population = new_population[:population_size]

    # Final evaluation to obtain the best individual
    fitnesses = [evaluate_fitness(ind, fixed_strategies, rounds, noise) for ind in population]
    best_index = np.argmax(fitnesses)
    best_individual = population[best_index]
    return best_individual, best_fitness_history, avg_fitness_history