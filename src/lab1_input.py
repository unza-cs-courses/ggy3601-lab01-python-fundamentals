#!/usr/bin/env python3
"""
Lab 1 - Task 4: User Input and Output
GGY3601 Python Programming for Earth Sciences

Instructions:
1. This task collects sample information from user input
2. The program should validate and format the output
3. Classification threshold: grade >= 2.0 is "Economic"

TODO: Complete the sample entry system below
"""

# Collect sample information from user
sample_id = input('Enter sample ID: ')
rock_type = input('Enter rock type: ')
grade = float(input('Enter grade (%): '))
depth = int(input('Enter depth (m): '))

# Display formatted summary
print('\n--- Sample Summary ---')
print(f'Sample ID: {sample_id}')
print(f'Rock Type: {rock_type}')
print(f'Grade: {grade:.2f}%')
print(f'Depth: {depth} meters')

# Classify the grade
# TODO: Add the classification logic
# If grade >= 2.0, print "Classification: Economic"
# Otherwise, print "Classification: Sub-economic"
if grade >= 2.0:
    print("Classification: Economic")
else:
    print("Classification: Sub-economic")
