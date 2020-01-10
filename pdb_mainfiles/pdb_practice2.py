#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 11:20:20 2020

@author: serenerodrigues
"""

# 1) print only the XYZ coordinates for the first 20 residues
# 2) print only the XYZ coordinates for the GLN residues
# 3) print only XYZ coordinates for the CA atoms
# 4) save data from 3) into a file in the format
## 0.0000
## 0.0000
## 0.0000
## where 0.0000 is the X coordinate of each alpha atom.

import numpy as np

file = open('1A2Y_B.pdb','r')
lines = file.readlines()
file.close()

x_y_z_coords = []
gln = []

for line in lines:
    coord_x = float(line[30:38])
    coord_y = float(line[38:46])
    coord_z = float(line[46:54])
    
    x_y_z_coords.append([coord_x, coord_y, coord_z])
    
    gl_n = str(line[17:20].strip())
    gln.append(gl_n)
    

resname = np.array(gln)

xyz_a = np.array(x_y_z_coords)

gln_only_coords = xyz_a[resname == 'GLN']

print(gln_only_coords)

