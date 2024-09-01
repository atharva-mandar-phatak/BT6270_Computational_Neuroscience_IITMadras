import numpy as np
from scipy.integrate import odeint

# Define the system of ODEs
def p_system(py, t, pmu, pw1, pw2, pW12, pW21, pphi,pr1, pr2, ptheta1, ptheta2, xhi= py):

    dpr1dt = (pmu - np.square(pr1))pr1 + (pW12(np.power(pr2, (pw1/pw2))np.cos(pw1(ptheta2/pw2 - ptheta1/pw1 + pphi/(pw1*pw2)))))
    dpr2dt = (pmu - np.square(pr2))pr2 + (pW21(np.power(pr1, (pw2/pw1))np.cos(pw2(ptheta1/pw1 - ptheta2/pw2 - pphi/(pw1*pw2)))))
    dptheta1dt = pw1 + (pW12*(np.power(pr2, (pw1/pw2))/pr1)(np.sin(pw1(ptheta2/pw2 - ptheta1/pw1 + pphi/(pw1*pw2)))))
    dptheta2dt = pw2 + (pW21*(np.power(pr1, (pw2/pw1))/pr2)(np.sin(pw2(ptheta1/pw1 - ptheta2/pw2 - pphi/(pw1*pw2)))))
    dxhidt = ((pW12*(np.power(pr2, (pw1/pw2))))/(pw1*pr1)) * np.sin(pw1*(pphi/(pw1*pw2) - xhi)) + ((pW12*(np.power(pr1, (pw2/pw1))))/(pw2*pr2)) * np.sin(pw2*(pphi/(pw1*pw2) - xhi))
    return [dpr1dt, dpr2dt, dptheta1dt, dptheta2dt, dxhidt]


# Set the initial conditions and parameters
pmu = 1
pw1 = 5
pw2 = 10
pW12 = 0.2
pW21 = 0.2
pphi =  2.9644 # Convert phase difference from degrees to radians
py0 = [1, 0.5, 3.7008, 2.3106, (phi/50)]  # Initial conditions for r1, theta1, r2, theta2
t = np.linspace(0, 100, 10000)  # Time grid

# Solve the ODEs
psol = odeint(p_system, py0, t, args=(pmu, pw1, pw2, pW12, pW21, pphi))

import matplotlib.pyplot as plt

# Calculate the difference in angles
pxhi = psol[:, 2]/pw1 - psol[:, 3]/pw2

# Calculate the derivative of xhi
import numpy as np

# Extract the xhi values
xhi_values = psol[:, 4]

# Compute dxhi/dt
dxhidt_values = np.gradient(xhi_values, t)

# Calculate the expression ptheta2/w2 - ptheta1/w1 + phi/(w1*w2)
expr = pxhi - pphi/(pw1*pw2)

import matplotlib.pyplot as plt

# Create a new figure
plt.figure()

# Plot normalized phase difference
plt.plot(t, pxhi, label='Normalized phase difference')

plt.plot(t, dxhidt_values, label='dxhidt')

# Add labels and legend
plt.xlabel('Time')
plt.ylabel('Values')
plt.legend()

# Show the figure
plt.show()


# Plot the expression ptheta2/w2 - ptheta1/w1 + phi/(w1*w2)
plt.figure()
plt.plot(t, expr)
plt.xlabel('Time')
plt.ylabel('ptheta2/w2 - ptheta1/w1 - phi/(w1*w2)')
plt.show()