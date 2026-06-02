## What this Code Does
The code in this repository calculates the integral galois module structure of the free part of the unit group 
of the ring of integers of a $C_4$ extension of $ℚ$. We briefly explain the algorithm as follows. Throughout let $\Gamma_K$ denote the free part of the unit group of the ring of integers of a number field $K$.
\
There exists two different cases, $C4$ number fields of signature $(0,2)$ and those of signature $(4,0)$. The first case is simple, Dirichlet's unit theorem gives us that $\Gamma_K$ is of rank 1. It follows that we have that $\text{Gal}(K/ℚ)$ acts trivially or by multiplication by $-1$ (that is, by sending a fundamental unit to its inverse) - we clearly have the latter since the former would imply that there existed a unit of infinite order in $ℚ$. 
\
Suppose now we are in the latter case. Again we use Dirichlet's unit theorem to give that $\Gamma_K$ is of rank $3$. Roiter's
"On the representations of the cyclic group of fourth order by integral matrices." gives us that there are 2 irreducible integral $C4$ modules of rank 1, 2 of rank 2 and 2 of rank 3. They are as follows (here we represent the action of the generator of $C4$ as a matrix): 
\
$`A := \begin{bmatrix} 1 \end{bmatrix}`$
\
$` B:= \begin{bmatrix} -1 \end{bmatrix}`$
\
$` C:=\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}`$
\
$`D :=\begin{bmatrix} 1 & 1 \\ 0 & -1 \end{bmatrix}`$
\
$`E :=\begin{bmatrix} 0 & -1 & 1 \\ 1 & 0 & 0 \\ 0 & 0 & -1 \end{bmatrix}`$
\
$` F :=\begin{bmatrix} 1 & 1 & 0 \\ 0 & 0 & -1 \\ 0 & 1 & 0 \end{bmatrix}.`$
Again we cannot have a non-trivial subspace fixed the galois action else we would have a unit of infinite order in $ℚ$. Excluding the matrices with eigenvalue $1$ we are left with $B$, $C$, and $E$. It follows that we either have $\Gamma_K$ isomorphic to three copies of $B$, $C \oplus B$ or $E$. However we see that three copies of $B$ is impossible. We are left with having to write an algorithm that tells apart $C \oplus B$ and $E$. Tensoring with the finite field of degree $2$ gives us two non-similar matrices. Our algorithm is therefore as follows: given $K$ we produce a matrix associated to the galois action on $\Gamma_K$ then ask which of the two matrices this is similar to after tensoring with $F_2$.  
## What's In Each File and How To Run The Code
Files of the form `.magma` contain code written in the software package Magma: files of the form `.py` contain code written in Python. Please note that all code is originally written in Magma, the python code is simply a wrapper. 
  * The file `RepAsMatrixCyclic.magma` contains a function that inputs cyclic extension of $ℚ$,
    $K$ and any field $F$ and outputs the action of the generator of $\text{Gal}(K/ℚ)$ on the free part of the unit group of 
    the ring of integers of $K$ as a matrix with coefficents in $F$. 
  * The file `C4_extensions.magma` contains a function that inputs $C_4$ extensions of $ℚ$ and outputs a matrix with 
     coefficents in $\mathbb{Q}$ representing the integral galois module structure of the unit group of the ring of integers        of $K$. To run this function you must first run `RepAsMatrixCyclic.magma` as the function defined here is necessary in         running the function in `C4_extensions.magma`. After running the file, where $K$ is a $C4$ number field run
    ```
    C4UnitStructure(K);
    ```
     The function returns a matrix, if you would like a representation, run
    ```
       C4 := CyclicGroup(4); 
       GModule(C4,C4UnitStructure(K));
    ```
  *  `C4_extensions.magma` contains (what we believe to be) all integral irreducible $C4$ representions both as matrices and as $C4$-modules.
  *  Running the file `Statistical_Test.magma` will allow you to run a statistical test on $C4$ number fields with signature $(4,0)$ to see how often each of the possible two structures occurs. To run this you must first go to the [LMFDB](https://www.lmfdb.org/) and download a list of $C4$ number fields of signiture $(4,0)$ ordered by discrimiant. The list produced here must first be run before `Statistical_Test.magma` can. The output gives the proportion of the number of times the non irreducible case occurs.
  *  `fields_magma.m` contains the list of number fields mentioned above.
  *  `statistical_test.py` is a python file that runs the aforementioned statistical test.
  *  The file `python_wrapper_generic.py` is a python file that allows the user to execute the magma file `C4_extensions.magma` for a polynomial the user must enter after executing it. When running the python file, it asks the user for a server where magma is installed and a username (followed by a password) to access it, on top of the aforementioned polynomial.
  *   The files `python_wrapper_edinburgh.py` and `python_wrapper_glasgow.py` do the same as the generic wrapper, but only require a username for those with an Edinburgh or a Glasgow account, respectively (because the servers containing magma are specified within the code).
  *   The files `example(imaginary).py` and `example(real).py` are two python files that run one example each as reality check. They are prescribed with $f=x^4+x^3+x^2+x^2+1$ and $f=x^4-4x^2+2,$ respectively. To run them, one needs to edit the server with magma within the file (same as the generic python wrapper above for these specific polynomials, except this time the program does not ask the user to enter the server).
  *   The file `presentation_slides.pdf` contains some slides that are a bit more introductory than the explanation above.
    
