#!/usr/bin/env python
# encoding: utf-8

name = ""
shortDesc = u""
longDesc = u"""

"""
entry(
    label = "Ods",
    group =
"""
1 O ux c0 {2,D} {3,S}
2 R ux {1,D}
3 R ux {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
This forbids O with both single and double bonds WHILE keeping a zero partial charge.
This does not forbid ozone, [O-][O+]=O
""",
)

entry(
    label = "Od_rad",
    group = 
"""
1 O u1 {2,D}
2 R ux {1,D}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    label = "N_birad_triplet_2singleBonds",
    group = 
"""
1 N u2 p0 {2,S} {3,S}
2 R ux {1,S}
3 R ux {1,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    label = "C_quintet",
    molecule =
"""
1 C u4 p0
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    label = "Carbene_D_triplet",
    group =
"""
1 C u2 p0 {2,D}
2 C u0 {1,D}
""",
    shortDesc = u"""""",
    longDesc =
u"""
restricts C2O, see RMG-Py issue #514
""",
)

entry(
    label = "Carbene_S_triplet",
    group =
"""
1 C   u2 p0 {2,S}
2 R!H u0 {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    label = "O3",
    group = 
"""
1 O u[0,1] {2,S}
2 O u0     {1,S} {3,S}
3 O u[0,1] {2,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    label = "O4..",
    group = 
"""
1 O u1 {2,S}
2 O u0 {1,S} {3,S}
3 O u0 {2,S} {4,S}
4 O u1 {3,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    label = "cyclic-C3O",
    group = 
"""
1 C u0 {2,D} {3,S} {4,S}
2 O u0 {1,D}
3 C u0 {1,S} {4,T}
4 C u0 {1,S} {3,T}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    label = "cyclobutyne",
    group =
"""
1 R!H ux {2,T} {4,S}
2 R!H ux {1,T} {3,S}
3 R!H ux {2,S} {4,[S,D,T,B]}
4 R!H ux {1,S} {3,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
""",
)

entry(
    label = "CO_birad",
    species =
"""
multiplicity 3
1 C u2 p0 c0 {2,D}
2 O u0 p2 c0 {1,D}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbidden after discussion with whgreen.
This species should quickly transform into a closed shell [C-]#[O+].
We don't need it as a resonance structure of carbon monoxide for reactivity since carbon monoxide has its designated
reaction families (CO_Disprop, R_Add_COm).
""",
)

entry(
    label = "CS_birad",
    species =
"""
multiplicity 3
1 C u2 p0 c0 {2,D}
2 S u0 p2 c0 {1,D}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbidden after discussion with whgreen.
This species should quickly transform into a closed shell [C-]#[S+] similar to the carbon monoxide case above.
We don't need it as a resonance structure of carbon monsulfide for reactivity since carbon monsulfide has its designated
reaction families (CO_Disprop [also deals with CS], R_Add_CSm).
""",
)

entry(
    label = "N-N(S)",
    species =
"""
1 N u0 p2 c0 {2,S}
2 N u0 p2 c0 {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
This structure is not a stationary point, and should quickly become N#N
""",
)

entry(
    label = "[N][N]",
    species =
"""
multiplicity 5
1 N u2 p1 c0 {2,S}
2 N u2 p1 c0 {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
N#N can be excited to [N]=[N], but we shouldn't allow it to reach [N][N]
""",
)

entry(
    label = "SOO2",
    species =
"""
multiplicity 3
1 S u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 O u1 p2 c0 {1,S}
4 O u1 p2 c0 {2,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
The SO--O2 complex isn't a sable species (i.e., its geometry cannot be optimized with a reasonable SO--OO bond length),
yet it is predicted by RMG, e.g, by R_Recombination of [S][O] and [O][O].

Another resonance structure of it which is forbidden as well via this entry is:
multiplicity 3
1 S u1 p1 c0 {2,S} {3,D}
2 O u0 p2 c0 {1,S} {4,S}
3 O u0 p2 c0 {1,D}
4 O u1 p2 c0 {2,S}
""",
)

entry(
    label = "SO2O2",
    species =
"""
multiplicity 3
1 S u0 p1 c0 {2,S} {3,S} {4,D}
2 O u0 p2 c0 {1,S} {5,S}
3 O u1 p2 c0 {1,S}
4 O u0 p2 c0 {1,D}
5 O u1 p2 c0 {2,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
The SO2--O2 complex isn't a sable species (i.e., its geometry cannot be optimized with a reasonable O2S--OO bond length),
yet it is predicted by RMG, e.g, by R_Addition_Multiple_Bond of O=S=O and [O][O].
Also, it is described as a TS in doi: 10.1021/jp067499p (Fig. 1 structure 5, Fig. 2)

Another resonance structure of it which is forbidden as well via this entry is:
multiplicity 3
1 S u1 p0 c0 {2,S} {3,D} {4,D}
2 O u0 p2 c0 {1,S} {5,S}
3 O u0 p2 c0 {1,D}
4 O u0 p2 c0 {1,D}
5 O u1 p2 c0 {2,S}
""",
)

entry(
    label = "S2O2",
    species =
"""
multiplicity 3
1 O u0 p2 c0 {2,S} {3,S}
2 S u0 p2 c0 {1,S} {4,S}
3 O u1 p2 c0 {1,S}
4 S u1 p2 c0 {2,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
The S2--O2 complex isn't a sable species (has an imaginary frequency),
yet it is predicted by RMG, e.g, by R_Recombination of [S][S] and [O][O].

Another resonance structure of it which is forbidden as well via this entry is:
multiplicity 3
1 O u0 p2 c0 {2,S} {3,S}
2 S u1 p1 c0 {1,S} {4,D}
3 O u1 p2 c0 {1,S}
4 S u0 p2 c0 {2,D}
""",
)

entry(
    label = "N2SH",
    species =
"""
multiplicity 2
1 N u0 p0 c+1 {2,D} {3,D}
2 S u1 p1 c0 {1,D} {4,S}
3 N u0 p2 c-1 {1,D}
4 H u0 p0 c0 {2,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
The N2--SH complex isn't a sable species (i.e., its geometry cannot be optimized with a reasonable NN--SH bond length),
yet it is predicted by RMG, e.g, by R_Addition_Multiple_Bond of [SH] to N#N.

Other resonance structures of it which are forbidden as well via this entry are:
multiplicity 2
1 N u0 p1 c0 {2,S} {3,D}
2 S u0 p2 c0 {1,S} {4,S}
3 N u1 p1 c0 {1,D}
4 H u0 p0 c0 {2,S}

multiplicity 2
1 N u1 p0 c+1 {2,S} {3,D}
2 S u0 p2 c0 {1,S} {4,S}
3 N u0 p2 c-1 {1,D}
4 H u0 p0 c0 {2,S}
""",
)

entry(
    label = "N2SO",
    group =
"""
1 O u0 {2,[S,D]}
2 S u0 {1,[S,D]} {3,[S,D]}
3 N u0 {2,[S,D]} {4,[S,D]}
4 N u0 {3,[S,D]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
The N2--SO complex isn't sable (i.e., NNSO's geometry cannot be optimized with a reasonable NN--SO bond length),
yet it is predicted by RMG, e.g, by R_Addition_Multiple_Bond of [S][O] to N#N.
N2SO2 is forbidden as well in this group for the same reason.
""",
)

entry(
    label = "SO3(T)",
    species =
"""
multiplicity 3
1 O u0 p2 c0 {2,D}
2 S u1 p0 c0 {1,D} {3,D} {4,S}
3 O u0 p2 c0 {2,D}
4 O u1 p2 c0 {2,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
The geometry of SO3(T) could not be stabilized at either B3LYP/6-311G(2d,d,p) nor M06-2x
without getting negative frequency/ies.
""",
)

entry(
    label = "cN3HNH2",
    species =
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 N u0 p1 c0 {1,S} {4,S} {5,S}
3 N u0 p1 c0 {1,S} {6,S} {7,S}
4 N u1 p1 c0 {1,S} {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Geometry could not converge at CBS-QB3
""",
)

entry(
    label = "cN3HN",
    group =
"""
1 N u0     p1 c0 {2,S} {3,S} {5,S}
2 N u[0,1] p1 c0 {1,S} {3,S}
3 N u0     p0 c+1 {1,S} {2,S} {4,D}
4 N u0     p2 c-1 {3,D}
5 R ux     px cx {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Geometry of the following species in this group could not converge at CBS-QB3
[N-]=[N+]1[N]N1
[N-]=[N+]1NN1
""",
)

entry(
    label = "NH3NNH",
    species =
"""
multiplicity 2
1 N u0 p0 c+1 {2,S} {4,S} {5,S} {6,S}
2 N u0 p2 c-1 {1,S} {3,S}
3 N u1 p1 c0 {2,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Geometry could not converge at wB97x-D3/6-311++G(3df,3pd) (alongd ref - xq1488)
""",
)

entry(
    label = "NNHNH",
    species =
"""
multiplicity 2
1 N u0 p0 c+1 {2,S} {3,D} {5,S}
2 N u0 p1 c0 {1,S} {4,D}
3 N u0 p2 c-1 {1,D}
4 N u1 p1 c0 {2,D}
5 H u0 p0 c0 {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Geometry could not converge at wB97x-D3/6-311++G(3df,3pd) (alongd ref - xq1492)
""",
)

entry(
    label = "C2_triplebond",
    species =
"""
1 C u0 p1 c-1 {2,T}
2 C u0 p0 c+1 {1,T}
""",
    shortDesc = u"""""",
    longDesc =
u"""
https://pubs.acs.org/doi/pdf/10.1021/ct400867h discusses complex wavefunction for C2
and that it cannot be assigned definitive bond order. We are forbidding the C2 triple bond
becuase we do not have good thermo for `Ctc` (C u0 p0 c+1 {1,T}) atomtype
""",
)

entry(
    label="strained",
    group=
"""
1  C u0 p0 c0 {2,[S,D,B,T]} {12,[S,D,B,T]}
2  C u0 p0 c0 {1,[S,D,B,T]} {3,[S,D,B,T]} {7,[S,D,B,T]}
3  C u0 p0 c0 {2,[S,D,B,T]} {4,[S,D,B,T]}
4  C u0 p0 c0 {3,[S,D,B,T]} {5,[S,D,B,T]}
5  C u0 p0 c0 {4,[S,D,B,T]} {6,[S,D,B,T]} {12,[S,D,B,T]}
6  C u0 p0 c0 {5,[S,D,B,T]} {7,[S,D,B,T]} {8,[S,D,B,T]}
7  C u[0,1] p0 c0 {2,[S,D,B,T]} {6,[S,D,B,T]}
8  C u0 p0 c0 {6,[S,D,B,T]} {9,[S,D,B,T]}
9 C u0 p0 c0 {8,[S,D,B,T]} {10,[S,D,B,T]}
10 C u0 p0 c0 {9,[S,D,B,T]} {11,[S,D,B,T]}
11 C u0 p0 c0 {10,[S,D,B,T]} {12,[S,D,B,T]}
12 N u0 p1 c0 {1,[S,D,B,T]} {5,[S,D,B,T]} {11,[S,D,B,T]}
""",
    shortDesc=u"""""",
    longDesc=
u"""
Strained structure, originally derived from: CN(CCC1C2C=CC3=C([CH]2)CCC2C(N13)=CC=CC=2)C
""",
)

entry(
    label="cCCOO",
    group=
"""
1 C u0 p0 c0 {2,S} {4,S}
2 C u0 p0 c0 {1,S} {3,S} 
3 O u0 p2 c0 {2,S} {4,S}
4 O u0 p2 c0 {1,S} {3,S}
""",
    shortDesc=u"""""",
    longDesc=
u"""
Strained structure, originally derived from: CN(C)CCCN1C2=CC=C[CH]C23OOC3CC3=CC=CC=C31
""",
)

entry(
    label="CC(=C=NO[O])C=O",
    species=
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,D} {7,S}
3  C u0 p0 c0 {2,D} {4,D}
4  N u0 p1 c0 {3,D} {5,S}
5  O u0 p2 c0 {4,S} {6,S}
6  O u1 p2 c0 {5,S}
7  C u0 p0 c0 {2,S} {8,D} {12,S}
8  O u0 p2 c0 {7,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {7,S}
""",
    shortDesc=u"""""",
    longDesc=
u"""
Did not converge at CBS-QB3
""",
)

entry(
    label="[O]ON=C=C(CO)C",
    species=
"""
multiplicity 2
1  O u1 p2 c0 {2,S}
2  O u0 p2 c0 {1,S} {3,S}
3  N u0 p1 c0 {2,S} {4,D}
4  C u0 p0 c0 {3,D} {5,D}
5  C u0 p0 c0 {4,D} {6,S} {8,S}
6  C u0 p0 c0 {5,S} {7,S} {9,S} {10,S}
7  O u0 p2 c0 {6,S} {11,S}
8  C u0 p0 c0 {5,S} {12,S} {13,S} {14,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {8,S}
""",
    shortDesc=u"""""",
    longDesc=
u"""
Did not converge at CBS-QB3
""",
)

entry(
    label="CC(=O)[CH]OON",
    species=
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  C u1 p0 c0 {2,S} {5,S} {6,S}
5  H u0 p0 c0 {4,S}
6  O u0 p2 c0 {4,S} {7,S}
7  O u0 p2 c0 {6,S} {8,S}
8  N u0 p1 c0 {7,S} {12,S} {13,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {8,S}
""",
    shortDesc=u"""""",
    longDesc=
u"""
Conformers did not converge at apfd/def2tzvp
""",
)

entry(
    label="C[C](C#N)ON=O",
    species=
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u1 p0 c0 {1,S} {3,S} {5,S}
3  C u0 p0 c0 {2,S} {4,T}
4  N u0 p1 c0 {3,T}
5  O u0 p2 c0 {2,S} {6,S}
6  N u0 p1 c0 {5,S} {7,D}
7  O u0 p2 c0 {6,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
""",
    shortDesc=u"""""",
    longDesc=
u"""
Did not converge at CBS-QB3
""",
)

entry(
    label="[O]ON=C=C",
    species=
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 N u0 p1 c0 {2,S} {4,D}
4 C u0 p0 c0 {3,D} {5,D}
5 C u0 p0 c0 {4,D} {6,S} {7,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {5,S}
""",
    shortDesc=u"""""",
    longDesc=
u"""
Did not converge at CBS-QB3
""",
)

entry(
    label="C(C#N)OO[C]=O",
    species=
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
2 C u0 p0 c0 {1,S} {3,T}
3 N u0 p1 c0 {2,T}
4 O u0 p2 c0 {1,S} {5,S}
5 O u0 p2 c0 {4,S} {6,S}
6 C u1 p0 c0 {5,S} {7,D}
7 O u0 p2 c0 {6,D}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {1,S}
""",
    shortDesc=u"""""",
    longDesc=
u"""
Conformers did not converge at apfd/def2tzvp
""",
)

entry(
    label="[O-][NH2+]O[O]",
    species=
"""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {3,S} {4,S} {5,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 O u0 p2 c0 {2,S} {6,S}
6 O u1 p2 c0 {5,S}
""",
    shortDesc=u"""""",
    longDesc=
u"""
Did not converge at CBS-QB3
""",
)

entry(
    label="CC(=COO[NH])O",
    species=
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {4,S} {12,S}
4  O u0 p2 c0 {3,S} {5,S}
5  O u0 p2 c0 {4,S} {6,S}
6  N u1 p1 c0 {5,S} {7,S}
7  H u0 p0 c0 {6,S}
8  O u0 p2 c0 {2,S} {13,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {8,S}
""",
    shortDesc=u"""""",
    longDesc=
u"""
Did not converge at CBS-QB3
""",
)

entry(
    label="[N]=CNOOC=C(O)C",
    species=
"""
multiplicity 2
1  N u1 p1 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {10,S}
3  N u0 p1 c0 {2,S} {4,S} {11,S}
4  O u0 p2 c0 {3,S} {5,S}
5  O u0 p2 c0 {4,S} {6,S}
6  C u0 p0 c0 {5,S} {7,D} {12,S}
7  C u0 p0 c0 {6,D} {8,S} {9,S}
8  O u0 p2 c0 {7,S} {13,S}
9  C u0 p0 c0 {7,S} {14,S} {15,S} {16,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {9,S}
""",
    shortDesc=u"""""",
    longDesc=
u"""
Did not converge at CBS-QB3
""",
)

entry(
    label="O=[C]CC(=O)O",
    species=
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u1 p0 c0 {1,D} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
4 C u0 p0 c0 {3,S} {5,D} {6,S}
5 O u0 p2 c0 {4,D}
6 O u0 p2 c0 {4,S} {9,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {6,S}
""",
    shortDesc=u"""""",
    longDesc=
u"""
Did not converge at CBS-QB3
""",
)

entry(
    label="CC(=[C]OON)O",
    species=
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,D} {7,S}
3  C u1 p0 c0 {2,D} {4,S}
4  O u0 p2 c0 {3,S} {5,S}
5  O u0 p2 c0 {4,S} {6,S}
6  N u0 p1 c0 {5,S} {11,S} {12,S}
7  O u0 p2 c0 {2,S} {13,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
""",
    shortDesc=u"""""",
    longDesc=
u"""
Did not converge at CBS-QB3
""",
)

entry(
    label="OC(=O)[CH]C#N",
    species=
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {8,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 O u0 p2 c0 {2,D}
4 C u1 p0 c0 {2,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 C u0 p0 c0 {4,S} {7,T}
7 N u0 p1 c0 {6,T}
8 H u0 p0 c0 {1,S}
""",
    shortDesc=u"""""",
    longDesc=
u"""
Did not converge at CBS-QB3
""",
)

entry(
    label="O=C=[C]C#N",
    species=
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,D}
3 C u1 p0 c0 {2,D} {4,S}
4 C u0 p0 c0 {3,S} {5,T}
5 N u0 p1 c0 {4,T}
""",
    shortDesc=u"""""",
    longDesc=
u"""
Did not converge at CBS-QB3
""",
)

entry(
    label="O=C=NC(=C(O)O)C#N",
    species=
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,D}
3  N u0 p1 c0 {2,D} {4,S}
4  C u0 p0 c0 {3,S} {5,D} {8,S}
5  C u0 p0 c0 {4,D} {6,S} {7,S}
6  O u0 p2 c0 {5,S} {10,S}
7  O u0 p2 c0 {5,S} {11,S}
8  C u0 p0 c0 {4,S} {9,T}
9  N u0 p1 c0 {8,T}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {7,S}
""",
    shortDesc=u"""""",
    longDesc=
u"""
Did not converge at CBS-QB3
""",
)

entry(
    label="OC(=O)C(=[N])C#N",
    species=
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {8,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 O u0 p2 c0 {2,D}
4 C u0 p0 c0 {2,S} {5,D} {6,S}
5 N u1 p1 c0 {4,D}
6 C u0 p0 c0 {4,S} {7,T}
7 N u0 p1 c0 {6,T}
8 H u0 p0 c0 {1,S}
""",
    shortDesc=u"""""",
    longDesc=
u"""
Did not converge at CBS-QB3
""",
)

entry(
    label="NC(=O)N=CC(=O)[O]",
    species=
"""
multiplicity 2
1  N u0 p1 c0 {2,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  N u0 p1 c0 {2,S} {5,D}
5  C u0 p0 c0 {4,D} {6,S} {11,S}
6  C u0 p0 c0 {5,S} {7,D} {8,S}
7  O u0 p2 c0 {6,D}
8  O u1 p2 c0 {6,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {5,S}
""",
    shortDesc=u"""""",
    longDesc=
u"""
Did not converge at CBS-QB3
""",
)

entry(
    label="N=C=C(C(=O)[O])C#N",
    species=
"""
multiplicity 2
1 N u0 p1 c0 {2,D} {9,S}
2 C u0 p0 c0 {1,D} {3,D}
3 C u0 p0 c0 {2,D} {4,S} {7,S}
4 C u0 p0 c0 {3,S} {5,D} {6,S}
5 O u0 p2 c0 {4,D}
6 O u1 p2 c0 {4,S}
7 C u0 p0 c0 {3,S} {8,T}
8 N u0 p1 c0 {7,T}
9 H u0 p0 c0 {1,S}
""",
    shortDesc=u"""""",
    longDesc=
u"""
Did not converge at CBS-QB3
""",
)

entry(
    label="N#CC(C(=O)[O])N=C=O",
    species=
"""
multiplicity 2
1  N u0 p1 c0 {2,T}
2  C u0 p0 c0 {1,T} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {7,S} {10,S}
4  C u0 p0 c0 {3,S} {5,D} {6,S}
5  O u0 p2 c0 {4,D}
6  O u1 p2 c0 {4,S}
7  N u0 p1 c0 {3,S} {8,D}
8  C u0 p0 c0 {7,D} {9,D}
9  O u0 p2 c0 {8,D}
10 H u0 p0 c0 {3,S}
""",
    shortDesc=u"""""",
    longDesc=
u"""
Did not converge at CBS-QB3
""",
)

entry(
    label="N#CC(C(=O)O)(C#N)[O]",
    species=
"""
multiplicity 2
1  N u0 p1 c0 {2,T}
2  C u0 p0 c0 {1,T} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {7,S} {9,S}
4  C u0 p0 c0 {3,S} {5,D} {6,S}
5  O u0 p2 c0 {4,D}
6  O u0 p2 c0 {4,S} {10,S}
7  C u0 p0 c0 {3,S} {8,T}
8  N u0 p1 c0 {7,T}
9  O u1 p2 c0 {3,S}
10 H u0 p0 c0 {6,S}
""",
    shortDesc=u"""""",
    longDesc=
u"""
Did not converge at CBS-QB3
converges into a TS, very interesting
""",
)

entry(
    label="N#CC(C(=O)[O])(C#N)O",
    species=
"""
multiplicity 2
1  N u0 p1 c0 {2,T}
2  C u0 p0 c0 {1,T} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {7,S} {9,S}
4  C u0 p0 c0 {3,S} {5,D} {6,S}
5  O u0 p2 c0 {4,D}
6  O u1 p2 c0 {4,S}
7  C u0 p0 c0 {3,S} {8,T}
8  N u0 p1 c0 {7,T}
9  O u0 p2 c0 {3,S} {10,S}
10 H u0 p0 c0 {9,S}
""",
    shortDesc=u"""""",
    longDesc=
u"""
Did not converge at CBS-QB3
""",
)

entry(
    label="O=NC=C(C(=O)[O])C#N",
    species=
"""
multiplicity 2
1  O u0 p2 c0 {2,D}
2  N u0 p1 c0 {1,D} {3,S}
3  C u0 p0 c0 {2,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {5,S} {8,S}
5  C u0 p0 c0 {4,S} {6,D} {7,S}
6  O u0 p2 c0 {5,D}
7  O u1 p2 c0 {5,S}
8  C u0 p0 c0 {4,S} {9,T}
9  N u0 p1 c0 {8,T}
10 H u0 p0 c0 {3,S}
""",
    shortDesc=u"""""",
    longDesc=
u"""
Did not converge at CBS-QB3
""",
)

entry(
    label="[O]C(=O)C(=C)C#N",
    species=
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 O u0 p2 c0 {2,D}
4 C u0 p0 c0 {2,S} {5,D} {6,S}
5 C u0 p0 c0 {4,D} {8,S} {9,S}
6 C u0 p0 c0 {4,S} {7,T}
7 N u0 p1 c0 {6,T}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {5,S}
""",
    shortDesc=u"""""",
    longDesc=
u"""
Did not converge at CBS-QB3
""",
)

entry(
    label="[CH2]C(=COON)O",
    species=
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,D} {9,S}
5  C u0 p0 c0 {4,D} {6,S} {10,S}
6  O u0 p2 c0 {5,S} {7,S}
7  O u0 p2 c0 {6,S} {8,S}
8  N u0 p1 c0 {7,S} {11,S} {12,S}
9  O u0 p2 c0 {4,S} {13,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {8,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {9,S}
""",
    shortDesc=u"""""",
    longDesc=
u"""
Did not converge at CBS-QB3
Interesting and unexpected
""",
)

entry(
    label="CC(=O)C(C#N)OO[NH]",
    species=
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  C u0 p0 c0 {2,S} {5,S} {7,S} {14,S}
5  C u0 p0 c0 {4,S} {6,T}
6  N u0 p1 c0 {5,T}
7  O u0 p2 c0 {4,S} {8,S}
8  O u0 p2 c0 {7,S} {9,S}
9  N u1 p1 c0 {8,S} {10,S}
10 H u0 p0 c0 {9,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {4,S}
""",
    shortDesc=u"""""",
    longDesc=
u"""
Did not converge at CBS-QB3
Interesting and unexpected, broke into NO
""",
)

entry(
    label="N#CNOO[CH]C(=O)C",
    species=
"""
multiplicity 2
1  N u0 p1 c0 {2,T}
2  C u0 p0 c0 {1,T} {3,S}
3  N u0 p1 c0 {2,S} {4,S} {11,S}
4  O u0 p2 c0 {3,S} {5,S}
5  O u0 p2 c0 {4,S} {6,S}
6  C u1 p0 c0 {5,S} {7,S} {8,S}
7  H u0 p0 c0 {6,S}
8  C u0 p0 c0 {6,S} {9,D} {10,S}
9  O u0 p2 c0 {8,D}
10 C u0 p0 c0 {8,S} {12,S} {13,S} {14,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {10,S}
13 H u0 p0 c0 {10,S}
14 H u0 p0 c0 {10,S}
""",
    shortDesc=u"""""",
    longDesc=
u"""
Did not converge at CBS-QB3
Interesting, a radical next to O-O broke it into two fragments
""",
)

entry(
    label="[O]ON=C=C(ON)C",
    species=
"""
multiplicity 2
1  O u1 p2 c0 {2,S}
2  O u0 p2 c0 {1,S} {3,S}
3  N u0 p1 c0 {2,S} {4,D}
4  C u0 p0 c0 {3,D} {5,D}
5  C u0 p0 c0 {4,D} {6,S} {8,S}
6  O u0 p2 c0 {5,S} {7,S}
7  N u0 p1 c0 {6,S} {9,S} {10,S}
8  C u0 p0 c0 {5,S} {11,S} {12,S} {13,S}
9  H u0 p0 c0 {7,S}
10 H u0 p0 c0 {7,S}
11 H u0 p0 c0 {8,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {8,S}
""",
    shortDesc=u"""""",
    longDesc=
u"""
Did not converge at CBS-QB3
breaks into O2
""",
)

entry(
    label="NC(=O)N=CC(=O)O",
    species=
"""
1  N u0 p1 c0 {2,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  N u0 p1 c0 {2,S} {5,D}
5  C u0 p0 c0 {4,D} {6,S} {11,S}
6  C u0 p0 c0 {5,S} {7,D} {8,S}
7  O u0 p2 c0 {6,D}
8  O u0 p2 c0 {6,S} {12,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {8,S}
""",
    shortDesc=u"""""",
    longDesc=
u"""
physical, but problematic at low [MeOH]
""",
)

entry(
    label="NC(=O)N=[C]C(=O)O",
    species=
"""
multiplicity 2
1  N u0 p1 c0 {2,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  N u0 p1 c0 {2,S} {5,D}
5  C u1 p0 c0 {4,D} {6,S}
6  C u0 p0 c0 {5,S} {7,D} {8,S}
7  O u0 p2 c0 {6,D}
8  O u0 p2 c0 {6,S} {11,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {8,S}
""",
    shortDesc=u"""""",
    longDesc=
u"""
physical, but problematic at low [MeOH]
""",
)

entry(
    label="NC(=O)N=CC(=O)O",
    species=
"""
1  N u0 p1 c0 {2,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  N u0 p1 c0 {2,S} {5,D}
5  C u0 p0 c0 {4,D} {6,S} {11,S}
6  C u0 p0 c0 {5,S} {7,D} {8,S}
7  O u0 p2 c0 {6,D}
8  O u0 p2 c0 {6,S} {12,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {8,S}
""",
    shortDesc=u"""""",
    longDesc=
u"""
physical, but problematic at low [MeOH]
""",
)
