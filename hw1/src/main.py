from population import population
from individual import individual
import matplotlib.pyplot as plt

"""main function"""
def main():

   #********************EXP1**************************
   
   # """Task 1:
   #       have a set mutation rate of 5% 
   #       plot the average fitness of the population over various population sizes
   # """

   # populations_1 = create_populations_of_increasing_magnitude(50, 10, 50)

   # mutate_population_lists(populations_1, 5)
   
   
   # mean_population_fitnesses1 = []

   # for index in range(0, len(populations_1)):
   #    mean_population_fitnesses1.append(populations_1[index].avg_fitness)
   
   # means_of_populations = {'means_of_population1' : mean_population_fitnesses1}

   # plt.scatter([50, 100, 150, 200, 250, 300, 350, 400, 450, 500], mean_population_fitnesses1)
   # plt.xlabel('Population Size')
   # plt.ylabel('Average Fitness')
   # plt.title('Average Fitness vs Population Size with 5% Mutation Rate')
   # plt.show()
   
   
   # """Task 2:
   #    increase the mutation rate to 25%
   #    plot the average fitness of the population over various population sizes
   # """
   # populations_2 = create_populations_of_increasing_magnitude(50, 10, 50)

   # mutate_population_lists(populations_2, 25)
   # mean_population_fitnesses2 = []

   # # mean_population_fitnesses = [population_1.avg_fitness, population_2.avg_fitness, population_3.avg_fitness, population_4.avg_fitness, population_5.avg_fitness, population_6.avg_fitness, population_7.avg_fitness, population_8.avg_fitness, population_9.avg_fitness, population_10.avg_fitness]
   # for index in range(0, len(populations_2)):
   #    mean_population_fitnesses2.append(populations_2[index].avg_fitness)
   
   # means_of_populations.update({'means_of_population2' : mean_population_fitnesses2})
   
   # plt.scatter([50, 100, 150, 200, 250, 300, 350, 400, 450, 500], mean_population_fitnesses2)
   # plt.xlabel('Population Size')
   # plt.ylabel('Average Fitness')
   # plt.title('Average Fitness vs Population Size with 25% Mutation Rate')
   # plt.show()

   # """Task 3
   #    plot the average fitness of the population over various mutation rates and population sizes
   # """

   # plt.scatter([50, 100, 150, 200, 250, 300, 350, 400, 450,  500], means_of_populations['means_of_population1'], label = '5% Mutation Rate', color = 'red')
   # plt.scatter([50, 100, 150, 200, 250, 300, 350, 400, 450,  500], means_of_populations['means_of_population2'], label = '25% Mutation Rate', color = 'blue')
   # plt.xlabel('Population Size')
   # plt.ylabel('Average Fitness')
   # plt.title('Average Fitness vs Population Size with Various Mutation Rates')
   # plt.legend()
   # plt.show()


   
   #********************EXP2********************
   
   """
      Task 1:

         have an initial fitness function just matching "T" characters
         plot the average fitness of the population over various population sizes
   """
   populations_1 = create_populations_of_increasing_magnitude(50, 10, 50)

   mean_population_fitnesses1 = []

   for index in range(0, len(populations_1)):
      mean_population_fitnesses1.append(populations_1[index].avg_fitness)
   
   means_of_populations = {'means_of_population1' : mean_population_fitnesses1}

   plt.scatter([50, 100, 150, 200, 250, 300, 350, 400, 450, 500], mean_population_fitnesses1)
   plt.xlabel('Population Size')
   plt.ylabel('Average Fitness')
   plt.title('Average Fitness vs Population Size with Original Fitness Function')
   plt.show()

   """
      Task 2: 

      implement a new fitness function that matches "T" characters in groups of 3
      plot the average fitness of the population over various population sizes

   """

   populations_2 = create_populations_of_increasing_magnitude(50, 10, 50)

   mean_population_fitnesses2 = []

   for index in range(0, len(populations_2)):
      mean_population_fitnesses2.append(populations_2[index].avg_strict_fitness)
   
   means_of_populations.update({'means_of_population2' : mean_population_fitnesses2})
   
   plt.scatter([50, 100, 150, 200, 250, 300, 350, 400, 450, 500], mean_population_fitnesses2)
   plt.xlabel('Population Size')
   plt.ylabel('Average Fitness')
   plt.title('Average Fitness vs Population Size with Strict Fitness Function')
   plt.show()



   """
      Task 3:
      
      plot the average fitness of the population over various population sizes
   
   """


   plt.scatter([50, 100, 150, 200, 250, 300, 350, 400, 450,  500], means_of_populations['means_of_population1'], label = 'Original Fitness Function', color = 'red')
   plt.scatter([50, 100, 150, 200, 250, 300, 350, 400, 450,  500], means_of_populations['means_of_population2'], label = 'Strict Fitness Function', color = 'blue')
   plt.xlabel('Population Size')
   plt.ylabel('Average Fitness')
   plt.title('Average Fitness vs Population Size with Various Fitness Functions')
   plt.legend()
   plt.show()
   


def create_populations_of_increasing_magnitude(initial_population_size, number_of_populations, magnitude_of_population_increase):
   """create a population of a set magnitude"""
   population_list = []

   for i in range(0,number_of_populations):
      population_list.append(population(initial_population_size))
      initial_population_size += magnitude_of_population_increase
   
   return population_list

def mutate_population_lists(population_list, mutation_rate):
   """mutate a list of populations"""
   for population in population_list:
      population.mutate_population(mutation_rate)

"""call main"""
if __name__ == "__main__":
   main()