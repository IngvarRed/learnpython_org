# Numpy Arrays

# Create 2 new lists height and weight
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# Import the numpy package as np
import numpy as np

# Create 2 numpy arrays from height and weight
np_height = np.array(height)
np_weight = np.array(weight)

print(np_height)
print(np_weight)

# Print out the type of np_height
print(type(np_height))

# Calculate bmi
bmi = np_weight / np_height ** 2

# Print the result
print(bmi)

# For a boolean response
bmi > 23

# Print only those observations above 23
bmi[bmi > 23]


# Exercise
print('=== Exercise ===')
'''
First, convert the list of weights from a list to a Numpy array. 
Then, convert all of the weights from kilograms to pounds. 
Use the scalar conversion of 2.2 lbs per kilogram to make your conversion. 
Lastly, print the resulting array of weights in pounds.
'''

weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

import numpy as np

# Create a numpy array np_weight_kg from weight_kg
np_weight_kg = np.array(weight_kg)

# Create np_weight_lbs from np_weight_kg
np_weight_po = np_weight_kg * 2.2

# Print out np_weight_lbs
print(np_weight_po)
