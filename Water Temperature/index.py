import numpy as np
import matplotlib.pyplot as plt

# Define the temperature range and membership function
temp_range = np.arange(0, 51, 2)
membership_off = np.zeros_like(temp_range)
membership_on = np.zeros_like(temp_range)

# Define the ideal temperature range
ideal_temp_start = 18
ideal_temp_end = 26

# Assign membership values
membership_off[(temp_range <= ideal_temp_end)] = 1 #temp < = 18 (Motor Off)
membership_on[(temp_range >= ideal_temp_end)] = 1

# Plot the membership functions
plt.figure(figsize=(8, 6))
plt.plot(temp_range, membership_off, 'r', label='OFF')
plt.plot(temp_range, membership_on, 'g', label='ON')
plt.fill_between(temp_range, membership_off, color='r', alpha=0.1)
plt.fill_between(temp_range, membership_on, color='g', alpha=0.1)
plt.title('Fuzzy Rule for Motor Activation based on Water Temperature')
plt.xlabel('Water Temperature (°C)')
plt.ylabel('Membership Degree')
plt.ylim(0, 1.1)
plt.legend()
plt.grid(True)
plt.show()