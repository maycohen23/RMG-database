#!/usr/bin/env python
# encoding: utf-8

name = "Oxidative_degradation_ethers/groups"
shortDesc = u""
longDesc = u"""
This family describes solution-phase oxidative degradation of ethers groups:
RCOCR' + *OO* <=> RCOC(OOH)R'
atom labels:
RCO[*1]_(H(*2)H)CR' + OO[*3] <=> RCOC[*1](O[*3]OH[*2])R'
"""

template(reactants=["Ether", "o2_radical"], products=["Mid"], ownReverse=False)

reverse = "reduction_to_ethar"

reversible = True

only_forward = True

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*2'],
    ['FORM_BOND', '*1', 1, '*3'],
    ['FORM_BOND', '*2', 1, '*3'],
])

entry(
    index=0,
    label="Ether",
    group=
"""
1     R ux px cx {2,S}
2     C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3     O u0 p2 c0 {2,S} {4,S}
4  *1 C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
5     R ux px cx {4,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8  *2 H u0 p0 c0 {4,S}
9     H u0 p0 c0 {4,S}

""",
    kinetics=None,
)

entry(
    index=1,
    label="o2_radical",
    group=
"""
1 *3 O u0 p2 c0 {2,D} 
2    O u0 p2 c0 {1,D} 


""",
    kinetics=None,
)

tree(
"""
L1: Ether

L1: o2_radical
"""
)
