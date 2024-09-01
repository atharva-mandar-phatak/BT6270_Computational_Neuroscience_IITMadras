import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Get user input for the required phase difference
phi_degrees = float(input("Enter the required phase difference in degrees: "))


# Define the system of ODEs for power coupling using Hopf Oscillator
def power_coupling_hopf_oscillator(py, t, mu, omega1, omega2, coupling_strength_12, coupling_strength_21,
                                   phase_difference):
    radius_1, radius_2, angle_1, angle_2, xi = py
    drdt_1 = (mu - np.square(radius_1)) * radius_1 + (
            coupling_strength_12 * np.power(radius_2, (omega1 / omega2)) * np.cos(
        omega1 * (angle_2 / omega2 - angle_1 / omega1 + phase_difference / (omega1 * omega2))))
    drdt_2 = (mu - np.square(radius_2)) * radius_2 + (
            coupling_strength_21 * np.power(radius_1, (omega2 / omega1)) * np.cos(
        omega2 * (angle_1 / omega1 - angle_2 / omega2 - phase_difference / (omega1 * omega2))))
    dthetadt_1 = omega1 + (coupling_strength_12 * np.power(radius_2, (omega1 / omega2)) / radius_1) * np.sin(
        omega1 * (angle_2 / omega2 - angle_1 / omega1 + phase_difference / (omega1 * omega2)))
    dthetadt_2 = omega2 + (coupling_strength_21 * np.power(radius_1, (omega2 / omega1)) / radius_2) * np.sin(
        omega2 * (angle_1 / omega1 - angle_2 / omega2 - phase_difference / (omega1 * omega2)))
    dxidt = (coupling_strength_12 * np.power(radius_2, (omega1 / omega2)) / (omega1 * radius_1)) * np.sin(
        omega1 * (phase_difference / (omega1 * omega2) - xi)) + (
                    coupling_strength_12 * np.power(radius_1, (omega2 / omega1)) / (omega2 * radius_2)) * np.sin(
        omega2 * (phase_difference / (omega1 * omega2) - xi))
    return [drdt_1, drdt_2, dthetadt_1, dthetadt_2, dxidt]


# Set the initial conditions and parameters
mu_value = 1
omega1_value = 5
omega2_value = 15
coupling_strength_12_value = 0.2
coupling_strength_21_value = 0.2
phi_radians = np.radians(phi_degrees)
initial_conditions = [1, 0.5, 3.7008, 2.3106, np.round(phi_radians / 50)]
time_grid = np.linspace(0, 100, 10000)

# Solve the ODEs
solution = odeint(power_coupling_hopf_oscillator, initial_conditions, time_grid, args=(
    mu_value, omega1_value, omega2_value, coupling_strength_12_value, coupling_strength_21_value, phi_radians))

# Extract variables
radius_1, radius_2, angle_1, angle_2, xi_values = solution[:, 0], solution[:, 1], solution[:, 2], solution[:,
                                                                                                  3], solution[:, 4]

# Calculate normalized phase difference
normalized_phase_difference = angle_1 / omega1_value - angle_2 / omega2_value

# Compute dxi/dt
dxi_values = np.gradient(xi_values, time_grid)

# Calculate the expression theta2/w2 - theta1/w1 + phi/(w1*w2)
expression = normalized_phase_difference - phi_radians / (omega1_value * omega2_value)

# Plot normalized phase difference
plt.figure()
plt.title(f"Normalized phase difference variation (required {phi_degrees}°) with time")
plt.plot(time_grid, normalized_phase_difference, label='Normalized phase difference', color='orange')
plt.grid()
plt.xlabel('Time (t)')
plt.ylabel(chr(936))
plt.legend()
plt.show()

# Plot the expression theta2/w2 - theta1/w1 + phi/(w1*w2)
plt.figure()
plt.title(f'\u03C3 variation with time for normalized phase difference of {phi_degrees}°')
plt.plot(time_grid, expression, label='\u03C3', color='indigo')
plt.legend()
plt.xlabel('Time')
plt.ylabel('\u03C3')
plt.grid()
plt.show()
