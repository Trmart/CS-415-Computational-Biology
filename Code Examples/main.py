import population as pop
import individual as ind

def main():
   
   #mother
   ind1 = ind.individual()
   ind1.print_individual()

   #daughter
   ind2 = ind.individual()

   #cell division by copying
   ind2.copy(ind1)

   #print and mutate the daughter
   ind2.print_individual()
   ind2.mutation()
   ind2.print_individual()

   pop1 = pop.population()

   pop1.print_population()

if __name__ == "__main__":
   main()