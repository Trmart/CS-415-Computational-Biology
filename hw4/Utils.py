"""
  Taylor Martin
  CS-415: Computational Biology
  Project 4
  Dr. Terry Soule
  Spring 2023
  5/10/2023

  FILE: Utils.py

"""

def perform_alignment_and_scoring(genome_sequences,substitution_matrix_aligned_sequences,blossum50_matrix_aligned_sequences,blossum50_matrix_alignment_scores, substitution_matrix_alignment_scores):
  
  print("\n\n*******************************************************************************************")  
  print("Blossum50 Matrix")
  print("*******************************************************************************************\n\n")  
    
  for i in range(len(genome_sequences)):
    for j in range(len(genome_sequences)):
        if i != j:
            blossum50_matrix_alignment_scores[i][j] = blossum50_matrix_aligned_sequences.calculate_alignment_score(genome_sequences[i], genome_sequences[j])
            print(f"{i+1},{j+1} Score: {blossum50_matrix_alignment_scores[i][j]}")
            blossum50_matrix_aligned_sequences.print_best_alignment_score_from_previous_pair()
            print(" ")
  
  print("\n\n*******************************************************************************************")  
  print("Blossum50 Matrix Alignment Scores")
  print("*******************************************************************************************")  
  
  for line in blossum50_matrix_alignment_scores:
      print(line)
  print(" ")
  print("Min, Max")
  for i in range(len(genome_sequences)):
      print(f"{i}: {min(blossum50_matrix_alignment_scores[i])},{max(blossum50_matrix_alignment_scores[i])}")
    
  print("\n\n*******************************************************************************************")    
  print("\nSubstitution Matrix")
  print("*******************************************************************************************\n\n")  
  
  for i in range(len(genome_sequences)):
      for j in range(len(genome_sequences)):
          if i != j:
              substitution_matrix_alignment_scores[i][j] = substitution_matrix_aligned_sequences.calculate_alignment_score(genome_sequences[i], genome_sequences[j])
              print(f"{i+1},{j+1} Score: {substitution_matrix_alignment_scores[i][j]}")
              substitution_matrix_aligned_sequences.print_best_alignment_score_from_previous_pair()
              print(" ")
  
  print("\n\n*******************************************************************************************")  
  print("\nSubstitution Matrix Alignment Scores")
  print("*******************************************************************************************\n\n")  
  
  for line in substitution_matrix_alignment_scores:
      print(line)
  print(" ")
  print("Min, Max")
  for i in range(len(genome_sequences)):
      print(f"{i}: {min(substitution_matrix_alignment_scores[i])},  {max(substitution_matrix_alignment_scores[i])}")