# SAT-Solver
Implementation of DPLL Algorithm in python,  it takes input from a file in Dimacs format specifying a cnf formula.


# How to use
Type in python dpll__solver.py to execute the python script,
Then It appears the prompt: "Type the name of the file.txt : " so It needs the name of the file (for example satisfable.txt), and the prompt:"Type the name of the file.txt where you want to write the output".
# Example
Let the input be:

```
c simple satisfable formula
c  
p cnf 3 6
1 2 0
1 -2 0
3 2 0
-3 1 0
1 2 3 0
-1 -2 0 
```

The output is

```
-2 3 1
```
Here, the formuls is satisfiable. Variables -2,1,3 are assigned true.

# Considerations 
The algorithm returns "0" if the formula is unsatisfable and if it doesn't find a valuation (i.e. a vector of assignments that it brings the formula to be True).



