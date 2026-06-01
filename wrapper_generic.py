import subprocess

host = input("SSH host (e.g. compute64y.maths.ed.ac.uk): ").strip()
username = input("Username: (e.g. s2681244) ").strip()
poly = input("Polynomial in x (use * for multiplication) giving rise to a Galois extension with a cyclic Galois group of order 4 over the rationals : ").strip()

magma_code = f"""
R<x> := PolynomialRing(Rationals());

K<a> := NumberField({poly});

load "Better_C4_extensions.magma";

C4UnitStructure(K);

quit;
"""

remote = f"""
set -e

if [ ! -d Unit_Group_Galois_Modules ]; then
    git clone https://github.com/ruthraistrick/Unit_Group_Galois_Modules
fi

cd Unit_Group_Galois_Modules

printf "%s" {repr(magma_code)} | magma
"""

subprocess.run(
    ["ssh", f"{username}@{host}"],
    input=remote,
    text=True
)