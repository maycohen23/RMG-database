#!/usr/bin/env python
# encoding: utf-8

name = "Surface/cathub/Ag-seed"
shortDesc = ""
longDesc = """
Training reactions removed using kinetics_library_to_training notebook
"""
autoGenerated=False
entry(
    index = 0,
    label = "X + X + N2 <=> NX + NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(7.59058,'eV/molecule'), T0=(1,'K')),
    shortDesc = """cathub_id:UmVhY3Rpb246NDMzMDY1""",
    longDesc = 
"""
equation : N2(g) + 2.0* -> 2.0N*
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangAchieving2021
reactionEnergy: 5.82204005215317 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ag",
    facet = "211",
)

entry(
    index = 1,
    label = "CH2CH2X <=> HX + CCH3X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(2.53029,'eV/molecule'), T0=(1,'K')),
    shortDesc = """cathub_id:UmVhY3Rpb246ODI2""",
    longDesc = 
"""
equation : CH2CH2* -> CCH3* + H*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 2.85434 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Ag",
    facet = "211",
)

entry(
    index = 2,
    label = "CH3X + X <=> HX + CH2X",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = MultiArrhenius(arrhenius=[SurfaceArrhenius(A=(3.43628e+16,'m^2/(mol*s)'), n=0, Ea=(2.39,'eV/molecule'), T0=(1,'K')), SurfaceArrhenius(A=(3.43628e+16,'m^2/(mol*s)'), n=0, Ea=(2.51142,'eV/molecule'), T0=(1,'K'))]),
    shortDesc = """cathub_id:UmVhY3Rpb246ODk3""",
    longDesc = 
"""
equation : CH3* -> CH2* + H*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 1.684 eV

equation : CH3* + * -> CH2* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: SchumannSelectivity2018
reactionEnergy: 2.11357453658 eV


A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH3] from Thermo library: DFT_QCI_thermo and S298=46.44 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ag",
    facet = "111",
)

entry(
    index = 3,
    label = "CH2CH3X + X + X <=> HX + CH2CH2X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.00714e+22,'m^4/(mol^2*s)'), n=0, Ea=(1.10063,'eV/molecule'), T0=(1,'K')),
    shortDesc = """cathub_id:UmVhY3Rpb246OTEx""",
    longDesc = 
"""
equation : CH2CH3* -> CH2CH2* + H*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 0.37292 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
A/=(2.483e-5 mol/m^2)^2 (Pt111 site density)
""",
    metal = "Ag",
    facet = "211",
)

entry(
    index = 4,
    label = "CH4 + X + X <=> HX + CH3X",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = MultiArrhenius(arrhenius=[SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(2.49,'eV/molecule'), T0=(1,'K')), SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(2.5497,'eV/molecule'), T0=(1,'K'))]),
    shortDesc = """cathub_id:UmVhY3Rpb246OTY1""",
    longDesc = 
"""
equation : CH4(g) -> CH3* + H*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 1.844 eV

equation : CH4(g) + 2.0* -> CH3* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: SchumannSelectivity2018
reactionEnergy: 1.990026617 eV


Could not determine reaction type estimating A = kb/298/h = 6.21e+12
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ag",
    facet = "111",
)

entry(
    index = 5,
    label = "OCHX <=> HX + COX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(0.48163,'eV/molecule'), T0=(1,'K')),
    shortDesc = """cathub_id:UmVhY3Rpb246OTgy""",
    longDesc = 
"""
equation : HCO* -> CO* + H*
dft_code : DACAPO
dftFunctional : RPBE
pubId: Studt et al submitted
reactionEnergy: -0.00057 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Ag",
    facet = "211",
)

entry(
    index = 6,
    label = "H3COX + X + X <=> HX + OCH2X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.00714e+22,'m^4/(mol^2*s)'), n=0, Ea=(1.18091,'eV/molecule'), T0=(1,'K')),
    shortDesc = """cathub_id:UmVhY3Rpb246MTAzMA==""",
    longDesc = 
"""
equation : H3CO* -> H2CO* + H*
dft_code : DACAPO
dftFunctional : RPBE
pubId: Studt et al submitted
reactionEnergy: 0.82238 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
A/=(2.483e-5 mol/m^2)^2 (Pt111 site density)
""",
    metal = "Ag",
    facet = "211",
)

entry(
    index = 7,
    label = "NO + X + X <=> NX + OX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(3.075,'eV/molecule'), T0=(1,'K')),
    shortDesc = """cathub_id:UmVhY3Rpb246MTM1MQ==""",
    longDesc = 
"""
equation : NO(g) -> N* + O*
dft_code : DACAPO
dftFunctional : RPBE
pubId: FalsigOn2014
reactionEnergy: 1.775 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ag",
    facet = "111",
)

