#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 16:12:40 2020

@author: serenerodrigues
"""

# read all XYZ coordinates from the PDB to a (N, 3)

# 1) print only the XYZ coordinates for the first 20 residues
# 2) print only the XYZ coordinates for the GLN residues
# 3) print only XYZ coordinates for the CA atoms
# 4) save data from 3) into a file in the format
## 0.0000
## 0.0000
## 0.0000
## where 0.0000 is the X coordinate of each alpha atom.

import numpy as np

file_ = open('1A2Y_B.pdb','r')
lines = file_.readlines()
file_.close()

x_y_z_coords = []
residue_numbers = []


for line in lines:
    coord_x = float(line[30:38])
    coord_y = float(line[38:46])
    coord_z = float(line[46:54])
    
    x_y_z_coords.append([coord_x, coord_y, coord_z])
    
    residue_numbers.append(float(line[22:26]))


resnuma = np.array(residue_numbers)
xyz_a = np.array(x_y_z_coords)

print(xyz_a)
first20 = xyz_a[resnuma <= 20]
print(first20)
print(len(first20))
print(first20.size)
print(first20.shape)


# #######--TESTING--BELOW--#################

# new_array = np.array(x_y_z_coords)
# final_copy = []

# for first in new_array:
#     f_twenty = float(line[22:26])
#     if f_twenty not in final_copy and f_twenty < 20:
#         final_copy.append(lines)

# print(final_copy)
    


# for lin in lines:
#     number = float(lin[22:26])
#     if number < 20:
#         print(len(lines))
        

#     if not in thingy and if number<20

# for lin in lines:
#     number = float(lin[22:26])
#   #   print(number)
#     if number < 20.0:
#         new_array = np.array(number)
#         print(str(new_array))
#         print(len(new_array))
    

        

