import numpy as np

class CurrentGeneration:
    solutions = []  # wszystkie losowe rozwiązania (pokolenie)
    population_fitnesses = []  # wszystkie oceny pokolenia

    def add_speciomen(self, specimen):
        self.solutions = np.append(self.solutions, specimen)

    def add_fitness(self, fitness):
        self.population_fitnesses = np.append(self.population_fitnesses, fitness)

    def change_solutions(self, solutions):
        self.solutions = solutions

    def change_fitnesses(self, fitnesses):
        self.population_fitnesses = fitnesses

    def best(self):
        return np.amin(self.population_fitnesses)

    def worst(self):
        return np.amax(self.population_fitnesses)

    def avg(self):
        return np.average(self.population_fitnesses)

    def clear_genetation(self):
        self.solutions = []
        self.population_fitnesses = []

    def delete_specimen(self, index, temp):
        temp_array = []
        for j in range(temp):
            temp_array.append(int((index*temp) + j))

        self.solutions = np.delete(self.solutions, temp_array)
        self.population_fitnesses = np.delete(self.population_fitnesses, index)

    def print(self):
        print(self.solutions)
        print(self.population_fitnesses)

class SavedData:
    bests = []
    worsts = []
    avreges = []

    def save_curr_gen_data(self,best,worst,avg):
        self.bests.append(best)
        self.worsts.append(worst)
        self.avreges.append(avg)

    def print(self):
        print("best: " + str(self.bests) + " worst: " + str(self.worsts) + " avg: " + str(self.avreges))

    def reset(self):
        self.bests = []
        self.worsts = []
        self.avreges = []
