# Python Program: Calculate Molecular Weight of a Protein Sequence
#Dictionary of amino acids and their molecular weights
amino_acid_weights = {
    'A': 89.1,   # Alanine
    'B': 110.2,  # Keratin (Note: 'B' is not a standard amino acid code)
    'C': 121.2,  # Cysteine
    'D': 133.1,  # Aspartic acid
    'E': 147.1,  # Glutamic acid
    'F': 165.2,  # Phenylalanine
    'G': 75.1,   # Glycine
    'H': 155.2,  # Histidine
    'I': 131.2,  # Isoleucine
    'K': 146.2,  # Lysine
    'L': 131.2,  # Leucine
    'M': 149.2,  # Methionine
    'N': 132.1,  # Asparagine
    'P': 115.1,  # Proline
    'Q': 146.2,  # Glutamine
    'R': 174.2,  # Arginine
    'S': 105.1,  # Serine
    'T': 119.1,  # Threonine
    'V': 117.1,  # Valine
    'W': 204.2,  # Tryptophan
    'Y': 181.2   # Tyrosine
}

#Read protein sequence from the user
protein_sequence = input("Enter the protein sequence (use one-letter codes, e.g., ACDEFGHIK): ").upper()
#Initialize total weight
total_weight = 0
#Calculate molecular weight
for amino_acid in protein_sequence:
    if amino_acid in amino_acid_weights:
        total_weight += amino_acid_weights[amino_acid]
    else:
        print(f"Warning: '{amino_acid}' is not a valid amino acid code.")
# Step 5: Display total molecular weight
print(f"\nTotal Molecular Weight of the Protein = {total_weight:.2f} Da")
