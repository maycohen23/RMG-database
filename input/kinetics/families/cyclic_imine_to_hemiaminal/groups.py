#!/usr/bin/env python
# encoding: utf-8

name = "cyclic_imine_to_hemiaminal/groups"
shortDesc = u""
longDesc = u"""
This family describes solution-phase hydrolysis of amine groups in a cyclic structure:
C=NR + H2O <=> H + RCN(OH)R'
atom labels:
RC[*1]=N[*2]R' + H[*4]O[*3]H <=> H[*4] + RC[*1]N[*2](OH[*3])R'
"""

template(reactants=["CdN", "H2O"], products=["CdONH2"], ownReverse=False)

reverse = "condensation_to_imine"

reversible = True

only_forward = True

recipe(actions=[
    ['CHANGE_BOND', '*1', -1, '*2'],
    ['BREAK_BOND', '*3', 1, '*4'],
    ['FORM_BOND', '*1', 1, '*3'],
    ['GAIN_RADICAL', '*4', 1],

])

entry(
    index=0,
    label="CdN",
    group="OR{CdN3, CdN4, CdN5, CdN6, CdN7, CdN8}",
    kinetics=None,
)

entry(
    index=1,
    label="CdN3",
    group=
"""
1 *1 C u0 p0 c0 {2,D} {3,[S,D]}
2 *2 N u0 p1 c0 {1,D} {3,[S]} 
3    R ux px cx {2,[S]} {1,[S,D]}
""",
    kinetics=None,
)

entry(
    index=2,
    label="CdN4",
    group=
"""
1 *1 C u0 p0 c0 {2,D} {4,[S,D]}
2 *2 N u0 p1 c0 {1,D} {3,[S]} 
3    R ux px cx {2,[S]} {4,[S,D]}
4    R ux px cx {1,[S,D]} {3,[S,D]}
""",
    kinetics=None,
)

entry(
    index=3,
    label="CdN5",
    group=
"""
1 *1 C u0 p0 c0 {2,D} {5,[S,D]}
2 *2 N u0 p1 c0 {1,D} {3,[S]} 
3    R ux px cx {2,[S]} {4,[S,D,T]}
4    R ux px cx {3,[S,D,T]} {5,[S,D,T]}
5    R ux px cx {1,[S,D]} {4,[S,D,T]}
""",
    kinetics=None,
)

entry(
    index=4,
    label="CdN6",
    group=
"""
1 *1 C u0 p0 c0 {2,D} {6,[S,D]}
2 *2 N u0 p1 c0 {1,D} {3,[S]} 
3    R ux px cx {2,[S]} {4,[S,D,T]}
4    R ux px cx {3,[S,D,T]} {5,[S,D,T]}
5    R ux px cx {4,[S,D,T]} {6,[S,D,T]}
6    R ux px cx {1,[S,D]} {5,[S,D,T]}
""",
    kinetics=None,
)

entry(
    index=5,
    label="CdN7",
    group=
"""
1 *1 C u0 p0 c0 {2,D} {7,[S,D]}
2 *2 N u0 p1 c0 {1,D} {3,S} 
3    R ux px cx {2,S} {4,[S,D,T]}
4    R ux px cx {3,[S,D,T]} {5,[S,D,T]}
5    R ux px cx {4,[S,D,T]} {6,[S,D,T]}
6    R ux px cx {5,[S,D,T]} {7,[S,D,T]}
7    R ux px cx {6,[S,D,T]} {1,[S,D]}

""",
    kinetics=None,
)

entry(
    index=6,
    label="CdN8",
    group=
"""
1 *1 C u0 p0 c0 {2,D} {8,[S,D]}
2 *2 N u0 p1 c0 {1,D} {3,S} 
3    R ux px cx {2,S} {4,[S,D,T]}
4    R ux px cx {3,[S,D,T]} {5,[S,D,T]}
5    R ux px cx {4,[S,D,T]} {6,[S,D,T]}
6    R ux px cx {5,[S,D,T]} {7,[S,D,T]}
7    R ux px cx {6,[S,D,T]} {8,[S,D,T]}
8    R ux px cx {7,[S,D,T]} {1,[S,D]}
""",
    kinetics=None,
)

entry(
    index=7,
    label="H2O",
    group=
"""
1 *3 O u0 p2 c0 {2,S} {3,S}
2 *4 H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    kinetics=None,
)


entry(
    index=8,
    label="Diazepam",
    group=
"""
1  C  u0 p0 c0 {2,S} {6,D} {21,S}
2  C  u0 p0 c0 {1,S} {3,D} {22,S}
3  C  u0 p0 c0 {2,D} {4,S} {23,S}
4  C  u0 p0 c0 {3,S} {5,D} {24,S}
5  C  u0 p0 c0 {4,D} {6,S} {25,S}
6  C  u0 p0 c0 {1,D} {5,S} {7,S}
7  *1 C  u0 p0 c0 {6,S} {8,D} {20,S}
8  *2 N  u0 p1 c0 {7,D} {9,S}
9  C  u0 p0 c0 {8,S} {10,S} {26,S} {27,S}
10 C  u0 p0 c0 {9,S} {11,D} {12,S}
11 O  u0 p2 c0 {10,D}
12 N  u0 p1 c0 {10,S} {13,S} {14,S}
13 C  u0 p0 c0 {12,S} {28,S} {29,S} {30,S}
14 C  u0 p0 c0 {12,S} {15,S} {20,D}
15 C  u0 p0 c0 {14,S} {16,D} {31,S}
16 C  u0 p0 c0 {15,D} {17,S} {32,S}
17 C  u0 p0 c0 {16,S} {18,S} {19,D}
18 Cl u0 p3 c0 {17,S}
19 C  u0 p0 c0 {17,D} {20,S} {33,S}
20 C  u0 p0 c0 {7,S} {14,D} {19,S}
21 H  u0 p0 c0 {1,S}
22 H  u0 p0 c0 {2,S}
23 H  u0 p0 c0 {3,S}
24 H  u0 p0 c0 {4,S}
25 H  u0 p0 c0 {5,S}
26 H  u0 p0 c0 {9,S}
27 H  u0 p0 c0 {9,S}
28 H  u0 p0 c0 {13,S}
29 H  u0 p0 c0 {13,S}
30 H  u0 p0 c0 {13,S}
31 H  u0 p0 c0 {15,S}
32 H  u0 p0 c0 {16,S}
33 H  u0 p0 c0 {19,S}

""",
   kinetics=None,
)
   

tree(
"""
L1: CdN
  L2: CdN3
  L2: CdN4
  L2: CdN5
  L2: CdN6
  L2: CdN7
   L3: Diazepam
  L2: CdN8
L1: H2O
"""
)
