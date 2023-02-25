from individual import individual
from population import population
import random
from enum import Enum

"""global variables"""
class Directional_Arrows(Enum):
    """Class To Hold Directional Arrows Unicode"""
    VERTICAL_ARROW = '\u2191'

    HORIZONTAL_ARROW = '\u2190'

    DIAGONAL_ARROW = '\u2196'

#gap penalty for scoring matrix
gap_penalty = -8

#sequences to align
# genome_sequence_1 = "TTAGCCAGT"
# genome_sequence_2 = "TAAGACATTTTAC"

genome_sequence_1 = "heagawhee"
genome_sequence_2 = "pawheae"


#blosum50 matrix
# Dictionary to map nucleic acid codes to matrix indices
aminamino_acid_dictionary = {'a':0, 'r':1, 'n':2, 'd':3, 'c':4, 'q':5, 'e':6, 'g':7,'h':8, 
                            'i':9, 'l':10, 'k':11, 'm':12, 'f':13, 'p':14, 's':15,'t':16, 'w':17, 'y':18, 
                            'v':19}

#blosum[0][0] = 5
#blosum50[0][1] = -2
#blosum50[0][2] = -1
#... very slow
#blosum50 matrix
blosum50 = [[]]
blosum50[0] = [5,-2,-1,-2,-1,-1,-1,0,-2,-1,-2,-1,-1,-3,-1,1,0,-3,-2,0]
blosum50.append([-2,7,-1,-2,-4,1,0,-3,0,-4,-3,3,-2,-3,-3,-1,-1,-3,-1,-3])
blosum50.append([-1,-1,7,2,-2,0,0,0,1,-3,-4,0,-2,-4,-2,1,0,-4,-2,-3])
blosum50.append([-2,-2,2,8,-4,0,2,-1,-1,-4,-4,-1,-4,-5,-1,0,-1,-5,-3,-4])
blosum50.append([-1,-4,-2,-4,13,-3,-3,-3,-3,-2,-2,-3,-2,-2,-4,-1,-1,-5,-3,-1])
blosum50.append([-1,1,0,0,-3,7,2,-2,1,-3,-2,2,0,-4,-1,0,-1,-1,-1,-3])
blosum50.append([-1,0,0,2,-3,2,6,-3,0,-4,-3,1,-2,-3,-1,-1,-1,-3,-2,-3])
blosum50.append([0,-3,0,-1,-3,-2,-3,8,-2,-4,-4,-2,-3,-4,-2,0,-2,-3,-3,-4])
blosum50.append([-2,0,1,-1,-3,1,0,-2,10,-4,-3,0,-1,-1,-2,-1,-2,-3,2,-4])
blosum50.append([-1,-4,-3,-4,-2,-3,-4,-4,-4,5,2,-3,2,0,-3,-3,-1,-3,-1,4])
blosum50.append([-2,-3,-4,-4,-2,-2,-3,-4,-3,2,5,-3,3,1,-4,-3,-1,-2,-1,1])
blosum50.append([-1,3,0,-1,-3,2,1,-2,0,-3,-3,6,-2,-4,-1,0,-1,-3,-2,-3])
blosum50.append([-1,-2,-2,-4,-2,0,-2,-3,-1,2,3,-2,7,0,-3,-2,-1,-1,0,1])
blosum50.append([-3,-3,-4,-5,-2,-4,-3,-4,-1,0,1,-4,0,8,-4,-3,-2,1,4,-1])
blosum50.append([-1,-3,-2,-1,-4,-1,-1,-2,-2,-3,-4,-1,-3,-4,10,-1,-1,-4,-3,-3])
blosum50.append([1,-1,1,0,-1,0,-1,0,-1,-3,-3,0,-2,-3,-1,5,2,-4,-2,-2])
blosum50.append([0,-1,0,-1,-1,-1,-1,-2,-2,-1,-1,-1,-1,-2,-1,2,5,-3,-2,0])
blosum50.append([-3,-3,-4,-5,-5,-1,-3,-3,-3,-3,-2,-3,-1,1,-4,-4,-3,15,2,-3])
blosum50.append([-2,-1,-2,-3,-3,-1,-2,-3,2,-1,-1,-2,0,4,-3,-2,-2,2,8,-1])
blosum50.append([0,-3,-3,-4,-1,-3,-3,-4,-4,4,1,-3,1,-1,-3,-2,0,-3,-1,5])


#create the scoring matrix
scoring_matrix = [[0 for row in range(0, len(genome_sequence_1) + 1)] for column in range(0, len(genome_sequence_2) + 1)]

