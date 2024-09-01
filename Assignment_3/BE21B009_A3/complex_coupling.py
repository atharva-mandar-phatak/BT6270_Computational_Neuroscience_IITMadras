import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

phi_deg = float(input("Enter the required phase difference in degrees: "))


# Define the system of ODEs for complex coupling using Hopf Oscillator
def hopf_oscillator_system(y, t, mu, omega1, omega2, coupling_strength_12, coupling_strength_21, phase_difference):
    r1, theta1, r2, theta2 = y
    dr1dt = (mu - np.square(r1)) * r1 + coupling_strength_12 * r2 * np.cos(theta2 - theta1 + phase_difference)
    dr2dt = (mu - np.square(r2)) * r2 + coupling_strength_21 * r1 * np.cos(theta1 - theta2 - phase_difference)
    dtheta1dt = omega1 + (coupling_strength_12 * (r2 / r1) * (np.sin(theta2 - theta1 + phase_difference)))
    dtheta2dt = omega2 + (coupling_strength_21 * (r1 / r2) * (np.sin(theta1 - theta2 - phase_difference)))
    return [dr1dt, dtheta1dt, dr2dt, dtheta2dt]


# Set the initial conditions and parameters
mu = 1
omega1 = 5
omega2 = 5
coupling_strength_12, coupling_strength_21 = [float(x) for x in input("Enter coupling strengths: ").split()]

phase_difference = np.radians(phi_deg)  # Convert phase difference from degrees to radians
initial_conditions = [0.5, 2.1, 0.7, 0.8]  # Initial conditions for r1, theta1, r2, theta2
time_grid = np.linspace(0, 20, 1000)  # Time grid

# Solve the ODEs
solution = odeint(hopf_oscillator_system, initial_conditions, time_grid,
                  args=(mu, omega1, omega2, coupling_strength_12, coupling_strength_21, phase_difference))

# Extract variables
radius_1, angle_1, radius_2, angle_2 = solution[:, 0], solution[:, 1], solution[:, 2], solution[:, 3]

# Calculate phase difference
phase_difference = angle_1 - angle_2

# Calculate complex variables
real_part_1 = radius_1 * np.cos(angle_1)
real_part_2 = radius_2 * np.cos(angle_2)
imaginary_part_1 = radius_1 * np.sin(angle_1)
imaginary_part_2 = radius_2 * np.sin(angle_2)

# Plot phase difference
fig, ax1 = plt.subplots()
ax1.plot(time_grid, phase_difference, label='Phase Difference', color='indigo')
fig.suptitle(f"Coupling constants " + r" $W_{12}$ = $W_{21}$ = " + f"{coupling_strength_12}", style='italic')
plt.title(f"Phase difference for  {np.radians(phi_deg).round(4)}")
plt.legend()
ax1.grid()
ax1.set_xlabel('Time')
ax1.set_ylabel(r'$\Theta_1$ - $\Theta_2$')

# Plot real parts of z1 and z2
fig, ax2 = plt.subplots()
fig.suptitle(f"Coupling of Oscillators at  {np.radians(phi_deg).round(4)}")
plt.title(f"Coupling constants " + r" $W_{12}$ = $W_{21}$ = " + f"{coupling_strength_12}", style='italic')
ax2.plot(time_grid, real_part_1, label='Real(z1)', color='indigo')
ax2.plot(time_grid, real_part_2, label='Real(z2)', color='orange')
ax2.set_xlim([0, 10])
ax2.set_ylim([-2, 2])
ax2.set_xlabel('Time (t)')
ax2.set_ylabel('Real(z)')
ax2.yaxis.tick_left()
ax2.xaxis.tick_bottom()
ax2.grid()
ax2.legend()

# Plot imaginary parts of z1 and z2
fig, ax3 = plt.subplots()
fig.suptitle(f"Coupling of Oscillators at  {np.radians(phi_deg).round(4)}")
plt.title(f"Coupling constants " + r" $W_{12}$ = $W_{21}$ = " + f"{coupling_strength_12}", style='italic')
ax3.plot(time_grid, imaginary_part_1, label='Imag(z1)', color='indigo')
ax3.plot(time_grid, imaginary_part_2, label='Imag(z2)', color='orange')
ax3.set_xlim([0, 10])
ax3.set_ylim([-2, 2])
ax3.set_xlabel('Time (t)')
ax3.set_ylabel('Imag(z)')
ax3.yaxis.tick_left()
ax3.xaxis.tick_bottom()
ax3.grid()
ax3.legend()

# Show the figures
plt.show()
