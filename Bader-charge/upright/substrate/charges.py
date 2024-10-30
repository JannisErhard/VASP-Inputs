# Define the number of valence electrons for each element (for Co and O here)
valence_electrons = {
    "Co" : 9,
    "O" : 6
}

# Read the ACF.dat file
with open('ACF.dat', 'r') as file:
    lines = file.readlines()

# Parse the ACF.dat file, skipping the header and footer
charges = []
for line in lines[2:]:  # Skip header lines
    data = line.split()
    if len(data) < 5:  # Skip lines without enough columns
        continue
    charge = float(data[4])  # Extract the charge from the 5th column
    charges.append(charge)

# Calculate the Bader charge for each atom (assuming a list of atom types)
atom_types =["Co"] * 54 + ["O"] * 54  # Modify this as per your system

bader_charges = []
for i, atom_type in enumerate(atom_types):
    bader_charge = valence_electrons[atom_type] - charges[i]
    bader_charges.append(bader_charge)

# Print the results
for i, charge in enumerate(bader_charges):
    print(f"Atom {i+1} ({atom_types[i]}): Bader Charge = {charge:.4f}")

