# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 11:01:24 2020

@author: 38670
"""  


import random   
def selectliteral(cnf):
    return random.choice(cnf)[0]  

def notliteral(literal):
    if '-' not in literal:
        return "-"+literal
    if '-' in literal:   
        return literal.replace('-','') 

def remove_clause(cnf,literal):
    cnf=[clause for clause in cnf if literal not in clause]
    return cnf

def remove_notliteral(cnf, literal):
    nl = notliteral(literal)
    for clause in cnf:
        if nl in clause:
            clause.remove(nl)
    return cnf
            
def cnf_has_a_clause_false(cnf):
    if any([c==["0"] for c in cnf]):
        return True
    else:
        return False

def dpll(cnff,val):  
    if len(cnff) == 0:
        return val
    if cnf_has_a_clause_false(cnff)==False:
        l = selectliteral(cnff) 
        cnff = remove_clause(cnff,l) 
        cnff = remove_notliteral(cnff, l) 
        val.append(l) 
        return dpll(cnff,val) 
    
    if cnf_has_a_clause_false(cnff)==True: 
        cnff = [row.split()  for row in list]
        val.pop() 
        for l in val:
            cnff = remove_clause(cnff,l) 
            cnff = remove_notliteral(cnff, l)
        return dpll(cnff,val)
    
  
list = open("file.txt").readlines()[3:]
cnf2 = [row.split()  for row in list]

d=dpll(cnf2,[])   
f=str(' '.join(d))

file = open("file_solution.txt",'w') 
 
file.write(f)
file.close() 

    
    
    