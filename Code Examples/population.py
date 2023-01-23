import individual as ind
import random

#global population size for population class
population_size = 4
#global tournament size for population class
tournament_size = 3
"""population class"""
class population:

   """class constructor"""
   def __init__(self):
      
      ##Print Object Init Message
      print("Creating A New Population")
      
      ##init the populations average fitness to 0, we do not know the fitness of the population yet.
      self.avg_fitness = 0
      
      ##init the population to an empty list
      self.the_population = []

      for i in range (0,population_size):
         self.the_population.append(ind.individual())

      self.calculate_population_stats()
   
   
   """print_population"""""
   """Print the individuals in the population """
   def print_population(self):

      ##print the population by calling the print_individual function for each individual in the population
      for i in self.the_population:
         i.print_individual()

      ##print the average fitness of the population
      print("Average Fitness: ", self.avg_fitness)
   
   """calculate_population_stats"""
   """Calculate the average fitness of the population"""
   def calculate_population_stats(self):
      self.avg_fitness = 0

      for i in self.the_population:
         self.avg_fitness += i.fitness
      
      self.avg_fitness /= population_size

   """tournament_selection function"""
   """randomly select two individuals from the population and return the individual with the higher fitness."""
   def tournament_selection(self):

      best_individual = random.randint(0, population_size)
      best_fitness = self.the_population[best_individual].fitness

      for i in range(0, tournament_size - 1):
         
         #select a random individual from the population
         current = random.randint(0, population_size)
         current_fitness = self.the_population[current].fitness
         
         #if the fitness of the random individual is greater than the fitness of the best individual
         if current_fitness > best_fitness:
            best_individual = current
            best_fitness = current_fitness

      #return the individual with the highest fitness
      return best_individual