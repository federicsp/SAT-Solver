# SAT-Solver
Implementation of DPLL Algorithm in python.


# How to use
Type in python dpll__solver.py to execute the python script,
then It appears the prompt: "Type the name of the file.txt : " so It needs the name of the file (for example satisfable.txt)

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
-1 -2 0");
}
```

The output is

```
-2 3 1
```
Here, the formuls is satisfiable. Variables -2,1,3 are assigned true.

# Considerations
The algorithm works only with small formulas, it doesn't work with the mini_sudoku.txt and more complex formulas.

The algorithm returns "0" if the formula is unsatisfable and if it doesn't find a valuation (i.e. a vector of assignments that it brings the formula to be True).



