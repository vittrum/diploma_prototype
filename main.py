import ga
import numpy

num_generations = 5
num_mating_parents = 4
inputs = [4, -2, 3.5, 5, -11, -4.7]
num_weights = 6
sol_per_pop = 8
pop_size = (sol_per_pop, num_weights)
new_population = numpy.random.uniform(low=-4.0, high=4.0, size=pop_size)

for _ in range(num_generations):
    fitness = ga.cal_pop_fitness(inputs, new_population)
    parents = ga.select_mating_pool(new_population, fitness, num_mating_parents)
    offspring_crossover = ga.crossover(parents, offspring_size=(pop_size[0] - parents.shape[0], num_weights))
    offspring_mutation = ga.mutation(offspring_crossover)
    new_population[0:parents.shape[0], :] = parents
    new_population[parents.shape[0]:, :] = offspring_mutation