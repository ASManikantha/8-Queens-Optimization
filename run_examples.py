from simulated_annealing import simulated_annealing
from genetic_algorithm import genetic_algorithm

def main():
    print("Running Simulated Annealing...")
    sa_solution, sa_cost = simulated_annealing()
    print("SA Solution:", sa_solution)
    print("SA Cost:", sa_cost)

    print("\nRunning Genetic Algorithm...")
    ga_solution, ga_fitness = genetic_algorithm()
    print("GA Solution:", ga_solution)
    print("GA Fitness:", ga_fitness)

if __name__ == "__main__":
    main()
