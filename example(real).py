import subprocess
import os

HOST = "s2688857@compute64y.maths.ed.ac.uk"
REPO = "Unit_Group_Galois_Modules"

poly = "x^4 - 4*x^2 + 2"

# -----------------------------
# clone repo if needed
# -----------------------------
if not os.path.isdir(REPO):
    subprocess.run([
        "git",
        "clone",
        "https://github.com/ruthraistrick/Unit_Group_Galois_Modules"
    ], check=True)

# -----------------------------
# clean Magma script (NO escaping hell)
# -----------------------------
magma_script = f"""
cd {REPO}

magma <<EOF
R<x> := PolynomialRing(Rationals());

K<a> := NumberField({poly});

load "Better_C4_extensions.magma";

C4UnitStructure(K);

quit;
EOF
"""

# -----------------------------
# send directly to ssh stdin
# -----------------------------
subprocess.run(
    ["ssh", HOST],
    input=magma_script,
    text=True
)
