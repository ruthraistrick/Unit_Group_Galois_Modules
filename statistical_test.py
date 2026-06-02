import subprocess

username = input("SSH username: ").strip()
host = input("SSH host: ").strip()

magma_code = """
load "RepAsMatrixCyclic.magma";
load "C4_extensions.magma";
load "fields_magma.m";

Fields := make_data();
n := #Fields;

CountA := 0;
CountB := 0;

IntegralMatrices := [
    Matrix(Integers(),3,3,[[-1,0,0],[0,0,-1],[0,1,0]]),
    Matrix(Integers(),3,3,[[0,-1,1],[1,0,0],[0,0,-1]])
];

for i in [1..n] do
    Gmod, Mat := C4UnitStructure(Fields[i]`field);

    if Mat eq IntegralMatrices[1] then
        CountA +:= 1;
    else
        CountB +:= 1;
    end if;
end for;

print "CountA:", CountA;
print "CountB:", CountB;
print "Ratio:", RealField(20)!CountA/n;

quit;
"""

remote = f"""
set -e

if [ ! -d Unit_Group_Galois_Modules ]; then
    git clone https://github.com/ruthraistrick/Unit_Group_Galois_Modules.git
else
    cd Unit_Group_Galois_Modules
    git pull
    cd ..
fi

cd Unit_Group_Galois_Modules

cat > run.m <<'EOF'
{magma_code}
EOF

magma run.m
"""

result = subprocess.run(
    ["ssh", f"{username}@{host}"],
    input=remote,
    text=True,
    capture_output=True
)

print(result.stdout)

if result.returncode != 0:
    print("ERROR:")
    print(result.stderr)
