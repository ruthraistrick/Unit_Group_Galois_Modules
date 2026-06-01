## What this Code Does
The code in this repository calculates the integral galois module structure of the free part of the unit group 
of the ring of integers of a $C_4$ extension of $ℚ$. We briefly explain the algorithm as follows. Throughout let $\Gamma_K$ denote the free part of the unit group of the ring of integers of a number field $K$.
\
There exists two different cases, $C4$ number fields of signature $(0,2)$ and those of signature $(4,0)$. The first case is simple, Dirichlet's unit theorem gives us that $\Gamma_K$ is of rank 1. It follows that we have that $\text{Gal}(K/ℚ)$ acts trivially or by multiplication by $-1$ - we clearly have the latter since the former would imply that there existed a unit of infinite order in $ℚ$. 
\
Suppose now we are in the latter case. Again we use Dirichlet's unit theorem to give that $\Gamma_K$ is of rank $3$. Roiter's
"On the representations of the cyclic group of fourth order by integral matrices." gives us that there are 2 irreducible integral $C4$ modules of rank 1, 2 of rank 2 and 2 of rank 3. They are as follows: 
\
\begin{equation}
\begin{bmatrix} 1 \end{bmatrix}
\end{equation}
\
$$\begin{bmatrix} -1 \end{bmatrix}$$
\
$$\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$$
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
