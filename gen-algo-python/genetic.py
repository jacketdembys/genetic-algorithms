import random

# generate a guess, a random string from the geneSet
def _generate_parent(length, geneSet):
    genes = []
    while len(genes) < length:
        sampleSize = min(length - len(genes), len(geneSet))
        genes.extend(random.sample(geneSet, sampleSize))

    return ''.join(genes)

# mutate 
# the algorithm produces a new guess by mutating the current one
def _mutate(parent, geneSet):
    index = random.randrange(0, len(parent))
    childGenes = list(parent)
    newGene, alternate = random.sample(geneSet, 2)
    childGenes[index] = alternate \
        if newGene == childGenes[index] \
        else newGene
    return ''.join(childGenes)

# main loop
def get_best(get_fitness, targetLen, optimalFitness, geneSet,  display):
    # initialize the best parent to a random sequence of letters and calling the display function
    random.seed(10)
    bestParent = _generate_parent(targetLen, geneSet)
    bestFitness = get_fitness(bestParent)
    display(bestParent)
    if bestFitness >= optimalFitness:
        return bestParent

    # generate a guess, request the fitness and keep the guess of the better fitness
    while True:
        child = _mutate(bestParent, geneSet)
        childFitness = get_fitness(child)
        
        if bestFitness >= childFitness:
            continue
        
        display(child)
        
        if childFitness >= optimalFitness:
            return child
        bestFitness = childFitness
        bestParent = child