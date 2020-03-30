# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 21:20:35 2020

@author: 38670
""" 

from dpll import dpll
  
list = open("file.txt").readlines()[3:]
cnf2 = [row.split()  for row in list]

d=dpll(cnf2,[])   
f=str(' '.join(d))

file = open("file_solution.txt",'w') 
 
file.write(f)
file.close() 


