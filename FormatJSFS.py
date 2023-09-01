#!/usr/bin/env python

#setup args
import argparse, sys 
import numpy as np          
msg = "Takes flattened output from 2D realsfs and creates a matrix output for use with fastsimcoal2"

parser = argparse.ArgumentParser(description = msg)
parser.add_argument("-i", "--Input", help = "Input file from realSFS", required=True)
parser.add_argument("-n1", help = "Number of diploid individuals in population 1", required=True)
parser.add_argument("-n2", help = "Number of diploid individuals in population 2", required=True)
args = parser.parse_args()

#input 
sfs_file = args.Input
n1 = int(args.n1)
n2 = int(args.n2)
#read in file
with open(sfs_file, 'r') as file:
    sfs_data = file.read().strip().split()
sfs_data = [float(x) for x in sfs_data]

#define functions
def add_last_to_first(input_sfs):
    if len(input_sfs) >= 2:
        input_sfs[0] += input_sfs[-1]
        input_sfs[-1] = 0
    return input_sfs

def unflatten_sfs(sfs_data, n1, n2):
    ncols = 2 * n1 + 1
    nrows = 2 * n2 + 1
    return np.array(sfs_data).reshape((nrows, ncols))

def round_matrix(matrix):
    """Round all values in the matrix to integers."""
    return [[int(round(val)) for val in row] for row in matrix]

def format_matrix_to_obs(matrix):
    header_row = "1\tobservations"
    column_names = ["d0_{}".format(i) for i in range(len(matrix[0]))]
    column_names_row = "\t" + "\t".join(column_names)
    data_rows = ["d1_{}\t{}".format(i, "\t".join(map(str, row))) for i, row in enumerate(matrix)]
    return header_row + "\n" + column_names_row + "\n" + "\n".join(data_rows)

def save_to_file(content, file_path):
    with open(file_path, "w") as file:
        file.write(content)

# Processing steps
sfs_data = add_last_to_first(sfs_data)
matrix = unflatten_sfs(sfs_data, n1, n2)
matrix = round_matrix(matrix)
matrix = format_matrix_to_obs(matrix)

output_path = 'format_' + sfs_file
save_to_file(matrix, output_path)
