#!/usr/bin/env python
# encoding: utf-8

name = "nitroso_to_oxime/groups"
shortDesc = u""
longDesc = u"""
This family describes solution-phase hydrolysis of amine groups:
N(=O)RH <=> N(OH)=R
*ONLY HAPPEN WHEN R HAS AT LEAST ONE H*
atom labels:
N[*1](=O[*2])R[*3]H[*4] <=> N[*1](O[*2]H[*4])=R[*3]
"""

template(reactants=["nitroso"], products=["oxime"], ownReverse=False)

reverse = "NULL"

reversible = True

only_forward = True

recipe(actions=[
    ['CHANGE_BOND', '*1', -1, '*2'],
    ['BREAK_BOND', '*3', 1, '*4'],
    ['FORM_BOND', '*2', 1, '*4'],
    ['CHANGE_BOND', '*2', +1, '*3'],


])

entry(
    index=0,
    label="nitroso",
    group=
"""
1 *3 R ux px cx {2,S} {4,S} 
2 *1 N u0 p1 c0 {1,S} {3,D}
3 *2 O u0 p2 c0 {2,D}
4 *4 H u0 p0 c0 {1,S}

""",
    kinetics=None,
)


tree(
"""
L1: nitroso
"""
)