entry(
    index = 8,
    label = "NOX + X <=> NX + OX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.8541e+16,'m^2/(mol*s)'), n=0, Ea=(3.12,'eV/molecule'), T0=(1,'K')),
    shortDesc = """cathub_id:UmVhY3Rpb246MTM1NA==""",
    longDesc = 
"""
equation : NO* -> N* + O*
dft_code : DACAPO
dftFunctional : RPBE
pubId: FalsigOn2014
reactionEnergy: 1.82 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [N]=O from Thermo library: primaryThermoLibrary and S298=49.02 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ag",
    facet = "111",
)

entry(
    index = 9,
    label = "CO + X + X <=> CX + OX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(5.133,'eV/molecule'), T0=(1,'K')),
    shortDesc = """cathub_id:UmVhY3Rpb246MTM2Mg==""",
    longDesc = 
"""
equation : CO(g) -> C* + O*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 4.223 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ag",
    facet = "211",
)

entry(
    index = 10,
    label = "COX + X <=> CX + OX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(7.83289e+16,'m^2/(mol*s)'), n=0, Ea=(5.2,'eV/molecule'), T0=(1,'K')),
    shortDesc = """cathub_id:UmVhY3Rpb246MTM2Mw==""",
    longDesc = 
"""
equation : CO* -> C* + O*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 4.29 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [C]=O from Thermo library: DFT_QCI_thermo + radical(CdCdJ2_triplet) and S298=55.33 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ag",
    facet = "211",
)

entry(
    index = 11,
    label = "H2O + X + X <=> HX + OHX",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = MultiArrhenius(arrhenius=[SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(1.783,'eV/molecule'), T0=(1,'K')), SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(1.73436,'eV/molecule'), T0=(1,'K'))]),
    shortDesc = """cathub_id:UmVhY3Rpb246MTQwNg==""",
    longDesc = 
"""
equation : H2O(g) -> OH* + H*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 0.914 eV

equation : H2O(g) + 2.0* -> OH* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: SchumannSelectivity2018
reactionEnergy: 1.12602915458 eV


Could not determine reaction type estimating A = kb/298/h = 6.21e+12
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ag",
    facet = "111",
)

