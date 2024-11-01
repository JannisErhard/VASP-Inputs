# VASP-Inputs
store and exchange vasp inputs

# VASP-Outputs

## ACF.dat 

Bader Analysis Output fuile, contains number of chages associated with the atom in fourth column. Depending on which POTCAR is used, this means a charge excess or deficit, i..e a net charge. In this study 9 electrons of Co are explicitely calculated and 6 of oxygen. I presum it is 4 for Carbon and 1 for Hydrogen.

# Problem

The combined system has a too large (14 eV) adsorption energy.  Even tests with considerable gap between surface and molecule show large (4 eV) pseudo-adsorption energies (pseudo, because there is no adsorption). 

## Hypotheses 

### 1 Charge Transfer

It might be that in the combined system, it is energetically more fevaorable for an additional electron to settle on the molecule. Thisn is probably an example of typical DFT delocalisation error (check lit.). Whatever the cause, wethr it is or not is easily chechecked looking at the charge deficite. 

#### Test 1.a
The surface-parallel configuration has 0.002599 electrons less, than the neutral molecule (positive charge). 
The upright configuration has 0.001943 more electrons than the neutral molecule (negative charge). 

If the additional 


### 2 Capacitor 

If the substrace has asymmetric charge distribution, the vacuum behaves like a capacitor. The polarisation of the electron density in the molecule will lead to lower overall energy in the system. 

#### Test 2.a  Vacuum potential

If the substrate  makes a capacitor of the vacuum, then this can be seen in the hartree potential. 

 
