from genetic_algorithm import evolution
from src.strategies import RandomStrategy, GrimTrigger, TitForTwoTats, Joss
from strategies import AlwaysDefect, AlwaysCooperate, TitForTat
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # Parameters for the GA
    GENERATIONS = 100
    POPULATION_SIZE = 100
    ROUNDS_PER_MATCH = 100
    TOURNAMENT_SIZE = 6
    CROSSOVER_RATE = 0.8
    MUTATION_RATE = 0.02
    
    # Define fixed strategies
    FIXED_STRATEGIES = [AlwaysCooperate(), AlwaysDefect(), TitForTat(), RandomStrategy(), GrimTrigger(), TitForTwoTats(), Joss()]
    
    # Run the genetic algorithm
    best_strategy, best_fit_hist, avg_fit_hist = evolution(
        fixed_strategies=FIXED_STRATEGIES,
        generations=GENERATIONS,
        population_size=POPULATION_SIZE,
        rounds=ROUNDS_PER_MATCH,
        tournament_size=TOURNAMENT_SIZE,
        crossover_rate=CROSSOVER_RATE,
        mutation_rate=MUTATION_RATE
    )
    
    # Print the best evolved strategy and its genotype
    print("\nBest Evolved Strategy Genotype (as moves):")
    print(best_strategy.genotype)  # Displays the strategy's genotype
    
    # Plot fitness progression over generations
    generations = range(len(best_fit_hist))
    plt.figure(figsize=(10, 6))
    plt.plot(generations, best_fit_hist, label="Best Fitness", color='blue')
    plt.plot(generations, avg_fit_hist, label="Average Fitness", color='green')
    plt.xlabel("Generation")
    plt.ylabel("Fitness (Total Score over Fixed Opponents)")
    plt.title("Fitness Progression over Generations")
    plt.legend()
    plt.grid(True)
    plt.show()