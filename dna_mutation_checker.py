# dna_mutation_checker.py
# Take input DNA sequences from the user
seq1 = input("Enter the First Sequence: ")
seq2 = input("Enter the Second Sequence: ")
# Check if both sequences are of the same length
if len(seq1) != len(seq2):
    print("Error: Both sequences must be of the same length.")
else:
    mutation_indices = []
    # Loop through both sequences to find mutations
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            mutation_indices.append(i)
    # Print the mutation positions
    if mutation_indices:
        print("Mutations found at positions (0-indexed):", mutation_indices)
    else:
        print("No mutations found. The sequences are identical.")