entry(
    index = 12,
    label = "OCH2X <=> HX + CHOX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(1.81856,'eV/molecule'), T0=(1,'K')),
    shortDesc = """cathub_id:UmVhY3Rpb246ODI2ODM=""",
    longDesc = 
"""
equation : CH2O* + * -> CHO* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: SchumannSelectivity2018
reactionEnergy: 1.64162462806 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Ag",
    facet = "111",
)

entry(
    index = 13,
    label = "X + CH3CHOHX + X <=> HX + CH3CHOX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.00714e+22,'m^4/(mol^2*s)'), n=0, Ea=(0.822165,'eV/molecule'), T0=(1,'K')),
    shortDesc = """cathub_id:UmVhY3Rpb246ODI3MTE=""",
    longDesc = 
"""
equation : CH3CHOH* + * -> CH3CHO* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: SchumannSelectivity2018
reactionEnergy: -0.25837740727 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
A/=(2.483e-5 mol/m^2)^2 (Pt111 site density)
""",
    metal = "Ag",
    facet = "111",
)

entry(
    index = 14,
    label = "X + CHOHX + X <=> HX + OCHX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.00714e+22,'m^4/(mol^2*s)'), n=0, Ea=(0.637676,'eV/molecule'), T0=(1,'K')),
    shortDesc = """cathub_id:UmVhY3Rpb246ODI3Njk=""",
    longDesc = 
"""
equation : CHOH* + * -> HCO* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: SchumannSelectivity2018
reactionEnergy: 0.0842642035277 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
A/=(2.483e-5 mol/m^2)^2 (Pt111 site density)
""",
    metal = "Ag",
    facet = "111",
)

entry(
    index = 15,
    label = "X + CH3COX + X <=> HX + CH2COX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.00714e+22,'m^4/(mol^2*s)'), n=0, Ea=(1.51707,'eV/molecule'), T0=(1,'K')),
    shortDesc = """cathub_id:UmVhY3Rpb246ODI3ODc=""",
    longDesc = 
"""
equation : CH3CO* + * -> CH2CO* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: SchumannSelectivity2018
reactionEnergy: 0.77431662858 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
A/=(2.483e-5 mol/m^2)^2 (Pt111 site density)
""",
    metal = "Ag",
    facet = "111",
)

entry(
    index = 16,
    label = "CH3CHOX <=> HX + CH3COX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(1.8495,'eV/molecule'), T0=(1,'K')),
    shortDesc = """cathub_id:UmVhY3Rpb246ODI3OTk=""",
    longDesc = 
"""
equation : CH3CHO* + * -> CH3CO* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: SchumannSelectivity2018
reactionEnergy: 1.48840956396 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Ag",
    facet = "111",
)

entry(
    index = 17,
    label = "HX + OCH3X <=> OHX + CH3X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^2/(mol*s)'), n=0, Ea=(1.01192,'eV/molecule'), T0=(1,'K')),
    shortDesc = """cathub_id:UmVhY3Rpb246ODI4MDU=""",
    longDesc = 
"""
equation : CH3O* + H* -> CH3* + OH*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: SchumannSelectivity2018
reactionEnergy: 0.0348758117907 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ag",
    facet = "111",
)

entry(
    index = 18,
    label = "X + OCH3X + X <=> HX + OCH2X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.00714e+22,'m^4/(mol^2*s)'), n=0, Ea=(1.27158,'eV/molecule'), T0=(1,'K')),
    shortDesc = """cathub_id:UmVhY3Rpb246ODI4NDE=""",
    longDesc = 
"""
equation : CH3O* + * -> CH2O* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: SchumannSelectivity2018
reactionEnergy: 0.900758478936 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
A/=(2.483e-5 mol/m^2)^2 (Pt111 site density)
""",
    metal = "Ag",
    facet = "111",
)

entry(
    index = 19,
    label = "H2 + CH2CH2X <=> HX + CH2CH3X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'m^3/(mol*s)'), n=0, Ea=(1.31974,'eV/molecule'), T0=(1,'K')),
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4MTQx""",
    longDesc = 
"""
equation : CH2CH2* + H2(g) + * -> CH3CH2* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 0.34857859078329057 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Ag",
    facet = "111",
)

entry(
    index = 20,
    label = "X + CHCH3X + X <=> HX + CHCH2X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.00714e+22,'m^4/(mol^2*s)'), n=0, Ea=(2.04408,'eV/molecule'), T0=(1,'K')),
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4MTU0""",
    longDesc = 
"""
equation : CH3CH* + * -> CH2CH* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 0.3206982138217427 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
A/=(2.483e-5 mol/m^2)^2 (Pt111 site density)
""",
    metal = "Ag",
    facet = "111",
)

entry(
    index = 21,
    label = "X + CCH3X + X <=> HX + CCH2X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.00714e+22,'m^4/(mol^2*s)'), n=0, Ea=(1.65341,'eV/molecule'), T0=(1,'K')),
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4MTU3""",
    longDesc = 
"""
equation : CH3C* + * -> CH2C* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 0.428025834960863 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
A/=(2.483e-5 mol/m^2)^2 (Pt111 site density)
""",
    metal = "Ag",
    facet = "111",
)
