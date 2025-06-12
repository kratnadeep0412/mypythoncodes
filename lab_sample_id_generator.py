# File name: lab_sample_id_generator.py
sample_id = input("Enter the Lab Sample ID (e.g., LAB2025-017): ")
n = int(input("Enter how many next IDs you want to generate: "))
# Split the input into prefix and number
prefix, number = sample_id.split('-')
number = int(number)
# Generate the next n IDs
generated_ids = []
for i in range(1, n + 1):
    new_id = f"{prefix}-{str(number + i).zfill(3)}"
    generated_ids.append(new_id)
# Print the generated IDs
print("Generated IDs:", generated_ids)
