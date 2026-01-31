#!/usr/bin/env python3
"""
Lab 1 - Task 5: String Operations
GGY3601 Python Programming for Earth Sciences

Instructions:
1. Demonstrate various string manipulation methods
2. Use your assigned rock_type from ASSIGNMENT.md in the description

TODO: Complete the string operations below
"""

# Sample data
sample_id = 'GEO-2024-001'
description = '  High grade sample  '  # TODO: You can modify this to include your rock_type

# String methods
print(f'Original ID: {sample_id}')

# TODO: Print lowercase version of sample_id
print(f'Lowercase: {sample_id.lower()}')

# TODO: Replace "GEO" with "SAMPLE"
print(f'Replace: {sample_id.replace("GEO", "SAMPLE")}')

# Trimming whitespace
print(f'Before strip: "{description}"')
print(f'After strip: "{description.strip()}"')

# String slicing
# TODO: Extract the year (positions 4-8) from sample_id
print(f'Year from ID: {sample_id[4:8]}')

# TODO: Extract first 3 characters from sample_id
print(f'First 3 chars: {sample_id[:3]}')

# String concatenation
# TODO: Combine sample_id and stripped description with ' - ' between them
full_name = sample_id + ' - ' + description.strip()
print(f'Full name: {full_name}')
