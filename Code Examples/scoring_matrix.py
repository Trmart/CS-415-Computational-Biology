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
genome_sequence_1 = "TTAGCCAGT"
genome_sequence_2 = "TAAGACATTTTAC"

#create the scoring matrix
scoring_matrix = [[0 for row in range(0, len(genome_sequence_1) + 1)] for column in range(0, len(genome_sequence_2) + 1)]

#create the direction matrix
direction_matrix = [[0 for row in range(0, len(genome_sequence_1) + 1)] for column in range(0, len(genome_sequence_2) + 1)]

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
            vertical_value =scoring_matrix[row-1][column] + gap_penalty
            #get the value of the cell to the left
            horizontal_value = scoring_matrix[row][column-1] + gap_penalty
            #get the value of the cell to the left and above
            diagonal_value = scoring_matrix[row-1][column-1]
            
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