# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 08:39:58 2020

@author: 38670
"""


from dpll import dpll

def main(): 
    txt = input("Type the name of the file.txt : ")
    txt_output= input("Type the name of the file.txt where you want to write the output' : ")
    list = open(txt).readlines()[3:]
    cnf2 = [row.split()  for row in list]
    d=dpll(cnf2,list,[])   
    f=str(' '.join(d))
    output = open(txt_output,'w') 
    output.write(f) 
    
    


if __name__ == '__main__':
    main()