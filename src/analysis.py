import matplotlib.pyplot as plt
from genetic_algorithm import strategies, play_game

def analyze_evolved_strategies(best_strategy):
    print("Analysis of Evolved Strategies:")
    print(f"Best evolved strategy: {best_strategy}")
    print("Characteristics:")
    print(f" - Always Cooperate: {best_strategy.count('C')}")
    print(f" - Always Defect: {best_strategy.count('D')}")
    print("Performance against fixed strategies:")
    for opponent in strategies:
        score, _ = play_game(
            lambda history: best_strategy[0] if not history else (best_strategy[1] if history[-1] == 'C' else best_strategy[2]),
            lambda history: opponent().play(history)
        )
        print(f" - Against {opponent.__name__}: Score = {score}")

# Performance against fixed strategies
def performance_against_fixed_strategies(strategy):
    print("Performance Against Fixed Strategies:")
    for opponent in strategies:
        score, _ = play_game(
            lambda history: strategy[0] if not history else (strategy[1] if history[-1] == 'C' else strategy[2]),
            lambda history: opponent().play(history)
        )
        print(f" - Against {opponent.__name__}: Score = {score}")

# Discussion of interesting findings
def discuss_findings():
    print("Discussion of Interesting Findings:")
    print(" - Strategies that always cooperate tend to perform well against cooperative opponents.")
    print(" - Strategies that defect can exploit cooperative opponents but may perform poorly against retaliatory strategies like TitForTat.")
    print(" - Mixed strategies (combining cooperation and defection) can balance the benefits of both approaches.")

# Visualization of fitness progression over generations
def plot_fitness_progression(fitness_history):
    generations = [gen for gen, _, _ in fitness_history]
    best_fitness = [best for _, best, _ in fitness_history]
    avg_fitness = [avg for _, _, avg in fitness_history]

    plt.figure(figsize=(10, 5))
    plt.plot(generations, best_fitness, label='Best Fitness')
    plt.plot(generations, avg_fitness, label='Average Fitness')
    plt.xlabel('Generation')
    plt.ylabel('Fitness')
    plt.title('Fitness Progression Over Generations')
    plt.legend()
    plt.show()