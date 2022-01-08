#!/usr/bin/env python
# encoding: utf-8

name = "imine_to_hydroxylamine/groups"
shortDesc = u""
longDesc = u"""
This family describes solution-phase hydrolysis of amine groups:
R=NR' + H2O <=> H + RN(OH)R'
atom labels:
R[*1]=N[*2]R' + H[*3]O[*4]H <=> H[*4] + R[*1]N[*2](OH[*4])R'
"""

template(reactants=["CdN", "H2O"], products=["CdNO", "H"], ownReverse=False)

reverse = "hydroxylamine_to_imine"

reversible = True

only_forward = True

recipe(actions=[
    ['CHANGE_BOND', '*1', -1, '*2'],
    ['BREAK_BOND', '*3', 1, '*4'],
    ['FORM_BOND', '*1', 1, '*4'],

])

entry(
    index=0,
    label="CdN",
    group=
"""
1 *1 R ux px cx {2,D} 
2 *2 N u0 p1 c0 {1,D} {3,S}
3    R ux px cx {2,S}
""",
    kinetics=None,
)

entry(
    index=1,
    label="H2O",
    group=
"""
1 *3 O u0 p2 c0 {2,S} {3,S}
2 *4 H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    kinetics=None,
)

tree(
"""
L1: CdN
L1: H2O
"""
)