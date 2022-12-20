import random
import fitness
import main
import numpy as np

selection_pressure = 0.3

def crossover(x, y, machines, curr_gen, two_clones, cross_prop):
    solution_size = x * y
    new_solutions = []
    curr_best = curr_gen.best()
    curr_best_sol = []
    # print(np.where(curr_gen.population_fitnesses == curr_best)[0][0])
    for i in range(x*y):
        curr_best_sol = np.append(curr_best_sol, curr_gen.solutions[x*y*np.where(curr_gen.population_fitnesses == curr_best)[0][0] + i])
    new_solutions = np.append(new_solutions, curr_best_sol)
    if x*y != machines:
        empty_spaces = True
    else:
        empty_spaces = False

    while len(new_solutions) != len(curr_gen.solutions):
        two_children = True

        parent_index_1 = random.randrange(len(curr_gen.population_fitnesses) - 1)
        parent_index_2 = random.randrange(len(curr_gen.population_fitnesses) - 1)
        while parent_index_1 == parent_index_2:
            parent_index_2 = random.randrange(len(curr_gen.population_fitnesses) - 1)
        # parent_index_2 = random.randrange(len(curr_gen.population_fitnesses) - 1)
        # rand = random.uniform(0, 1)
        # if rand < selection_pressure:
        #     while curr_gen.population_fitnesses[parent_index_1] == curr_gen.population_fitnesses[parent_index_2]:
        #         parent_index_2 = random.randrange(len(curr_gen.population_fitnesses) - 1)

        parent_1 = []
        parent_2 = []
        for i in range(solution_size):
            parent_1.append(curr_gen.solutions[parent_index_1 * solution_size + i])
            parent_2.append(curr_gen.solutions[parent_index_2 * solution_size + i])

        parent_1 = np.array(parent_1)
        parent_2 = np.array(parent_2)

        rand = random.uniform(0, 1)
        if rand < cross_prop:

            if (parent_1 == parent_2).all:
                two_children = two_clones

            # half_point = int(len(parent_1) / 2)
            half_point = random.randrange(len(parent_1)-1)


            if len(new_solutions) != len(curr_gen.solutions):
                new_child1 = np.zeros(solution_size)
                new_child1[:] = np.nan

                new_child1[0:half_point] = parent_2[0:half_point]
                new_child1 = fill(new_child1, parent_1, half_point,empty_spaces)

                new_solutions = np.append(new_solutions, new_child1)

            if len(new_solutions) != len(curr_gen.solutions) and two_children:
                new_child2 = np.zeros(solution_size)
                new_child2[:] = np.nan

                new_child2[0:half_point] = parent_1[0:half_point]
                new_child2 = fill(new_child2, parent_2, half_point, empty_spaces)

                new_solutions = np.append(new_solutions, new_child2)
        else:
            if len(new_solutions) != len(curr_gen.solutions):
                new_solutions = np.append(new_solutions, parent_1)

    curr_gen.change_solutions(new_solutions)
    return curr_gen


def fill(specimen, parent, specimen_ind, empty_spaces):
    not_checked = True
    while not_checked:
        not_checked = False
        for i in parent:
            if not np.isnan(i):
                if i not in specimen:
                    specimen = fixer(specimen, i, specimen_ind,empty_spaces)
                    not_checked = True
                    specimen_ind += 1
    return specimen


def fixer(specimen, number, specimen_ind, empty_spaces):
    rand = random.randrange(1)
    if specimen_ind+rand < len(specimen) and empty_spaces:
        specimen[specimen_ind+rand] = number
    else:
        specimen[specimen_ind] = number
    return specimen


def crossover2(x, y, machines, curr_gen, two_clones, cross_prop):
    solution_size = x * y
    new_solutions = []
    curr_best = curr_gen.best()
    curr_best_sol = []
    # print(np.where(curr_gen.population_fitnesses == curr_best)[0][0])
    for i in range(x*y):
        curr_best_sol = np.append(curr_best_sol, curr_gen.solutions[x*y*np.where(curr_gen.population_fitnesses == curr_best)[0][0] + i])
    new_solutions = np.append(new_solutions, curr_best_sol)
    if x*y != machines:
        empty_spaces = True
    else:
        empty_spaces = False

    while len(new_solutions) != len(curr_gen.solutions):
        two_children = True

        parent_index_1 = random.randrange(len(curr_gen.population_fitnesses) - 1)
        parent_index_2 = random.randrange(len(curr_gen.population_fitnesses) - 1)
        while parent_index_1 == parent_index_2:
            parent_index_2 = random.randrange(len(curr_gen.population_fitnesses) - 1)
        # parent_index_2 = random.randrange(len(curr_gen.population_fitnesses) - 1)
        # rand = random.uniform(0, 1)
        # if rand < selection_pressure:
        #     while curr_gen.population_fitnesses[parent_index_1] == curr_gen.population_fitnesses[parent_index_2]:
        #         parent_index_2 = random.randrange(len(curr_gen.population_fitnesses) - 1)

        parent_1 = []
        parent_2 = []
        for i in range(solution_size):
            parent_1.append(curr_gen.solutions[parent_index_1 * solution_size + i])
            parent_2.append(curr_gen.solutions[parent_index_2 * solution_size + i])

        parent_1 = np.array(parent_1)
        parent_2 = np.array(parent_2)

        rand = random.uniform(0, 1)
        if rand < cross_prop:

            if (parent_1 == parent_2).all:
                two_children = two_clones

            # half_point = int(len(parent_1) / 2)
            half_point = random.randrange(len(parent_1)-1)


            if len(new_solutions) != len(curr_gen.solutions):
                new_child1 = np.zeros(solution_size)
                new_child1[:] = np.nan

                new_child1[0:half_point] = parent_2[0:half_point]
                new_child1[half_point: solution_size] = parent_1[half_point: solution_size]

                new_child1 = fix(new_child1, parent_1, half_point, half_point, machines)

                new_solutions = np.append(new_solutions, new_child1)

            if len(new_solutions) != len(curr_gen.solutions) and two_children:
                new_child2 = np.zeros(solution_size)
                new_child2[:] = np.nan

                new_child2[0:half_point] = parent_1[0:half_point]
                new_child2[half_point: solution_size] = parent_2[half_point: solution_size]

                new_child2 = fix(new_child2, parent_2, half_point, half_point, machines)

                new_solutions = np.append(new_solutions, new_child2)
        else:
            if len(new_solutions) != len(curr_gen.solutions):
                new_solutions = np.append(new_solutions, parent_1)

    curr_gen.change_solutions(new_solutions)
    return curr_gen

def fix(specimen, parent, specimen_ind, half_point, machines):
    not_checked = True
    missing = []
    while not_checked:
        not_checked = False
        for i in parent:
            if not np.isnan(i):
                if i not in specimen and i not in missing:
                    missing = np.append(missing, i)
                    not_checked = True
                    specimen_ind += 1
    miss_index = 0
    for i in range(half_point, len(specimen)):
        if not np.isnan(specimen[i]):
            if len(np.where(specimen == specimen[i])[0]) > 1:
                if len(missing) > miss_index:
                    specimen[i] = missing[miss_index]
                    miss_index += 1
                else:
                    specimen[i] = np.nan

    for i in range(machines):
        if i not in specimen:
            specimen[np.where(np.isnan(specimen))[0][0]] = i

    return specimen

