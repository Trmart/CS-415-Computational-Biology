from population import population
from individual import individual
import matplotlib.pyplot as plt

"""main function"""
def main():
   """"""
   #EXP1
   #task 1
   #have a set mutation rate of about 5-10% 
   #plot the average fitness of the population over various population sizes
   population_1 = population(50)
   # population_1.print_population()

   population_2 = population(100)
   # population_2.print_population()

   population_3 = population(200)
   # population_3.print_population()

   population_4 = population(500)
   # population_4.print_population()

   population_1.mutate_population(5)
   population_2.mutate_population(5)
   population_3.mutate_population(5)
   population_4.mutate_population(5)

   mean_population_fitnesses = [population_1.avg_fitness, population_2.avg_fitness, population_3.avg_fitness, population_4.avg_fitness]

   plt.scatter([50, 100, 200, 500], mean_population_fitnesses)
   plt.xlabel('Population Size')
   plt.ylabel('Average Fitness')
   plt.title('Average Fitness vs Population Size')
   plt.show()
   #task 2
   #increase the mutation rate to about 20-25%
   #plot the average fitness of the population over various population sizes
   population_1 = population(50)
   # population_1.print_population()

   population_2 = population(100)
   # population_2.print_population()

   population_3 = population(200)
   # population_3.print_population()

   population_4 = population(500)
   # population_4.print_population()

   population_1.mutate_population(25)
   population_2.mutate_population(25)
   population_3.mutate_population(25)
   population_4.mutate_population(25)

   mean_population_fitnesses = [population_1.avg_fitness, population_2.avg_fitness, population_3.avg_fitness, population_4.avg_fitness]

   plt.scatter([50, 100, 200, 500], mean_population_fitnesses)
   plt.xlabel('Population Size')
   plt.ylabel('Average Fitness')
   plt.title('Average Fitness vs Population Size')
   plt.show()

   #task 3
   #plot the average fitness of the population over various mutation rates and population sizes

   #task 4
   #Work on EXP1 part of Report

   #EXP2
   #task 1
   #have an initial fitness function just matching "T" characters
   #plot the average fitness of the population over various population sizes


   #task 2
   #implement a new fitness function that matches "T" characters in groups of 3
   #plot the average fitness of the population over various population sizes

   #task 3
   #plot the average fitness of the population over various population sizes

   #task 4
   #Work on EXP2 part of Report



"""call main"""
if __name__ == "__main__":
   main()