Given a tower that is made up of these 6 blocks:
- True (T)
- False (F)
    (The value of the following are based on all blocks below them (not just in their column))
- all (A): exactly 0 F
- any (Y): at least 1 T
- none (N): exactly 0 T
- some (S) : at least one F and at least one T

find how many blocks are false in the whole building


recompute expression blocks

                
NTAT    A    Y    N    S
YTST    A(F)    Y(T)    N(F)    S(T)
FTFF    A(F)    Y(T)    N(F)    S(T)
FATN    A(T)    Y(T)    N(F)    S(F)
TFTT    


FTFT
TTTT
FTFF
FTTF
TTTT