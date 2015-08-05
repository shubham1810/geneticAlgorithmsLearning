import random
import string

CROSSOVER_RATE = 0.9
MUTATION_RATE = 0.02
POPULATION_SIZE = 4096
MAX_ALLOWABLE_GENERATIONS = 200

CHARACTERS = string.letters + string.digits + string.punctuation + string.whitespace


def random_number():
    return random.random()


class Chromosome:

    str = ''
    fitness = 1024

    def __init__(self, str='', fitness=1024):
        self.str = str
        self.fitness = fitness


def generate_string(length):
    return "".join([random.choice(CHARACTERS) for i in xrange(length)])


def fitness(value, target):
    return sum([abs(ord(value[j]) - ord(target[j])) for j in xrange(len(target))])


def selection_function(pop):
    return random.randint(0, len(pop)/3)


def mutate(val):

    for z in xrange(len(val)):

        if random_number() < MUTATION_RATE:

            val = val[:z] + random.choice(CHARACTERS) + val[z+1:]

    return val


def crossover(offspring_one, offspring_two):

    if random_number() < CROSSOVER_RATE:
        crossover_val = int(random_number() * len(offspring_one))
        t1 = offspring_one[:crossover_val]+offspring_two[crossover_val:]
        t2 = offspring_two[:crossover_val]+offspring_one[crossover_val:]

        return t1, t2

    return offspring_one, offspring_two


if __name__ == '__main__':
    tgt = str(raw_input('Enter the target value: '))

    population = [Chromosome() for i in range(POPULATION_SIZE)]

    for i in range(POPULATION_SIZE):
        population[i].str = generate_string(len(tgt))
        population[i].fitness = fitness(population[i].str, tgt)

    generations_required = 0

    solution_found = False

    while not solution_found:

        for i in xrange(POPULATION_SIZE):
            population[i].fitness = fitness(population[i].str, tgt)

        population = sorted(population, key=lambda x: x.fitness)
        print "Generation " + str(generations_required) + " and value :\t" + population[0].str

        if not population[0].fitness:
            solution_found = True
            print "Finally the solution is found!"


        temp = []

        while len(temp) < POPULATION_SIZE:

            offspring1 = population[selection_function(population)].str
            offspring2 = population[selection_function(population)].str

            offspring1, offspring2 = crossover(offspring1, offspring2)

            mutate(offspring1)
            mutate(offspring2)

            temp.append(Chromosome(offspring1, fitness(offspring1, tgt)))
            temp.append(Chromosome(offspring2, fitness(offspring2, tgt)))


        population, temp = temp, population
        generations_required += 1

        if generations_required > MAX_ALLOWABLE_GENERATIONS:
            print "Maximum generations exceeded"
            break