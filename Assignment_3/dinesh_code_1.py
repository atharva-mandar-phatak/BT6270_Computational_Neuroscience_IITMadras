import numpy as np
import scipy
from scipy.integrate import odeint

phi_deg = float(input("Enter the required phase difference in degrees: "))


# Define the system of ODEs
def system(y, t, mu, w1, w2, W12, W21, phi):
    r1, theta1, r2, theta2 = y
    dr1dt = (mu - np.square(r1)) * r1 + W12 * r2 * np.cos(theta2 - theta1 + phi)
    dr2dt = (mu - np.square(r2)) * r2 + W21 * r1 * np.cos(theta1 - theta2 - phi)
    dtheta1dt = w1 + (W12 * (r2 / r1) * (np.sin(theta2 - theta1 + phi)))
    dtheta2dt = w2 + (W21 * (r1 / r2) * (np.sin(theta1 - theta2 - phi)))
    return [dr1dt, dtheta1dt, dr2dt, dtheta2dt]


# Set the initial conditions and parameters
mu = 1
w1 = 5
w2 = 5
W12 = 0.7
W21 = 0.7
phi = np.radians(phi_deg)  # Convert phase difference from degrees to radians
y0 = [0.5, 2.1, 0.7, 0.8]  # Initial conditions for r1, theta1, r2, theta2
t = np.linspace(0, 20, 1000)  # Time grid

# Solve the ODEs
sol = odeint(system, y0, t, args=(mu, w1, w2, W12, W21, phi))

# The solution is an array with four columns, each containing the solution for one of the variables
r1 = sol[:, 0]
theta1 = sol[:, 1]
r2 = sol[:, 2]
theta2 = sol[:, 3]

import matplotlib.pyplot as plt

# Calculate the difference in angles
theta_diff = theta1 - theta2

# Calculate the complex variables
real_z1 = r1 * np.cos(theta1)
real_z2 = r2 * np.cos(theta2)

# Create a new figure
plt.figure()

# Plot theta_diff
#plt.subplot(2, 1, 1)
plt.
plt.plot(t, theta_diff, label='phase difference')
plt.legend()
plt.xlabel('Time')
plt.ylabel(r'$\Theta_1$ - $\Theta_2$')

plt.show()

# Plot z1 and z2
plt.figure()
#plt.subplot(2, 1, 2)
plt.plot(t, real_z1, label='real(z1)')
plt.plot(t, real_z2, label='real(z2)')
plt.xlim([0, 10])
plt.ylim([-2, 2])
plt.xlabel('Time (t)')
plt.ylabel('real(z)')
plt.yticks()
plt.xticks()
plt.legend()

# Show the figure
plt.show()
