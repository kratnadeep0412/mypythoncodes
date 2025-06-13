#palindrome using functions
def Palindrome_DNA(sequence):
    # Create empty string to store reverse complement
    reverse_complement = ''
    # Create the complement manually using if conditions
    for base in sequence[::-1]:  # Reverse the sequence
        if base == 'A':
            reverse_complement += 'T'
        elif base == 'T':
            reverse_complement += 'A'
        elif base == 'C':
            reverse_complement += 'G'
        elif base == 'G':
            reverse_complement += 'C'
    # Check if original and reverse complement are same
    if sequence == reverse_complement:
        print(f"Given DNA Sequence {sequence} is a palindrome")
    else:
        print(f"Given DNA Sequence {sequence} is not a palindrome")
# Example input
dna_seq = input("Enter the DNA Sequence: ")
Palindrome_DNA(dna_seq)
