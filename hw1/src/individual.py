import random #for random number generation
#import copy #for the copy function

#set the size of the genome
genome_size = 10

#set the possible DNA characters
DNA_Characters = ['A', 'C', 'G', 'T']

individual_mutatation_rate = 2

"""individual class"""
class individual:
   
   """class constructor"""
   def __init__(self):

      #Print Object Init Message
      print("Creating A New Individual\n")

      #init fitness to 0, we do not know the fitness of the individual yet.
      self.fitness = 0

      #init the genome to an empty list
      self.genome = []

      #populate the genome with random DNA characters
      for i in range(0, genome_size):
         self.genome.append(random.choice(DNA_Characters))

      #calculate the fitness of the individual
      self.calculate_fitness()

   """print_individual"""""
   def print_individual(self):
      
      #print the individual by calling the __str__ function
      print(self.__str__(), "\n")

   """calculate_fitness function"""
   """go through and add up all of the 'T' characters in the genome. """
   """The total number of 'T' characters is the fitness of the individual."""
   def calculate_fitness(self):
      #reset the fitness of the individual to 0
      self.fitness = 0

      #go through the genome and count the number of 'T' characters
      for c in self.genome:
         if c == 'T':
            self.fitness += 1

   """mutation function"""
   """select a random index in the genome and change the character at that index to a random DNA character."""
   def mutation(self):

      for i in range(0, genome_size):
         
         #select a random index in the genome
         if random.uniform(0,100) < individual_mutatation_rate:
            
            #set the character at the random index to a random DNA character
            self.genome[i] = random.choice(DNA_Characters)
      
      #recalculate the fitness of the individual
      self.calculate_fitness()
   
   """copy function"""
   """copy the fitness and genome from the copy_source individual to the current individual."""
   def copy(self, copy_source):

      #copy the fitness
      self.fitness = copy_source.fitness

      #copy the genome one character at a time using list comprehension
      self.genome = [i for i in copy_source.genome]

   """str function"""
   """return a string representation of the individual"""
   def __str__(self):
      
      output = "Individual #" + str(id(self))
      output += " Genome: "
      
      for c in self.genome:
         output += c
      
      output += " "

      output += "Fitness: "

      output += str(self.fitness)

      return output