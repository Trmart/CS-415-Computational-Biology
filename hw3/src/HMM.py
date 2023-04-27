"""
    Taylor Martin
    CS-415 : Computational Biology
    Spring 2023
    Homework 3 : HMM.py
    Due Date : 4/28/2023

    Generates a Hidden Markov Model from a given set of sequences and states
    Generates the emission probabilities for each state
    Generates the transition probabilities for each state
    Saves the emission and transition probabilities to a csv file
    

    Usage: python3 HMM.py

"""

"""Global Variables"""

in_filename = "/home/trmart/Documents/CS-415/CS-415-Computational-Biology/hw3/resources/DataFile2.txt"

transitions_out_filename = "/home/trmart/Documents/CS-415/CS-415-Computational-Biology/hw3/output/transition_probabilities.csv"

emissions_out_filename = "/home/trmart/Documents/CS-415/CS-415-Computational-Biology/hw3/output/emission_probabilities.csv"

scoring_matrix_size = 26

unicode_point = 97

number_of_HMM_states = 3

def load_csv_data_file():
    
    with open(in_filename, "r") as f:
        data_file = f.read().splitlines()
    
    amino_acid_sequence = []
    HMM_state_sequence = []
    
    for i in range(0, len(data_file), number_of_HMM_states): 
        amino_acid_sequence.append(data_file[i])
        HMM_state_sequence.append([int(j) for j in data_file[i+1]])

    return amino_acid_sequence, HMM_state_sequence

def save_emission_tables_to_csv(filename, state0_emissions, state1_emissions, state2_emissions):

    with open(filename, "w") as f:
        f.write("state 0 emission probabilities:   " + " , ".join(str(i) for i in state0_emissions) + "\n\n")
        f.write("state 1 emission probabilities:   " + " , ".join(str(i) for i in state1_emissions) + "\n\n")
        f.write("state 2 emission probabilities:   " + " , ".join(str(i) for i in state2_emissions) + "\n")

def save_transition_table_to_csv(filename, transition_table):
    
    with open(filename, "w") as f:
        
        for row in transition_table:
            
            f.write(' , '.join(map(str, row)))
            
            f.write('\n')

def generate_state_emission_probabilities_table(amino_acid_sequence, HMM_state_sequence):

    state0_emissions = [0] * scoring_matrix_size
    state1_emissions = [0] * scoring_matrix_size
    state2_emissions = [0] * scoring_matrix_size

    states_emissions_totals = [0] * number_of_HMM_states


    for i in range(len(amino_acid_sequence)):
        
        for j in range(len(amino_acid_sequence[0])):
            
            char_num = ord(amino_acid_sequence[i][j]) - unicode_point
            
            state = HMM_state_sequence[i][j]

            if state == 0: state0_emissions[char_num] += 1
            
            elif state == 1: state1_emissions[char_num] += 1
            
            else: state2_emissions[char_num] += 1

            states_emissions_totals[state] += 1

    state0_emissions = [round(state0_emissions[i] / states_emissions_totals[0], 6) for i in range(scoring_matrix_size)]
    state1_emissions = [round(state1_emissions[i] / states_emissions_totals[1], 5) for i in range(scoring_matrix_size)]
    state2_emissions = [round(state2_emissions[i] / states_emissions_totals[2], 5) for i in range(scoring_matrix_size)]

    return state0_emissions, state1_emissions, state2_emissions

def generate_state_transition_probabilities_table(state_sequence):
    
    transition_table = [[0] * number_of_HMM_states for _ in range(number_of_HMM_states)]
    
    for states in state_sequence:
        
        for i in range(len(states) - 1):
            
            transition_table[states[i]][states[i+1]] += 1
    
    for row in transition_table:
        
        total = sum(row)
        
        if total > 0: row[:] = [round(num/total, 5) for num in row]
    
    return transition_table

def main():
    
    amino_acid_sequence, hmm_state_sequence = load_csv_data_file()

    transition_probabilities = generate_state_transition_probabilities_table(hmm_state_sequence)

    state0_emissions, state1_emissions, state2_emissions = generate_state_emission_probabilities_table(amino_acid_sequence, hmm_state_sequence)
    
    save_transition_table_to_csv(transitions_out_filename, transition_probabilities)

    save_emission_tables_to_csv(emissions_out_filename, state0_emissions, state1_emissions, state2_emissions)

if __name__ == "__main__":
    main()