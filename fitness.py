import numpy as np
import initialization
import main

dist_matrix = np.matrix


def manhattan_dist(matrix, machines, temp=None):
    global dist_matrix

    dist_matrix = np.zeros((machines, machines))

    for i in range(machines):
        for j in range(machines):
            machine_i = np.where(matrix == i)
            machine_j = np.where(matrix == j)

            if machine_j != np.nan and machine_i != np.nan:
                dist_matrix[i][j] = np.abs(machine_i[0] - machine_j[0]) + np.abs(machine_i[1] - machine_j[1])
            else:
                dist_matrix[i][j] = 0


def fitness_method(machines):
    grade = 0

    for i in range(machines):
        for j in range(machines):
            grade += initialization.flow_matrix[i][j] * initialization.cost_matrix[i][j] * dist_matrix[i][j]
    return grade


def prepare_to_judge_specimen(specimen, machines, temp = None):
    manhattan_dist(specimen, machines, temp)
    return fitness_method(machines)

def judge_curr_gen(machines, x, y, curr_gen):
    new_fitneses = []
    for i in range(main.starting_population_size):
        curr_specimen = []
        for j in range(x*y):
            curr_specimen = np.append(curr_specimen, curr_gen.solutions[i*x*y + j])
        curr_specimen = np.reshape(curr_specimen, (x, y))
        new_fitneses = np.append(new_fitneses, prepare_to_judge_specimen(curr_specimen, machines))
    curr_gen.change_fitnesses(new_fitneses)
    return curr_gen

