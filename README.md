# VASP-Inputs
store and exchange vasp inputs

# VASP-Outputs

## ACF.dat 

Bader Analysis Output File, contains the number of charges associated with the atom in the fourth column. Depending on which POTCAR is used, this means an excess or deficit of charge, i.e. a net charge. In this study 9 electrons are explicitly calculated for Co and 6 for oxygen. I assume it is 4 for carbon and 1 for hydrogen.

# Problem

The combined system has too high (14 eV) adsorption energy.  Even tests with a considerable gap between the surface and the molecule show large pseudo adsorption energies (pseudo because there is no adsorption). Pseudo Adsorption energies are 1eV when the molecule is parallel to the surface and 4 eV when it is orthogonal to the surface. 

## Hypotheses 

### 1 Charge Transfer Hypothesis

It may be that in the combined system it is energetically more favorable for an additional electron to settle on the molecule. This is probably an example of a typical DFT delocalization error (see Lit.). Whatever the cause, it can be easily checked by looking at the charge deficit.


#### Test 1.a
The surface-parallel configuration has 0.002599 electrons less, than the neutral molecule (positive charge). 
The upright configuration has 0.001943 more electrons than the neutral molecule (negative charge). 


#### Conclusion of Test 1.a
The molecule is weakly positively ionised in parallel configuration and weekly negative ionised in orthogonal configuration. 
Both configurations yield negative (binding ) psudo adsorptiokn energies. However the molecule can only either stabilize charge better or worse than the substrate, not both.
If charge transfer was the cause of the too large pseudo adsorption energies, the molecule would need to have the same sign in its ionisation in both cases. 


### 2 Substrate Capacitor Hypothesis

If the substrate has asymmetric charge distribution, the vacuum behaves like the inside of a capacitor. The polarisation of the electron density in the molecule will lead to lower overall energy in the system. 

#### Test 2.a  Vacuum potential

If the substrate  makes a capacitor of the vacuum, then this can be seen in the hartree potential, as a slope in the vacuum where there should be a flat line.  
In deed, a massive dipole field needs to be compenasted of 0.5 a.u.. The surface hatree potential of the substrate is much lower than the potential of the 
"bulk" end (the end of the cell, also pointed towards a vacuum, but atoms are fixed).

![Colors show Charges, the acis group behaves as expected](https://github.com/JannisErhard/VASP-Inputs/blob/main/Images/potential.jpeg.png?raw=true)

An Image of the Vacuu  Potential

#### Test 2.b  Partial Charges in Molecule

For the upright molecule one would find partial charges, which are asummetrically distributed.
![Colors show Charges, the acis group behaves as expected](https://github.com/JannisErhard/VASP-Inputs/blob/main/Images/upright_molecule.jpeg?raw=true)
But findings dont back this up.

### 3 The vacuum is too small 

If the vacuum is too small, the molecule is always absorbed. 

#### 3.a
To test if the vacuum is converged a series of calculations with increasing vacuum height is executed.

| vac | substrate     | molecule      | combined      | Adsorption E        |
|-----|---------------|---------------|---------------|---------------------|
| 15  | -629.80335865 | -             | -825.24892376 | -                   |
| 25  | -629.80155847 | -190.61951233 | -             | -                   |
| 30  | -629.79997894 | -190.61917075 | -831.83072619 | -11.411576500000024 |

energies and vacuum size. the table is imcomplete but comparing the firstand the last row for combined, one can see that 15 clearly is not converged. Wether 30 is converged is unclear.It would make sense to add calculations for 20 and fill the gaps in the table.
