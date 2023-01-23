import individual as ind

population_size = 4

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
   """Print the population function"""
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
      