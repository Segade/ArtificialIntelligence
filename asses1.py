import numpy as np
import random
from copy import deepcopy

 


def cost(ind):
  result = 0
  total = 0 

  for i in ind.chromosome:
    total += i 

  expectedValue = round(total /  squareSize)

# process the rows
  for i in range(squareSize):
    criteria = ind.chromosome[(i * squareSize) : (i*squareSize) + squareSize]
    rowSum = np.sum(criteria)
    result += (expectedValue - rowSum)**2
#    print ("\nRow. " , criteria , ", the sum is " , rowSum , ", The result is " ,result)

 
 # process the columns  
  for col in range(squareSize):
    colSum = 0
#    print("Col")
    for row in range(col, len(ind.chromosome), squareSize):
      colSum += ind.chromosome[row]
#      print(ind.chromosome[row], end=' ')

    result += (expectedValue - colSum)**2
#    print("the sum is " , colSum , ", the result is " ,  result)

# process the left right top diagonal 
  index = 0
  total = 0
  for i in range(0, squareSize):
    total += ind.chromosome[i]
    index +=  squareSize + 1

  result += (expectedValue - total)**2


# process the right left top diagonal 
  index = squareSize -1
  total = 0
  for i in range(0, squareSize):
    total += ind.chromosome[index]
    index += squareSize - 1

  result += (expectedValue - total)**2


  return result 


 

  
 
 

# classes definitions 	
	
class problem:
  def __init__(self):
    self.squareSize = 3
    self.number_of_genes = self.squareSize**2
    self.cost_function = cost


class parameters:
  def __init__(self):
    self.population  = 1000
    self.number_of_generations = 100
    self.gene_mutate_rate = 0.2
    self.crossover_explore_rate = 0.2
		
class individual:
  def __init__(self, prob ):
    self.cost = prob.cost_function
    self.chromosome = list(range(1,(prob.number_of_genes+1)))
    random.shuffle(self.chromosome)


  def mutate(self, mutateRate):
    for index in range(len(self.chromosome)):
      if (np.random.uniform() < mutateRate):
        swap = index + 1
        aux =self.chromosome[index] 

        if ((index+1) == len(self.chromosome)):
          swap = 0    

        self.chromosome[index] = self.chromosome[swap]
        self.chromosome[swap] = aux


  def crossover(self, parent1, number_of_genes):
    split = np.random.randint(1, number_of_genes)
    child1 = deepcopy(self)
    child1.chromosome = self.chromosome[:split]
    aux = self.chromosome[split:]
    print("\child\n", child1.chromosome)
 
    for i in parent1.chromosome:
      pasa = True
      for j in child1.chromosome :
          if i == j:
            pasa = False

      if pasa == True:
        child1.chromosome.append(i)

    print ("\nsplit  " , split)
    return child1 


print("hello")
prob = problem()

ind1 = individual(prob)
ind2 = individual(prob)
child = ind1.crossover(ind2, prob.number_of_genes)

print("\nparent1 \n" , ind1.chromosome , "\nparent2 \n" , ind2.chromosome , "\nchild1 \n" , child.chromosome) 