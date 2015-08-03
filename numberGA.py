import random
import string

CROSSOVER_RATE = 0.7
MUTATION_RATE = 0.001
POPULATION_SIZE = 100
CHROMOSOME_LENGTH = 300
GENE_LENGTH = 4
MAX_ALLOWABLE_GENERATIONS = 500


def random_number():
    return random.random()


class Chromosome:

    bits = ""
    fitness = 0.0

    def __init__(self, bits="", fitness=0.0):
        self.bits = bits
        self.fitness = fitness


def print_gene_symbol(val):

    if val < 10:
        print str(val),
    else:

        if val == 10:
            print '+',
        elif val == 11:
            print '-',
        elif val == 12:
            print '*',
        elif val == 13:
            print '/',

    return


def get_random_bits(length):

    bits = ''

    for i in xrange(length):
        if random_number() > 0.5:
            bits += '1'
        else:
            bits += '0'

    return bits


def bin_to_dec(bits):
    return int(bits, 2)


def assign_fitness(bits, target):

    #print bits

    #buffer = [None] * int(CHROMOSOME_LENGTH/GENE_LENGTH)
    #print len(buffer)
    buffer = []

    num_elements, buffer = parse_bits(bits, buffer)
    #print len(buffer), num_elements, buffer

    result = 0.0
    #print buffer[num_elements]

    for x in range(0, num_elements-1, 2):

        if buffer[x] == 10:
            result += buffer[x+1]
        elif buffer[x] == 11:
            result -= buffer[x+1]
        elif buffer[x] == 12:
            result *= buffer[x+1]
        elif buffer[x] == 13:
            result /= buffer[x+1]

    #print result
    if result == float(target):
        return 999.0
    else:
        return 1.0/float(abs(float(target) - result))


def print_chromosome(bits):

    buffer = []

    num_elements, buffer = parse_another_bits(bits, buffer)

    for x in range(num_elements):
        print_gene_symbol(buffer[x])

    return


def parse_another_bits(bits, buffer):

    c_buff = 0

    b_operator = True

    this_gene = 0

    for x in range(0, CHROMOSOME_LENGTH, GENE_LENGTH):
        this_gene = bin_to_dec(bits[x:x+GENE_LENGTH])
        #print this_gene
        #print this_gene, bits[x:x+GENE_LENGTH]

        if b_operator:

            if (this_gene < 10) or (this_gene > 13):
                continue
            else:
                b_operator = False
                buffer.append(this_gene)
        else:

            if this_gene > 9:
                continue
            else:
                b_operator = True
                buffer.append(this_gene)

    c_buff = len(buffer)

    for x in range(c_buff-1):
        #print buffer
        if buffer[x] == 13 and buffer[x+1] == 0:
            buffer[x] = 10

    return c_buff, buffer


def parse_bits(bits, buffer):

    c_buff = 0

    b_operator = True

    this_gene = 0

    for x in range(0, CHROMOSOME_LENGTH, GENE_LENGTH):
        this_gene = bin_to_dec(bits[x:x+GENE_LENGTH])
        #print this_gene, bits[x:x+GENE_LENGTH]

        if b_operator:

            if (this_gene < 10) or (this_gene > 13):
                continue
            else:
                b_operator = False
                buffer.append(this_gene)
        else:

            if this_gene > 9:
                continue
            else:
                b_operator = True
                buffer.append(this_gene)

    c_buff = len(buffer)

    for x in range(c_buff-1):
        #print buffer
        if buffer[x] == 13 and buffer[x+1] == 0:
            buffer[x] = 10

    return c_buff, buffer


def roulette(fit, pop):

    slice_val = float(random_number() * fit)
    fitness_so_far = 0.0

    for u in range(POPULATION_SIZE):
        fitness_so_far += pop[u].fitness

        if fitness_so_far >= slice_val:
            return pop[u].bits

    return ''


def mutate(bits):

    #new_bits = ''

    for k in range(len(bits)):
        #print type(bits[k]), type(k)
        #new_bits += bits[k]

        if random_number() < MUTATION_RATE:
            #print "changes"
            if bits[k] == "1":
                bits = bits[:k] + '0' + bits[k+1:]
            else:
                bits = bits[:k] + '1' + bits[k+1:]

    return bits


def crossover(ofs1, ofs2):

    if random_number() < CROSSOVER_RATE:

        crossover_val = int(random_number() * CHROMOSOME_LENGTH)
        t1 = ofs1[0:crossover_val] + ofs2[crossover_val:CHROMOSOME_LENGTH]
        t2 = ofs2[0:crossover_val] + ofs1[crossover_val:CHROMOSOME_LENGTH]
        return t1, t2

    return ofs1, ofs2


if __name__ == '__main__':

    while True:
        population = [Chromosome() for i in range(POPULATION_SIZE)]

        target_value = float(input("Enter a target Value: "))

        for i in range(POPULATION_SIZE):
            population[i].bits = get_random_bits(CHROMOSOME_LENGTH)
            #print population[i].bits, "************************"
            population[i].fitness = 0.0


        #for i in range(POPULATION_SIZE):
        #    print population[i].bits, "************************"

        #print "======================================"

        generations_required_for_solution = 0

        b_found = False

        while not b_found:
            total_fitness = 0.0

            #for i in range(POPULATION_SIZE):
            #    print population[i].bits, "*************************************"

            for i in range(POPULATION_SIZE):
                population[i].fitness = assign_fitness(population[i].bits, target_value)
                #print population[i].fitness
                total_fitness += population[i].fitness
                #print total_fitness

            #print "===================================================="

            fit_val = sorted(population, key=lambda c: c.fitness)[0]
            print "Current Generation: " + str(generations_required_for_solution) + " status is fitness: " + str(fit_val.fitness) + " solution: "
            print_chromosome(fit_val.bits)

            for i in xrange(POPULATION_SIZE):
                if population[i].fitness == 999.0:
                    print "Solution found in " + str(generations_required_for_solution) + " generations!"
                    print ''
                    print_chromosome(population[i].bits)
                    b_found = True
                    break

            temp = []
            c_pop = 0

            while len(temp) < POPULATION_SIZE:

                offspring1 = roulette(total_fitness, population)
                #print offspring1
                offspring2 = roulette(total_fitness, population)

                offspring1, offspring2 = crossover(offspring1, offspring2)

                mutate(offspring1)
                mutate(offspring2)

                temp.append(Chromosome(offspring1, 0.0))
                temp.append(Chromosome(offspring2, 0.0))

            #population = temp
            for z in range(POPULATION_SIZE):
                population[z] = temp[z]

            generations_required_for_solution += 1

            if generations_required_for_solution > MAX_ALLOWABLE_GENERATIONS:

                print "No solutions in this test run"
                b_found = True


        print ''
        print ''