# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 08:39:58 2020

@author: 38670
"""


from dpll import dpll

def main(): 
    txt = input("Type the name of the file.txt : ")
    list = open(txt).readlines()[3:]
    cnf2 = [row.split()  for row in list]
    d=dpll(cnf2,list,[])   
    f=str(' '.join(d))
    output = open("file_solution.txt",'w') 
    output.write(f) 
    
    


if __name__ == '__main__':
    main()