#create the direction matrix
direction_matrix = [['.' for row in range(0, len(genome_sequence_1) + 1)] for column in range(0, len(genome_sequence_2) + 1)]

"""create_scoring_matrix function"""
def create_scoring_matrix():
    """Create the scoring matrix for the two sequences"""

    #fill in the first row and column with gap penalties
    for index in range(0,len(scoring_matrix[0])):
        scoring_matrix[0][index] = index * gap_penalty
        direction_matrix[0][index] = Directional_Arrows.HORIZONTAL_ARROW.value #used to be 'h'
    
    for index in range(0,len(scoring_matrix)):
        scoring_matrix[index][0] = index * gap_penalty
        direction_matrix[index][0] = Directional_Arrows.VERTICAL_ARROW.value  #used to be 'v'
    
    #fill in the rest of the matrix with random numbers
    for row in range(1,len(scoring_matrix)):
        for column in range(1,len(scoring_matrix[0])):
            
            #get the value of the cell above
            vertical_value = scoring_matrix[row-1][column] + gap_penalty
            #get the value of the cell to the left
            horizontal_value = scoring_matrix[row][column-1] + gap_penalty
            #get the value of the cell to the left and above
            diagonal_value = scoring_matrix[row-1][column-1]

            #get the blosum50 index for the two amino acids
            blosum50_index_1 = aminamino_acid_dictionary[genome_sequence_1[column-1]]
            blosum50_index_2 = aminamino_acid_dictionary[genome_sequence_2[row-1]]
            
            diagonal_value += blosum50[blosum50_index_2][blosum50_index_1]
            
            if(genome_sequence_1[column-1] == genome_sequence_2[row-1]):
                diagonal_value += 10
            else:
                diagonal_value -= 10
            
            scoring_matrix[row][column] = max(vertical_value, horizontal_value, diagonal_value)

            if diagonal_value >= horizontal_value and diagonal_value >= vertical_value:
                direction_matrix[row][column] =  Directional_Arrows.DIAGONAL_ARROW.value 

            if horizontal_value > diagonal_value and horizontal_value > vertical_value:
                direction_matrix[row][column] = Directional_Arrows.HORIZONTAL_ARROW.value
            
            if vertical_value > diagonal_value and vertical_value > horizontal_value:
                direction_matrix[row][column] = Directional_Arrows.VERTICAL_ARROW.value

            #final value is the max of the three values above max(vertical_value, horizontal_value, diagonal_value)
            #print the max value for testing
            # print(f'{"Max Value: " + str(scoring_matrix[row][column])}')
    
    print_matrix(direction_matrix)

    #return the scoring matrix
    return scoring_matrix

"""print_matrix function"""""
def print_matrix(matrix, output_padding=5):
    """print the scoring matrix"""
    for row in matrix:
        for col in row:
            print(f'{str(col) :>{output_padding}}', end='')
        print()
    print()

def align_genome_sequences():
    """"""
    aligned_sequence_1 = ""
    aligned_sequence_2 = ""

    position_1 = len(genome_sequence_1)
    position_2 = len(genome_sequence_2)

    while position_1 > 0 or position_2 > 0:
        
        if(direction_matrix[position_2][position_1] == Directional_Arrows.DIAGONAL_ARROW.value): 
            
            aligned_sequence_1 += genome_sequence_1[position_1 - 1]
            
            aligned_sequence_2 += genome_sequence_2[position_2 - 1]

            position_1 -= 1
            position_2 -= 1

        elif(direction_matrix[position_2][position_1] == Directional_Arrows.HORIZONTAL_ARROW.value): 
            
            aligned_sequence_1 += genome_sequence_1[position_1 - 1]

            aligned_sequence_2 += '-'

            position_1 -= 1

        elif(direction_matrix[position_2][position_1] == Directional_Arrows.VERTICAL_ARROW.value): 
            
            aligned_sequence_1 += '-'

            aligned_sequence_2 += genome_sequence_1[position_1 - 1]

            position_2 -= 1

    #from beginning to end, copy the list in reverse [::-1]
    aligned_sequence_1 = aligned_sequence_1[::-1]

    #from beginning to end, copy the list in reverse [::-1]
    aligned_sequence_2 = aligned_sequence_2[::-1]

    return aligned_sequence_1,aligned_sequence_2

"""main function"""
def main():
    """"""
    matrix = create_scoring_matrix()
    print_matrix(matrix)
    
    print(genome_sequence_1 + '\n')
    
    print(genome_sequence_2 + '\n')

    aligned_sequence_1, aligned_sequence_2 = align_genome_sequences()

    print(aligned_sequence_1)
    print(aligned_sequence_2)

if __name__ == "__main__":
    main()