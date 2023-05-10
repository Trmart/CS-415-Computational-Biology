"""
  Taylor Martin
  CS-415: Computational Biology
  Project 4
  Dr. Terry Soule
  Spring 2023
  5/10/2023

  FILE: DataLoader.py

"""

import json

def load_data():
  """
  Loads data from project4data
  Load Blossum50 Matrix 
  Loads Substitution Matrix
  """
  genome_sequences = []
  
  #open and load data from project4data-1.txt
  f = open("project4data-1.txt")
  for line in f:
      genome_sequences.append(line[0:-1])
  f.close()

  #open and load data from project4data-1.txt
  f = open("blossum50.json")
  blossum50_matrix = json.load(f)
  f.close()
  
  #open and load data from project4data-1.txt
  f = open("substitution_matrix.json")
  substitution_matrix = json.load(f)
  f.close()
  

  return genome_sequences, blossum50_matrix, substitution_matrix