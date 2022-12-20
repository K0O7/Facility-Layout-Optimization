import random
import main

def mutations(specimen_size, curr_gen, mutation_rate, mutation_severnes):
    print()
    for i in range(main.starting_population_size):
        rand = random.uniform(0, 1)
        if rand < mutation_rate:
            for j in range(mutation_severnes):
                rand_index = random.randrange(specimen_size-1)
                rand_index2 = (rand_index + 1) % specimen_size

                temp = curr_gen.solutions[i*specimen_size + rand_index]

                curr_gen.solutions[i * specimen_size + rand_index] = curr_gen.solutions[i*specimen_size + rand_index2]
                curr_gen.solutions[i * specimen_size + rand_index2] = temp
    return curr_gen