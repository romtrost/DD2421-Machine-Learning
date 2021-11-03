import monkdata as m
import dtree as d
import drawtree_qt5 as dt
import random
import matplotlib.pyplot as plt
import statistics
import numpy as np

# Seperating training data into training and validation sets
def partition(data, fraction):
    ldata = list(data)
    random.shuffle(ldata)
    breakPoint = int(len(ldata) * fraction)
    return ldata[:breakPoint], ldata[breakPoint:]

def pruning(data, fraction):
    
    monkTrain, monkVal = partition(data, fraction)  # Seperating data
    tree = d.buildTree(monkTrain, m.attributes) # Building tree with training data
    treePruned = d.allPruned(tree) # Returns a list of trees, where each tree has a different node pruned
    
    maxScore = d.check(tree, monkVal) # Gets current best validation score, which is from the original tree
    valScores = [maxScore] # List of scores, assign first value = validation performance of orginial tree
    bestTrees = [tree] # List of trees associated with highest validation scores, 1st value = orig. tree
    
    pruned = 0 # Counter keeping track of pruning
    
    while (True):
    
        pruned = pruned + 1
        
        valPerf = [] # Holds the validation performance for all pruned trees of this iteration
        
        for i in range(0, len(treePruned)):
            valPerf.append(d.check(treePruned[i], monkVal))
             
        maxPerf = max(valPerf) # Highest validation score
        maxIndex = valPerf.index(maxPerf) # Gets index of highest validation score
        
        valScores.append(maxPerf) # Adds highest score to valScores
        bestTrees.append(treePruned[maxIndex]) # Adds tree with highest score to bestTrees
        
        if valScores[pruned] < valScores[pruned - 1]: # If new best score is worst than the last, STOP
            valScores.pop()
            bestTrees.pop()
            break
        
        treePruned = d.allPruned(treePruned[maxIndex])
        
    bestValScore = valScores[-1] # Best score is the last score in valScores
    bestTree = bestTrees[-1] # Best tree is the last tree in bestTrees
        
    #print(valScores)
    #print(bestTrees) 
    #dt.drawTree(bestTree) # Draws bestTree
    
    return bestValScore, bestTree

def testPruned(trainData, testData):
    
    fractions = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
    testScores = []
    
    for fraction in fractions:
        _, tree = pruning(trainData, fraction)  # Gets best pruned tree
        testScore = d.check(tree, testData)     # Tests tree against test dataset 
        testScores.append(testScore)            # Adds score to list testScores
        
    return fractions, testScores

allData = [] # Contains all data
# Main loop
for i in range(0, 100): 
    
    fractions = testPruned(m.monk3, m.monk3test)[0]
    test = testPruned(m.monk3, m.monk3test)[1]
    allData.append(test)
    plt.scatter(fractions, test) # Scatters data in a plot

allData = np.transpose(allData) # Puts tests scores in each row --> 6 rows (fractions), n columns (n iterations/runs)
#print(allData)


means = [] # Assigns mean of values for every fraction
stdev = [] # Assigns standard deviation of values for every fraction
for i in range (0, len(allData)):
    means.append(statistics.mean(allData[i]))
    stdev.append(statistics.stdev(allData[i]))
    
print("Means: \n", means)
print("\nStandard Deviations: \n", stdev)


plt.title("Pruning Effect over 100 runs on MONK-3 data")    
plt.xlabel("Fraction")
plt.ylabel("Test Score")
plt.show()

