# File Name: set_operations_demo.py

Set = {'Python', 'C', 'C++', 'SQL', 'React JS', 'Angular JS'}
Set2 = {'Python', 'History', 'Chemistry'}
# Adding single elements
Set.add('HTML')
Set.add('CSS')
Set.add('Nord JS')
# Adding multiple elements
Set.update(['Biochemistry', 'Genetics'])
# Removing specific elements
Set.remove('HTML')    
Set.pop()             
Set.discard('C')      
# Union of sets
print("Union of sets:", Set | Set2)
# Intersection of sets
print("Intersection of sets:", Set & Set2)
