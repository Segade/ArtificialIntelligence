import numpy as np
import random
from copy import deepcopy

 


def cost(ind):
  result = 0
  total = 0 
  squareSize = round(len(ind) ** 0.5)

  for i in ind:
    total += i 

  expectedValue = round(total /  squareSize)

# process the rows
  for i in range(squareSize):
    criteria = ind[(i * squareSize) : (i*squareSize) + squareSize]
    rowSum = np.sum(criteria)
    result += (expectedValue - rowSum)**2
#    print ("\nRow. " , criteria , ", the sum is " , rowSum , ", The result is " ,result)
#  print("\nresult  " , result)

 
 # process the columns  
  for col in range(squareSize):
    colSum = 0
#    print("Col")
    for row in range(col, len(ind), squareSize):
      colSum += ind[row]
#      print(ind.chromosome[row], end=' ')

    result += (expectedValue - colSum)**2
#    print("the sum is " , colSum , ", the result is " ,  result)
#  print("\nresult  " , result)

# process the left right top diagonal 
  index = 0
  total = 0
  for i in range(0, squareSize):
    total += ind[i]
    index +=  squareSize + 1

  result += (expectedValue - total)**2


# process the right left top diagonal 
  index = squareSize -1
  total = 0
  for i in range(0, squareSize):
    total += ind[index]
    index += squareSize - 1

  result += (expectedValue - total)**2


  return round(result) 


 

  
 
 

# classes definitions 	
	
class problem:
  def __init__(self):
    self.squareSize = 5
    self.number_of_genes = self.squareSize**2
    self.cost_function = cost


class parameters:
  def __init__(self):
    self.population  = 1000
    self.number_of_generations = 300 
    self.gene_mutate_rate = 0.2
    self.crossover_explore_rate = 4
    self.child_rate_per_generation = 1
    self.gene_mutate_range = 8


	
class individual:
  def __init__(self, prob ):
    self.chromosome = list(range(1,(prob.number_of_genes+1)))
    random.shuffle(self.chromosome)

    self.squareSize = prob.squareSize
    self.cost = prob.cost_function(self.chromosome )
 



  def mutate(self, mutateRate, mutateRange):
    for index in range(len(self.chromosome)):

      if (np.random.uniform() < mutateRate):
        index2 = index 
 
        for x in range(mutateRange ):
          index2 = index2 + x

          if (index2  >= len(self.chromosome)):  index2 = 0

          swap = index2 + 1
          aux =self.chromosome[index2] 

          if ((index2 + 1) == len(self.chromosome)):  swap = 0
            
          self.chromosome[index2] = self.chromosome[swap]
          self.chromosome[swap] = aux
#          print("\n    ", self.chromosome[index2] , "  ", self.chromosome[swap] )
 

  def crossover(self, parent1, explore_rate):
 
    split = np.random.randint(1 , len(self.chromosome) - explore_rate)  
#    print("split value " , split)
    child1 = deepcopy(self)
    child1.chromosome = self.chromosome[:split]
    aux = self.chromosome[split:]
#    print("\child\n", child1.chromosome)
 
    for i in parent1.chromosome:
      pasa = True
      for j in child1.chromosome :
          if i == j:
            pasa = False

      if pasa == True:
        child1.chromosome.append(i)

    child2 = deepcopy(self)
    child2.chromosome = parent1.chromosome[:split]
 
    for i in parent1.chromosome:
      pasa = True
      for j in child2.chromosome :
          if i == j:
            pasa = False

      if pasa == True:
        child2.chromosome.append(i)


#    print ("\nsplit  " , split)
    return child1, child2 


 
###############################

def choose_indices_from(number_in_list):
  index_1 = np.random.randint(number_in_list)
  index_2 = np.random.randint(number_in_list)
  if index_1 == index_2:
    return choose_indices_from(number_in_list)
  return index_1,index_2

def run_genetic(prob, params):
  # Read in important info from problem
  cost_function = prob.cost_function


  number_in_population = params.population
  max_number_of_generations = params.number_of_generations
  number_of_children_per_generation = params.child_rate_per_generation * number_in_population
  explore_crossover = params.crossover_explore_rate
  gene_mutate_rate = params.gene_mutate_rate
  gene_mutate_range = params.gene_mutate_range

  # Generate initial population
  population = []

  #placeholder for best solution

  best_solution = individual(prob)
  best_solution.cost = np.infty
  for i in range(number_in_population):
    new_individual = individual(prob)
    population.append(new_individual)

    if new_individual.cost < best_solution.cost:
      best_solution = deepcopy(new_individual)

  #  Generational Iteration

  for _iteration in range(max_number_of_generations):

    # create children

    children = []

    while len(children) < number_of_children_per_generation:
      parent1_index , parent2_index = choose_indices_from(len(population))
      parent1 = population[parent1_index]
      parent2 = population[parent2_index]

      child1, child2 = parent1.crossover(parent2,explore_crossover)
      child1.mutate(gene_mutate_rate, gene_mutate_range)
      child1.cost = cost_function(child1.chromosome)
      child2.mutate(gene_mutate_rate, gene_mutate_range)
      child2.cost = cost_function(child2.chromosome)

      # add children in list
      children.append(child1)
      children.append(child2)
      #end of the while loop

    # all children created

    # add the children to the population

    # sort the population

    # adjust the best solution






  return best_solution
##### execution
print("hello")


prob = problem()
par = parameters()
bs = run_genetic(prob,par)
print("\nThe length of the chromosome is " , len(bs.chromosome), 
". The square size is " , round(len(bs.chromosome)**0.5) ,
"\nThe population is ", par.population , ". The number of generations is ", par.number_of_generations ,
". The mutate rate is " , par.gene_mutate_rate , ". The mutate range is " , par.gene_mutate_range ,
". The explore rate is " , par.crossover_explore_rate ,
"\nThe best solution " ,
"\nThe chromosome is " , bs.chromosome ,
 "\nThe cost is ", bs.cost)

#p = problem()
#ind = individual(p)
#pa = parameters()
#print("\noriginal\n", ind.chromosome)
#ind.mutate(pa.gene_mutate_rate, pa.gene_mutate_range)
#print("\nmutate\n", ind.chromosome)
#c = ind.cost
#print("chromosome  ", ind.chromosome ,"\ncost  ", c)