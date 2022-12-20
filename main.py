import initialization
import current_genetation
import selection
import crossover
import mutation
import fitness
import matplotlib.pyplot as pyl
import numpy as np

starting_population_size = 100
number_of_generations = 200


def start_all(type, population_size, num_of_gen, is_roulette, beta, tournament_size_proc, two_clones, cross_prop, mutation_rate,
              mutation_severnes):

    global starting_population_size
    global number_of_generations

    number_of_generations = num_of_gen
    starting_population_size = population_size

    all_data = current_genetation.SavedData()
    curr_gen = current_genetation.CurrentGeneration()

    machines = 0
    x = 0
    y = 0
    json_cost_name = type + '_cost.json'
    json_flow_name = type + '_flow.json'

    if type == 'easy':
        machines = 9
        x = 3
        y = 3

    if type == 'flat':
        machines = 12
        x = 1
        y = 12

    if type == 'hard':
        machines = 24
        x = 5
        y = 6

    curr_gen = initialization.start(json_cost_name, json_flow_name, machines, x, y, curr_gen)

    all_data.save_curr_gen_data(initialization.init_best, initialization.init_worst, initialization.init_avg)

    for i in range(number_of_generations):
        print(i)

        if is_roulette:
            curr_gen = selection.roulette_selection(x * y, curr_gen, beta)
        else:
            curr_gen = selection.tournament_selection(x * y, curr_gen, tournament_size_proc)

        curr_gen = crossover.crossover2(x, y, machines, curr_gen, two_clones, cross_prop)

        curr_gen = mutation.mutations(x * y, curr_gen, mutation_rate, mutation_severnes)

        curr_gen = fitness.judge_curr_gen(machines, x, y, curr_gen)

        print(curr_gen.population_fitnesses)
        print()
        all_data.save_curr_gen_data(curr_gen.best(), curr_gen.worst(), curr_gen.avg())
        print(curr_gen.best())
        print(curr_gen.worst())
        print(curr_gen.avg())

    pyl.plot(range(len(all_data.bests)), all_data.bests, label='best')
    pyl.plot(range(len(all_data.worsts)), all_data.worsts, label='worst')
    pyl.plot(range(len(all_data.avreges)), all_data.avreges, label="avrege")
    curr_gen.print()
    print(all_data.bests)
    print(all_data.worsts)
    print(all_data.avreges)
    pyl.legend()
    pyl.show()


def start_all_random(type, population_size, num_of_gen):
    global starting_population_size
    global number_of_generations

    number_of_generations = num_of_gen
    starting_population_size = population_size

    all_data = current_genetation.SavedData()
    curr_gen = current_genetation.CurrentGeneration()

    machines = 0
    x = 0
    y = 0
    json_cost_name = type + '_cost.json'
    json_flow_name = type + '_flow.json'

    if type == 'easy':
        machines = 9
        x = 3
        y = 3

    if type == 'flat':
        machines = 12
        x = 1
        y = 12

    if type == 'hard':
        machines = 24
        x = 5
        y = 6

    curr_gen = initialization.start(json_cost_name, json_flow_name, machines, x, y, curr_gen)
    all_data.save_curr_gen_data(initialization.init_best, initialization.init_worst, initialization.init_avg)

    for i in range(number_of_generations):
        print(i)
        curr_gen = initialization.start_random(machines, x, y)
        all_data.save_curr_gen_data(curr_gen.best(), curr_gen.worst(), curr_gen.avg())

    pyl.plot(range(len(all_data.bests)), all_data.bests, label='best')
    pyl.plot(range(len(all_data.worsts)), all_data.worsts, label='worst')
    pyl.plot(range(len(all_data.avreges)), all_data.avreges, label="avrege")
    curr_gen.print()
    print(all_data.bests)
    print(np.amin(all_data.bests))
    print(all_data.worsts)
    print(all_data.avreges)
    pyl.legend()
    pyl.show()

if __name__ == '__main__':
    #typ, wielkość populacji, ilosc generacji czy_ruletka, beta, wielkosc turnamentu, czy 2 kolny, prawdop_mutacji, wielkosc mutacji
    start_all('hard', 100, 100, True, 93, 0.2, True, 0.8, 0.3, 3)
    # start_all_random('hard', 100, 100)

    # beta  wieksze niż ~83 best właściwie stałe mniejsze wacha się
    #pytanie o prawdopodobieństwo krzyżowania
    #18146+17712+17324=