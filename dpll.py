# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 11:01:24 2020

@author: 38670
"""  


import random 
    
def selectliteral(cnf): 
    if cnf:
        for clause in cnf:
            if len(clause)==2:
                return clause[0]
    else:
        randomclause= random.choice(cnf)
        randomclause.pop()
        randomliteral=random.choice(randomclause) 
        return randomliteral
        

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
 
k=0    
    
def dpll(cnff,list_cnf,val):
    global k
    k=k+1
    if k==2000:
        return "0"
    if len(cnff) == 0:
        return val
    if cnf_has_a_clause_false(cnff)==False: 
        l = selectliteral(cnff) 
        cnff = remove_clause(cnff,l) 
        cnff = remove_notliteral(cnff, l) 
        val.append(l)  
        return dpll(cnff,list_cnf,val) 
    
    if cnf_has_a_clause_false(cnff)==True:   
        cnff=[row.split()  for row in list_cnf]      
        return dpll(cnff,list_cnf,[])
    
 
    
    