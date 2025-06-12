# Python Program: Dictionary Operations - Job Roles
# Initial JobRole dictionary
JobRole = {101: 'Front-End Developer', 102: 'Back-End Developer', 103: 'Full-Stack Developer'}
JobRole2 = {}
# Update dictionary: Change role for key 101
JobRole[101] = 'UI/UX Developer'
# Add new elements
JobRole[104] = 'Data Engineer'
JobRole[105] = 'Python Developer'
JobRole[106] = 'Data Analyst'
# Delete element: Remove the role with key 101 (UI/UX Developer)
JobRole.pop(101)
# Print dictionary after deletion
print("\nJobRole after removing key 101 (UI/UX Developer):")
print(JobRole)
# Delete element using del keyword: Remove the role with key 103 (Full-Stack Developer)
del JobRole[103]
# Print dictionary after another deletion
print("\nJobRole after removing key 103 (Full-Stack Developer):")
print(JobRole)
# Print the number of remaining roles
print("\nTotal Number of Job Roles:", len(JobRole))
# Print all keys in the dictionary
print("\nList of Job Role IDs:", JobRole.keys())
# Print all values in the dictionary
print("\nList of Job Role Names:", JobRole.values())
