import random
import string

CROSSOVER_RATE = 0.7
MUTATION_RATE = 0.001
POPULATION_SIZE = 100



class Chromosome:

    def __init__(self, bits="", fitness=0.0):
        self.bits = bits
        self.fitness = fitness