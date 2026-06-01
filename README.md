The code in this repository calculates the integral galois module structure of the free part of the unit group 
of the ring of integers of a $C_4$ extension of $ℚ$.
## What's In Each File and How To Run The Code
Files of the form `.magma` contain code written in the software package Magma: files of the form `.py` contain code written in Python. Please note that all code is originally written in Magma, the python code is simply a wrapper. 
  * The file `RepAsMatrixCyclic.magma` contains a function that inputs cyclic extension of $ℚ$,
    $K$ and any field $F$ and outputs the action of the generator of $\text{Gal}(K/ℚ)$ on the free part of the unit group of 
    the ring of integers of $K$ as a matrix with coefficents in $F$. 
  * The file `C4_extensions.magma` contains a function that inputs $C_4$ extensions of $ℚ$ and outputs a matrix with 
     coefficents in $\mathbb{Q}$ representing the integral galois module structure of the unit group of the ring of integers        of $K$. To run this function you must first run `RepAsMatrixCyclic.magma` as the function defined here is necessary in         running the function in `C4_extensions.magma`.
  *  
