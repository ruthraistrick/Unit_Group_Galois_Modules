import subprocess

username = input("Glasgow username: ").strip()
poly = input("Irreducible polynomial in x such that its splitting field has a cyclic group of order 4 as Galois group(e.g. x^4+x^3+x^2+x+1) : ").strip()

remote = f"""
set -e

if [ ! -d Unit_Group_Galois_Modules ]; then
    git clone https://github.com/ruthraistrick/Unit_Group_Galois_Modules
fi

cd Unit_Group_Galois_Modules

magma <<EOF
R<x> := PolynomialRing(Rationals());

K<a> := NumberField({poly});

load "C4_extensions.magma";

C4UnitStructure(K);

quit;
EOF
"""

subprocess.run(
    ["ssh", f"{username}@euclid-36.maths.gla.ac.uk"],
    input=remote,
    text=True
)
