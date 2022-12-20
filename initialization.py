import json
import numpy as np
import random

import current_genetation
import fitness
import main

temp_curr_gen = current_genetation.CurrentGeneration()

cost_matrix = np.matrix
flow_matrix = np.matrix

init_best = 0
init_worst = 0
init_avg = 0


def readAll(cost_j, flow_j, machines):
    global cost_matrix
    global flow_matrix

    flow_matrix = np.zeros((machines, machines))
    cost_matrix = np.zeros((machines, machines))

    with open(cost_j) as json_file:
        data = json.load(json_file)

        for d in data:
            cost_matrix[d["source"], d["dest"]] = d["cost"]

    with open(flow_j) as json_file:
        data = json.load(json_file)

        for d in data:
            flow_matrix[d["source"], d["dest"]] = d["amount"]


def random_method(machines, x_size, y_size):
    global temp_curr_gen
    for i in range(main.starting_population_size):
        specimen_matrix = np.empty((x_size, y_size))
        specimen_matrix[:] = np.nan

        for j in range(machines):
            x = random.randrange(x_size)
            y = random.randrange(y_size)
            machine = random.randrange(machines - 1)
            not_added = True

            while not_added:
                if not machine in specimen_matrix:
                    if np.isnan(specimen_matrix[x][y]):
                        specimen_matrix[x][y] = machine
                        not_added = False
                    else:
                        x = (x + 1) % x_size
                        if x == 0:
                            y = (y + 1) % y_size
                else:
                    machine = (machine + 1) % machines

        temp_curr_gen.add_speciomen(specimen_matrix)
        temp_curr_gen.add_fitness(fitness.prepare_to_judge_specimen(specimen_matrix, machines))


def data_save():
    global init_best
    global init_worst
    global init_avg
    global temp_curr_gen

    init_worst = np.amax(temp_curr_gen.worst())
    init_best = np.amin(temp_curr_gen.best())
    init_avg = np.average(temp_curr_gen.avg())


def start(cost_json, flow_json, num_of_machines, x_size, y_size, curr_gen):
    global temp_curr_gen
    temp_curr_gen = curr_gen
    readAll(cost_json, flow_json, num_of_machines)
    random_method(num_of_machines, x_size, y_size)
    data_save()
    printing()
    return temp_curr_gen


def start_random(num_of_machines, x_size, y_size):
    global temp_curr_gen
    temp_curr_gen = current_genetation.CurrentGeneration()
    random_method(num_of_machines, x_size, y_size)
    return temp_curr_gen

def printing():
    print("\ndistance matrix")
    print(fitness.dist_matrix)

    print("\ncost matrix")
    print(cost_matrix)

    print("\nflow matrix")
    print(flow_matrix)

    print("\nall random solutions")
    print(temp_curr_gen.solutions)

    print("\ngraded solutions ")
    print(temp_curr_gen.population_fitnesses)

    print("\nbest grade")
    print(init_best)

    print("\nworst grade")
    print(init_worst)

    print("\navg grade")
    print(init_avg)
