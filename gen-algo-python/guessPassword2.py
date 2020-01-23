import datetime
import genetic

# mfunction of the main genetic search
def guess_password(target):
    geneSet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
    startTime = datetime.datetime.now()

    def fnGetFitness(genes):
        return get_fitness(genes, target)

    def fnDisplay(genes):
        display(genes, target, startTime)

    optimalFitness = len(target)
    genetic.get_best(fnGetFitness, len(target), optimalFitness, geneSet, fnDisplay)

# display what is happening
def display(guess, target, startTime):
    timeDiff = datetime.datetime.now() - startTime
    fitness = get_fitness(guess, target)
    print("{0}\t{1}\t{2}".format(guess, fitness, str(timeDiff)))

# fitness
# the fitness value is feedback provided to guide the search toward the solution 
def get_fitness(guess, target):
    return sum(1 for expected, actual in zip(target, guess) if expected == actual)

# target string to be searched
def test_Hello_World():
    target = "Hello World"
    guess_password(target)

# main funciton
if __name__ == "__main__":
    test_Hello_World()
