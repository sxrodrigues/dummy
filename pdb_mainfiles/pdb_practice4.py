#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 11:25:38 2020

@author: serenerodrigues
"""

# 4) save data from 3) into a file in the format
## 0.0000
## 0.0000
## 0.0000
## where 0.0000 is the X coordinate of each alpha atom.

import numpy as np

file = open('1A2Y_B.pdb','r')
lines = file.readlines()
file.close()

xyz_coords = []
ca = []

for line in lines:
    coord_x = float(line[30:38])
    coord_y = float(line[38:46])
    coord_z = float(line[46:54])
    
    xyz_coords.append([coord_x, coord_y, coord_z])
    
    c_a = str(line[12:16].strip())
    ca.append(c_a)
    

atom_name = np.array(ca)

xyz_a = np.array(xyz_coords)

ca_only_coords = xyz_a[atom_name == 'CA']

# print(ca_only_coords)
x = ca_only_coords[:,0]
x_coords_only = np.array(x)

print(x_coords_only.shape)
x_to_file = np.reshape(x_coords_only, (116,1))

print(x_to_file)
f = open("X coordinates of ea alpha atom.txt","w")
f.writelines(str(x_to_file))
f.close()