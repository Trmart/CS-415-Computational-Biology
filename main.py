"""
  Taylor Martin
  CS-415: Computational Biology
  Project 4
  Dr. Terry Soule
  Spring 2023
  5/10/2023

  FILE: Main.py

"""

from DataLoader import load_data
from Utils import perform_alignment_and_scoring
import GenomeAligner

def main():
  """Project 4 Main"""
  
  genome_sequences, blossum50_matrix, substitution_matrix = load_data()

  substitution_matrix_aligned_sequences = GenomeAligner.GenomeAligner(substitution_matrix, -1)
  blossum50_matrix_aligned_sequences = GenomeAligner.GenomeAligner(blossum50_matrix, -2)
  blossum50_matrix_alignment_scores = [[250 for i in range(8)] for i in range(8)]
  substitution_matrix_alignment_scores = [[610 for i in range(8)] for i in range(8)]
  
  perform_alignment_and_scoring(genome_sequences,substitution_matrix_aligned_sequences,blossum50_matrix_aligned_sequences,blossum50_matrix_alignment_scores, substitution_matrix_alignment_scores)
  

if __name__ == "__main__":
  main()