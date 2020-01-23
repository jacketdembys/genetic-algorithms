# hello world genetic algorithm program
import random
import datetime

# genes to be used when building the guesses
geneSet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
target = "Hello World!"

# generate a guess, a random string from the geneSet
def generate_parent(length):
    genes = []
    while len(genes) < length:
        sampleSize = min(length - len(genes), len(geneSet))
        genes.extend(random.sample(geneSet, sampleSize))

    return ''.join(genes)

# fitness
# the fitness value is feedback provided to guide the search toward the solution 
def get_fitness(guess):
    return sum(1 for expected, actual in zip(target, guess) if expected == actual)

# mutate 
# the algorithm produces a new guess by mutating the current one
def mutate(parent):
    index = random.randrange(0, len(parent))
    childGenes = list(parent)
    newGene, alternate = random.sample(geneSet, 2)
    childGenes[index] = alternate \
        if newGene == childGenes[index] \
        else newGene
    return ''.join(childGenes)

# display what is happening
def display(guess):
    timeDiff = datetime.datetime.now() - startTime
    fitness = get_fitness(guess)
    print("{0}\t{1}\t{2}".format(guess, fitness, str(timeDiff)))

if __name__ == "__main__":
    
    # initialize the best parent to a random sequence of letters and calling the display function
    random.seed(10)
    startTime = datetime.datetime.now()
    bestParent = generate_parent(len(target))
    bestFitness = get_fitness(bestParent)
    display(bestParent)

    # generate a guess, request the fitness and keep the guess of the better fitness
    while True:
        child = mutate(bestParent)
        childFitness = get_fitness(child)
        if bestFitness >= childFitness:
            continue
        display(child)
        if childFitness >= len(bestParent):
            break
        bestFitness = childFitness
        bestParent = child


