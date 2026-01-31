# Your Assignment Parameters

These are your unique values for Lab 1. Use these exact values in your code.

## Task Values

| Parameter | Your Value |
|-----------|------------|
| Sample Depth | {sample_depth} meters |
| Sample Mass | {sample_mass} kg |
| Sample Volume | {sample_volume} cubic meters |
| Rock Type | {rock_type} |
| Grade Value | {grade_value}% |

## Task 1: Environment Verification (10 marks)

1. Open a terminal/command prompt
2. Run: `python --version` (or `python3 --version`)
3. Create `src/lab1_setup.py` with:

```python
# lab1_setup.py
# Your Name: [YOUR NAME]
# Student ID: [YOUR ID]
import sys
print(f'Python version: {sys.version}')
print('Environment setup successful!')
```

## Task 2: Variables and Data Types (20 marks)

Create `src/lab1_variables.py` demonstrating all four basic data types using YOUR values:

```python
# lab1_variables.py
# Integer: Store a sample depth in meters
depth = {sample_depth}

# Float: Store an ore grade percentage
grade = {grade_value}

# String: Store a rock type name
rock_type = '{rock_type}'

# Boolean: Store whether sample is processed
is_processed = False

# Print each variable with its type
print(f'Depth: {{depth}}, Type: {{type(depth)}}')
print(f'Grade: {{grade}}, Type: {{type(grade)}}')
print(f'Rock Type: {{rock_type}}, Type: {{type(rock_type)}}')
print(f'Processed: {{is_processed}}, Type: {{type(is_processed)}}')
```

## Task 3: Arithmetic Expressions (20 marks)

Create `src/lab1_calculations.py` that performs geological calculations using YOUR values:

```python
# lab1_calculations.py
# Given data - USE YOUR ASSIGNED VALUES
mass = {sample_mass}      # kg
volume = {sample_volume}  # cubic meters
depth_start = 100         # meters
depth_end = {sample_depth}  # meters

# Calculate density (mass / volume)
density = mass / volume
print(f'Density: {{density:.2f}} kg/m3')

# Calculate drilling interval
interval = depth_end - depth_start
print(f'Drilling interval: {{interval}} meters')

# Calculate average depth
avg_depth = (depth_start + depth_end) / 2
print(f'Average depth: {{avg_depth}} meters')

# Calculate volume of cylindrical core
import math
radius = 0.05  # 5cm
core_volume = math.pi * radius**2 * interval
print(f'Core volume: {{core_volume:.4f}} cubic meters')
```

## Task 4: User Input and Output (20 marks)

Create `src/lab1_input.py` that collects sample information:

```python
# lab1_input.py
sample_id = input('Enter sample ID: ')
rock_type = input('Enter rock type: ')
grade = float(input('Enter grade (%): '))
depth = int(input('Enter depth (m): '))

print('\\n--- Sample Summary ---')
print(f'Sample ID: {{sample_id}}')
print(f'Rock Type: {{rock_type}}')
print(f'Grade: {{grade:.2f}}%')
print(f'Depth: {{depth}} meters')

if grade >= 2.0:
    print('Classification: Economic')
else:
    print('Classification: Sub-economic')
```

## Task 5: String Operations (15 marks)

Create `src/lab1_strings.py` demonstrating string manipulation:

```python
# lab1_strings.py
sample_id = 'GEO-2024-001'
description = '  High grade {rock_type} sample  '

# String methods
print(f'Original ID: {{sample_id}}')
print(f'Lowercase: {{sample_id.lower()}}')
print(f'Replace: {{sample_id.replace("GEO", "SAMPLE")}}')

# Trimming whitespace
print(f'Before strip: "{{description}}"')
print(f'After strip: "{{description.strip()}}"')

# String slicing
print(f'Year from ID: {{sample_id[4:8]}}')
print(f'First 3 chars: {{sample_id[:3]}}')
```

## Code Quality (15 marks)

- Include comments explaining your code
- Use meaningful variable names
- Format output clearly

## Testing Your Code

Run the automated tests locally:

```bash
pytest tests/visible/ -v
```

Push to GitHub to see your score on the Actions tab.
