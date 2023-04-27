"""
    Taylor Martin
    CS-415 : Computational Biology
    Spring 2023
    Homework 3 : substitution_matrix.py
    Due Date : 4/28/2023

    Generates a scoring matrix from a given set of sequences
    Calculates the probability of each amino acid
    Calculates the probability of each pair of amino acids
    Saves the scoring matrix to a csv file

    Usage: python3 substitution_matrix.py

"""

import math 

unicode_point = 97
scoring_matrix_size = 26

def load_csv_data_file(filename):
    
    with open(filename, "r") as f:
    
        genome_sequences = [f.readline().rstrip("\n") for i in range(160)]
    
    return genome_sequences

def print_scoring_matrix(matrix, tab_length=3):
    
    print(f'{" ":>{tab_length}}', end='')
    
    for i in range(len(matrix[0])):
        
        print(f'{chr(i + unicode_point):>{tab_length}}', end='')
    
    print()

    for i in range(len(matrix[0])):
        
        print(f'{chr(i + unicode_point):>{tab_length}}', end='')
        
        for j in range(len(matrix)):
            
            print(f'{matrix[i][j]:{tab_length}}', end='')
        
        print()

def save_scoring_matrix_to_csv(filename, scoring_matrix):

    with open(filename, "w") as f:
        
        for i in range(0,len(scoring_matrix[0])):
            
            for j in range(0,len(scoring_matrix)):
                
                f.write(f'{scoring_matrix[i][j]},')
            
            f.write('\n')

def generate_probability_scores(scoring_matrix):

    probability_scores = [0 for i in range(scoring_matrix_size)]
    
    for i in range(len(probability_scores)):
        
        probability_scores[i] = scoring_matrix[i][i]

        j = 0
        
        while j != i:
            
            probability_scores[i] += scoring_matrix[j][i]
            
            j += 1
    
    return probability_scores

def generate_pair_probability_scores(probability_scores):
    
    pair_probability_scores = [[0 for i in range(scoring_matrix_size)] for j in range(scoring_matrix_size)]
    
    for i in range(scoring_matrix_size):
        
        for j in range(i, scoring_matrix_size):
            
            pair_probability_scores[i][j] = 2 * probability_scores[i] * probability_scores[j]
            
            pair_probability_scores[j][i] = pair_probability_scores[i][j]
        
        pair_probability_scores[i][i] = probability_scores[i] ** 2
    
    return pair_probability_scores

def generate_scoring_matrix(amino_acid_sequences):
    
    scoring_matrix = [[0 for j in range(scoring_matrix_size)] for i in range(scoring_matrix_size)]
    
    sequence_length = len(amino_acid_sequences)


    for i in range(len(amino_acid_sequences[0])):
        
        for j in range(sequence_length):
            
            for k in range(j+1, sequence_length):
                
                i_temp_index = ord(amino_acid_sequences[j][i]) - unicode_point
                k_temp_index = ord(amino_acid_sequences[k][i]) - unicode_point

                scoring_matrix[i_temp_index][k_temp_index] += 1
                scoring_matrix[k_temp_index][i_temp_index] += 1
    
    total_number_pairs = (sequence_length-1) * sequence_length / 2 * len(amino_acid_sequences[0])


    for i in range(scoring_matrix_size):
        
        for j in range(i, scoring_matrix_size):
            
            scoring_matrix[i][j] /= total_number_pairs
            
            scoring_matrix[j][i] = scoring_matrix[i][j]

    probability_scores = generate_probability_scores(scoring_matrix)

    pair_probability_scores = generate_pair_probability_scores(probability_scores)


    for i in range(scoring_matrix_size):
        
        for j in range(i, scoring_matrix_size):
            
            if pair_probability_scores[i][j] == 0 or scoring_matrix[i][j] == 0:
                
                scoring_matrix[i][j] = 0
            
            else:
                
                scoring_matrix[i][j] = round(2 * math.log( (scoring_matrix[i][j]/pair_probability_scores[i][j]) , 2))
            
            scoring_matrix[j][i] = scoring_matrix[i][j]
    
    return scoring_matrix

def main():
    
    in_filename = "/home/trmart/Documents/CS-415/CS-415-Computational-Biology/hw3/resources/DataFile1-1.txt"
    
    amino_acid_sequences = load_csv_data_file(in_filename)
    
    scoring_matrix = generate_scoring_matrix(amino_acid_sequences)
    
    print_scoring_matrix(scoring_matrix)
    
    out_filename = "/home/trmart/Documents/CS-415/CS-415-Computational-Biology/hw3/output/substitution_matrix.csv"
    
    save_scoring_matrix_to_csv(out_filename, scoring_matrix)

if __name__ == "__main__":
    main()