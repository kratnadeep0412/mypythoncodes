# File Name: gene_expression_classifier.py
# Input: space-separated gene expression values
values_string = input("Enter the gene expression values: ")
# Convert input string to a list of floats
gene_expression = [float(value) for value in values_string.split()]
# Classification storage
output = []
# Classification logic
for data in gene_expression:
    if data < 5:
        output.append("low")
    elif 5 <= data <= 15:
        output.append("normal")
    else:
        output.append("overexpressed")
# Output the classification
print("Gene expression classification:", output)
