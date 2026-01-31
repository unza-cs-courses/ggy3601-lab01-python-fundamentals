#!/usr/bin/env python3
"""
Lab 1 - Task 3: Arithmetic Expressions
GGY3601 Python Programming for Earth Sciences

Instructions:
1. Check ASSIGNMENT.md for YOUR unique values
2. Replace placeholder values with your assigned values
3. Complete the calculations as specified

TODO: Complete this file using your assigned values from ASSIGNMENT.md
"""

import math

# Given data - USE YOUR ASSIGNED VALUES FROM ASSIGNMENT.md
mass = 11.6      # TODO: Replace with your sample_mass (kg)
volume = 7.8    # TODO: Replace with your sample_volume (cubic meters)
depth_start = 100  # meters (keep this value)
depth_end = 225      # TODO: Replace with your sample_depth (meters)

# Calculate density (mass / volume)
# TODO: Calculate and print density to 2 decimal places
density = mass / volume  # YOUR CALCULATION HERE
print(f'Density: {density:.2f} kg/m3')

# Calculate drilling interval
# TODO: Calculate interval (depth_end - depth_start)
interval = depth_end - depth_start  # YOUR CALCULATION HERE
print(f'Drilling interval: {interval} meters')

# Calculate average depth
# TODO: Calculate average of depth_start and depth_end
avg_depth = (depth_start + depth_end) / 2  # YOUR CALCULATION HERE
print(f'Average depth: {avg_depth} meters')

# Calculate volume of cylindrical core
# radius = 0.05m (5cm), length = interval
# Formula: V = pi * r^2 * length
radius = 0.05
core_volume = math.pi * radius**2 * interval  # TODO: YOUR CALCULATION HERE
print(f'Core volume: {core_volume:.4f} cubic meters')
