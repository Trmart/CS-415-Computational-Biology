import population as pop
import individual as ind

"""main function"""
def main():
   
   #mother
   # ind1 = ind.individual()
   # ind1.print_individual()

   # #daughter
   # ind2 = ind.individual()

   # #cell division by copying
   # ind2.copy(ind1)

   # #print and mutate the daughter
   # ind2.print_individual()
   # ind2.mutation()
   # ind2.print_individual()

   pop1 = pop.population()

   pop1.print_population()

   #assign a new individual from tournament selection of the population and print the winner
   ind3 = pop1.the_population[pop1.tournament_selection()]
   ind3.print_individual()

   pop1.generational()

"""call main"""
if __name__ == "__main__":
   main()