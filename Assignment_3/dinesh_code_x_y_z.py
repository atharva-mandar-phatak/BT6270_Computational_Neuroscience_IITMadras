import numpy as np
import scipy
from scipy.integrate import odeint

# Define the system of ODEs
def system(y, t, mu, w1, w2, W12, W21, phi):
    r1, theta1, r2, theta2 = y
    dr1dt = (mu - np.square(r1))*r1 + W12*r2*np.cos(theta2 - theta1 + phi)
    dr2dt = (mu - np.square(r2))*r2 + W21*r1*np.cos(theta1 - theta2 - phi)
    dtheta1dt = w1 + (W12*(r2/r1)*(np.sin(theta2 - theta1 + phi)))
    dtheta2dt = w2 + (W21*(r1/r2)*(np.sin(theta1 - theta2 - phi)))
    return [dr1dt, dtheta1dt, dr2dt, dtheta2dt]

# Set the initial conditions and parameters
mu = 1
w1 = 5
w2 = 5
W12 = 0.2
W21 = 0.2
phi = np.radians(45)  # Convert phase difference from degrees to radians
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
z1 = r1 * np.cos(theta1)
z2 = r2 * np.cos(theta2)

# Create a new figure
plt.figure()

# Plot theta_diff
plt.subplot(2, 1, 1)
plt.plot(t, theta_diff)

plt.xlabel('Time')
plt.ylabel('Theta1 - Theta2')

# Plot z1 and z2
plt.subplot(2, 1, 2)
plt.plot(t, z1, label='z1')
plt.plot(t, z2, label='z2')
plt.xlim([0,10])
plt.ylim([-1,1])
plt.xlabel('Time')
plt.ylabel('z')
plt.legend()

# Show the figure
plt.show()