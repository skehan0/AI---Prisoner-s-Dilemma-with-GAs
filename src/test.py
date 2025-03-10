import unittest
from genetic_algorithm import random_genome, init_population, play_game, fitness, tournament_selection, mutate, crossover, genotype_length, population_size, strategies

class TestGeneticAlgorithm(unittest.TestCase):

    def test_random_genome(self):
        genome = random_genome(genotype_length)
        self.assertEqual(len(genome), genotype_length, "Genome length should be correct")
        self.assertTrue(all(gene in ['C', 'D'] for gene in genome), "Genome should contain only 'C' or 'D'")

    def test_init_population(self):
        population = init_population(population_size)
        self.assertEqual(len(population), population_size, "Population size should be correct")
        self.assertTrue(all(len(ind) == genotype_length for ind in population), "Each individual should have the correct genome length")

    def test_play_game(self):
        strategy1 = lambda history: 'C'
        strategy2 = lambda history: 'D'
        score1, score2 = play_game(strategy1, strategy2, rounds=10)
        self.assertEqual(score1, 0, "Score1 should be correct")
        self.assertEqual(score2, 50, "Score2 should be correct")

    def test_fitness(self):
        strategy = ['C', 'C', 'D']
        score = fitness(strategy)
        self.assertIsInstance(score, int, "Fitness score should be an integer")

    def test_tournament_selection(self):
        population = init_population(population_size)
        fitness_values = [fitness(ind) for ind in population]
        selected = tournament_selection(population, fitness_values)
        self.assertEqual(len(selected), population_size, "Selected population size should be correct")

    def test_mutate(self):
        individual = ['C', 'D', 'C']
        original_individual = individual.copy()
        
        # Set mutation rate to 1 to ensure mutation occurs
        mutation_rate = 1.0
        
        mutated_individual = mutate(individual, mutation_rate)
        
        self.assertNotEqual(original_individual, mutated_individual, "Mutation should change the genome")
        self.assertEqual(len(original_individual), len(mutated_individual), "Genome length should remain the same")

    def test_crossover(self):
        parent1 = ['C', 'D', 'C']
        parent2 = ['D', 'C', 'D']
        
        child1, child2 = crossover(parent1, parent2)
        
        self.assertEqual(len(parent1), len(child1), "Child genome length should be the same as parent")
        self.assertEqual(len(parent2), len(child2), "Child genome length should be the same as parent")
        
        # Check that children are a combination of parents
        self.assertTrue(any(child1[i] != parent1[i] for i in range(len(parent1))), "Child1 should be a combination of parents")
        self.assertTrue(any(child2[i] != parent2[i] for i in range(len(parent2))), "Child2 should be a combination of parents")

if __name__ == '__main__':
    unittest.main()