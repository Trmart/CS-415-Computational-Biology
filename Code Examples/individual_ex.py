import random #for random number generation
#import copy #for the copy function

#set the size of the genome
genome_size = 10

#set the possible DNA characters
DNA_Characters = ['A', 'C', 'G', 'T']

class individual:
   def __init__(self):

      #Print Object Init Message
      print("Creating A New Individual")

      #init fitness to 0, we do not know the fitness of the individual yet.
      self.fitness = 0

      #init the genome to an empty list
      self.genome = []

      #populate the genome with random DNA characters
      for i in range(0, genome_size):
         self.genome.append(random.choice(DNA_Characters))

      #calculate the fitness of the individual
      self.calculate_fitness()

   #print the individual function
   def print_individual(self):

      #print fitness and genome
      # print("Fitness: ", self.fitness)
      # print("Genome: ", self.genome)
      # print(self.__str__())
      
      # print ("Genome: ")
      # for c in self.genome:
      #    print(c, end="")
      # print(" Fitness: ", self.fitness)

      print(self.__str__())
      print()

   #This is the fitness function for this problem.
   #go through and add up all of the 'T' characters in the genome. 
   #The total number of 'T' characters is the fitness of the individual.
   def calculate_fitness(self):
      #reset the fitness of the individual to 0
      self.fitness = 0

      #go through the genome and count the number of 'T' characters
      for c in self.genome:
         if c == 'T':
            self.fitness += 1

   #This is the mutation function for this problem.
   #select a random index in the genome and change the character at that index to a random DNA character.
   def mutation(self):

      #select a random index in the genome
      index = random.randint(0, genome_size - 1)

      #select a random DNA character
      new_char = random.choice(DNA_Characters)

      #set the character at the random index to the random DNA character
      self.genome[index] = new_char

      #recalculate the fitness of the individual
      self.calculate_fitness()
   
   #copy function
   def copy(self, copy_source):

      #copy the fitness
      self.fitness = copy_source.fitness
      
      #copy the genome one character at a time using for loop
      # for i in range(0,genome_size):
      #    self.genome[i] = copy_source.genome[i]

      #copy the genome one character at a time using list comprehension
      self.genome = [i for i in copy_source.genome]

   def __str__(self):
      
      output = "Individual # " + str(id(self))
      output += " Genome: "
      
      for c in self.genome:
         output += c
      
      output += " "

      output += "Fitness: "

      output += str(self.fitness)

      return output

def main():
   
   #mother
   ind1 = individual()
   ind1.print_individual()

   #daughter
   ind2 = individual()

   #cell division by copying
   ind2.copy(ind1)

   #print and mutate the daughter
   ind2.print_individual()
   ind2.mutation()
   ind2.print_individual()


if __name__ == "__main__":
   main()