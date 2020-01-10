#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 11:23:19 2020

@author: serenerodrigues
"""

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

print(ca_only_coords)


#i know i put float but why it's giving this one in scientific notation and not
#just in 54.9948 like the others i am not sure