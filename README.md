# 8-Queens Optimization

This repository contains implementations of two optimization algorithms for solving the classic 8-Queens problem: Simulated Annealing and Genetic Algorithm. The goal of the 8-Queens problem is to place eight queens on an 8x8 chessboard such that no two queens can attack each other.

## Project Structure

- `simulated_annealing.py`: Contains the implementation of the Simulated Annealing algorithm.
- `genetic_algorithm.py`: Contains the implementation of the Genetic Algorithm.


## Simulated Annealing Algorithm for 8-Queens

1. Initialization:
Start with a randomly generated state (solution).
Define initial temperature and cooling rate.

2. Iterative Process:
Move: Randomly alter the state to generate a new candidate solution.
Evaluate: Calculate the energy (or cost) of both the current state and the new state.
Acceptance Criteria: Decide whether to move to the new state based on the energy difference and the current temperature.
Cooling: Gradually decrease the temperature over iterations.

3. Termination:
Repeat the process until a stopping criterion is met (e.g., a fixed number of iterations or convergence to a satisfactory solution).


## Genetic Algorithm for 8-Queens

1. Initialization:
Create Initial Population: Generate a set of random solutions (individuals). Each solution is a permutation of the numbers 0 to 7, representing the positions of the queens.

2. Iterative Process:
Evaluate Fitness: Assess the fitness of each individual in the population. The fitness is determined by the number of non-attacking pairs of queens (fewer clashes mean higher fitness).
Selection: Choose individuals from the current population to act as parents for the next generation. Selection is often based on fitness, with better solutions having a higher chance of being chosen.
Crossover (Reproduction): Create new individuals (children) by combining traits from two parent individuals. This involves exchanging segments of the parent solutions.
Mutation: Introduce random changes to some individuals to maintain genetic diversity and explore new solutions. For example, randomly swap two queens’ positions in an individual.
Replacement: Replace some or all of the old population with new individuals (children) to form the next generation.

3. Termination:
Repeat the process for a specified number of generations or until a stopping criterion is met (e.g., a solution with optimal fitness is found).
