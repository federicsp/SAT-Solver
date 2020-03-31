# SAT-Solver
Implementation of DPLL Algorithm in python.


# How to use
Type in python dpll__solver.py to execute the python script,
then It appears the prompt: "Type the name of the file.txt : " so It needs the name of the file (for example satisfable.txt). The solution is written on file_solution.txt

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
The algorithm  doesn't work with long formulas ( for example the mini_sudoku.txt and more complex formulas), I tried to implement different ways to improve the algorithm: for example seeking better ways to select the literal or going back to some particular time after an unsuccesful recursion (and restarting from there the recursion) but it didn't work.

The algorithm returns "0" if the formula is unsatisfable and if it doesn't find a valuation (i.e. a vector of assignments that it brings the formula to be True).



