from individual import individual
from population import population
import random

"""global variables"""

#gap penalty for scoring matrix
gap_penalty = -8

#sequences to align
sequence1 = "TTAGCCAGT"
sequence2 = "TAAGACATTTTAC"


"""create_scoring_matrix function"""
def create_scoring_matrix():
    """Create the scoring matrix for the two sequences"""
    scoring_matrix = [[0 for i in range(0, len(sequence1) + 1)] for j in range(0, len(sequence2) + 1)]

    #create the direction matrix
    direction_matrix = [[0 for i in range(0, len(sequence1) + 1)] for j in range(0, len(sequence2) + 1)]
    
    #fill in the first row and column with gap penalties
    for i in range(0,len(scoring_matrix[0])):
        scoring_matrix[0][i] = i * gap_penalty
    
    for i in range(0,len(scoring_matrix)):
        scoring_matrix[i][0] = i * gap_penalty
    
    #fill in the rest of the matrix with random numbers
    for r in range(1,len(scoring_matrix)):
        for c in range(1,len(scoring_matrix[0])):
            
            #get the value of the cell above
            vertical_value =scoring_matrix[r-1][c] + gap_penalty
            #get the value of the cell to the left
            horizontal_value = scoring_matrix[r][c-1] + gap_penalty
            #get the value of the cell to the left and above
            diagonal_value = scoring_matrix[r-1][c-1] + gap_penalty
            
            if(sequence1[c-1] == sequence2[r-1]):
                diagonal_value += 10
            else:
                diagonal_value -= 10
            
            scoring_matrix[r][c] = max(vertical_value, horizontal_value, diagonal_value)

            if diagonal_value > horizontal_value and diagonal_value > vertical_value:
                direction_matrix[r][c] = "d "
            
            #final value is the max of the three values above max(vertical_value, horizontal_value, diagonal_value)
            print(f'{"Max Value: " + str(scoring_matrix[r][c])}')
    
    #print the scoring matrix
    # print_matrix(scoring_matrix)

    #return the scoring matrix
    return scoring_matrix

"""print_matrix function"""""
def print_matrix(matrix):
    """print the scoring matrix"""
    for row in matrix:
        print(f'{str(row) :<5}')
        for col in matrix:
            print(f'{str(col) :<5}')


"""main function"""
def main():
    """"""
    matrix = create_scoring_matrix()
    print_matrix(matrix)
    
    print(sequence1)
    
    print(sequence2)


if __name__ == "__main__":
    main()