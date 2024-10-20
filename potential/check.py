import h5py
import numpy as np

# Open the vaspout.h5 file
with h5py.File("vaspout.h5", "r") as hdf_file:
    # Extract different components of the potential
    potential_total = np.array(hdf_file["results/potential/total"])
    potential_grid = np.array(hdf_file["results/potential/grid"])
    potential_hartree = np.array(hdf_file["results/potential/hartree"])
    potential_ionic = np.array(hdf_file["results/potential/ionic"])

# You can now inspect or process the potential data
print("Total Potential:", potential_total)
print("Grid Data:", potential_grid)
print("Hartree Potential:", potential_hartree)
print("Ionic Potential:", potential_ionic)

