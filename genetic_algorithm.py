import numpy as np
import random

# Parameters
POPULATION_SIZE = 100
MUTATION_RATE = 0.01
GENERATIONS = 1000

# Function to create a random individual (solution)
def create_individual():
    return list(np.random.permutation(8))

# Function to calculate the fitness of an individual
def fitness(individual):
    # Number of pairs of queens that are attacking each other
    clashes = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if individual[i] == individual[j] or \
               abs(individual[i] - individual[j]) == abs(i - j):
                clashes += 1
    return 28 - clashes  # Maximum fitness is 28 (no clashes)

# Function to select parents based on fitness
def select_parents(population):
    sorted_population = sorted(population, key=fitness, reverse=True)
    return sorted_population[:2]  # Select top 2 individuals

# Function to crossover (reproduce) two parents to create a child
def crossover(parent1, parent2):
    point = random.randint(1, 7)
    child = parent1[:point] + [x for x in parent2 if x not in parent1[:point]]
    return child

# Function to mutate an individual
def mutate(individual):
    if random.random() < MUTATION_RATE:
        i, j = random.sample(range(8), 2)
        individual[i], individual[j] = individual[j], individual[i]

# Main genetic algorithm function
def genetic_algorithm():
    population = [create_individual() for _ in range(POPULATION_SIZE)]
    for generation in range(GENERATIONS):
        population = sorted(population, key=fitness, reverse=True)
        if fitness(population[0]) == 28:
            print(f"Solution found in generation {generation}: {population[0]}")
            return population[0]

        new_population = []
        for _ in range(POPULATION_SIZE // 2):
            parents = select_parents(population)
            child1 = crossover(parents[0], parents[1])
            child2 = crossover(parents[1], parents[0])
            mutate(child1)
            mutate(child2)
            new_population.append(child1)
            new_population.append(child2)

        population = new_population

    print("No optimal solution found.")
    return None

# Run the genetic algorithm
if __name__ == "__main__":
    solution = genetic_algorithm()
    if solution:
        print("Solution:", solution)
