import math
import main
import numpy as np
import random


def roulette_selection(solution_size, curr_gen, beta):
    temp_list = []
    worst = curr_gen.worst()

    for i in range(main.starting_population_size):
        temp_list.append(math.exp(-beta * curr_gen.population_fitnesses[i]/worst))
    temp_sum = sum(temp_list)

    probability = [val/temp_sum for val in temp_list]

    winners = []
    winners = np.append(winners, np.where(curr_gen.population_fitnesses == curr_gen.best())[0][0])
    while len(winners) < main.starting_population_size:
        winners = np.append(winners, pick(probability))

    curr_gen = parents_chosen(curr_gen, solution_size, winners)

    return curr_gen


def pick(probability):
    temp_sum = 0

    for i in range(len(probability)):
        temp_sum += probability[i]
        if random.random() <= temp_sum:
            return i


def tournament_selection(solution_size, curr_gen, turnament_size_perc):
    N = int(main.starting_population_size * turnament_size_perc) #wielkość turnieju
    M = int(main.starting_population_size) #ilość turniejów

    #wybór uczestnikow turnieju (bez powtórzeń)
    winners = []
    winners = np.append(winners, np.where(curr_gen.population_fitnesses == curr_gen.best())[0][0])
    while M > len(winners):
        participants_index = []
        participants_fitness = []
        for i in range(N):
            not_chose = True
            while not_chose:
                rand = random.randrange(main.starting_population_size)
                if rand not in participants_index:
                    participants_index = np.append(participants_index, rand)
                    participants_fitness = np.append(participants_fitness, int(curr_gen.population_fitnesses[rand]))
                    not_chose = False
        winner = participants_index[np.where(participants_fitness == np.amin(participants_fitness))]

        if len(np.where(winners == winner)[0]) <= (N * 1):
            winners = np.append(winners, participants_index[np.where(participants_fitness == np.amin(participants_fitness))])

    curr_gen = parents_chosen(curr_gen, solution_size, winners)

    return curr_gen


def parents_chosen(curr_gen, solution_size, winners):
    temp_solutions = []
    temp_fitnesses = []

    for i in range(main.starting_population_size):
        temp_fitnesses = np.append(temp_fitnesses, curr_gen.population_fitnesses[int(winners[i])])
        temp_solution = []
        for j in range(solution_size):
            temp_solution = np.append(temp_solution, curr_gen.solutions[int(winners[i]*solution_size + j)])
        temp_solutions = np.append(temp_solutions, temp_solution)

    curr_gen.solutions = temp_solutions
    curr_gen.population_fitnesses = temp_fitnesses

    return curr_gen