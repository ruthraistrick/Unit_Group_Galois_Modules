function C4UnitStructure(K)
    F := Rationals();
    G := GaloisGroup(K);
    C4 := CyclicGroup(4);
    if IsIsomorphic(G,C4) then
        r1, r2 := Signature(K);
        OK := RingOfIntegers(K);
        Ugp, Umap := UnitGroup(OK);
        Aut := Automorphisms(K);
        if r1 eq 0 and r2 eq 2 then  //deals with the easy case - 4 complex roots
            gen1 := K ! Umap(Ugp.2);
            if Aut[2](gen1) eq -1*gen1 or Aut[2](gen1) eq gen1 then
                return Matrix(Rationals(),1,1,[1]);
            else 
                return Matrix(Rationals(),1,1,[-1]);
            end if;
        elif r1 eq 4 and r2 eq 0 then //deals with harder case - 4 real roots
            function RepAsMatrix(K) //turns the action of the generator into a matrix
                OK := RingOfIntegers(K);
                Ugp, Umap := UnitGroup(OK);
                Aut := Automorphisms(K);
                gen1 := K ! Umap(Ugp.2); //generators of free part of unit group
                gen2 := K ! Umap(Ugp.3);
                gen3 := K ! Umap(Ugp.4);
                Gens := [gen1, gen2, gen3];
                function Vector(g)
                    action := (OK ! (Aut[2](g))) @@ Umap;
                    coords := ElementToSequence(action);
                    correctcoords:= coords[2..4];
                    return correctcoords;
                end function;
                M := Transpose(Matrix(F, 3, 3, &cat[Vector(g) : g in Gens]));
                return M;
            end function;
            M := RepAsMatrix(K);
            L := FiniteField(2,1);
            M2 := ChangeRing(M,L);
            threedimreps := [ 
                Matrix(L,3,3, [[-1,0,0], [0,0,-1], [0,1,0]]), 
                Matrix(L,3,3,[[0,-1,1],[1,0,0],[0,0,-1]]),
                Matrix(L,3,3, [[1,1,0],[0,0,-1],[0,1,0]])];
            FiniteSimilarMatrices := [];
            for i in threedimreps do
                if IsSimilar(M2, i) eq true then
                Append(~FiniteSimilarMatrices, i);
                end if;
            end for;
            if #FiniteSimilarMatrices eq 1 then // This asks if we have B+C
                return Matrix(F,3,3, [[-1,0,0], [0,0,-1], [0,1,0]]);
            else 
                ratthreereps := [ Matrix(F,3,3,[[0,-1,1],[1,0,0],[0,0,-1]]),
                Matrix(F,3,3, [[1,1,0],[0,0,-1],[0,1,0]])
                ];
                for i in ratthreereps do
                    if IsSimilar(M,i) eq true then
                        return i;
                    end if;
                end for;    
            end if;

        else
            return "Can't do";
        end if;
    else 
        return "This function is only for C4 extensions";
    end if;
end function;   
