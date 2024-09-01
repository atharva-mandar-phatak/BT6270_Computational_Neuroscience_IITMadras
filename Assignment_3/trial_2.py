import numpy as np
import matplotlib.pyplot as plt

# Define the Hopf oscillator equations
def hopf_oscillator(state, t, mu):
    x, y = state
    dx_dt = -y + mu * x * (1 - x ** 2 - y ** 2)
    dy_dt = x + mu * y * (1 - x ** 2 - y ** 2)
    return [dx_dt, dy_dt]

# Define the function to simulate the coupled oscillators
def simulate_coupled_oscillators(mu1, mu2, initial_state1, initial_state2, coupling, omega1=5, omega2=5, time=100, dt=0.1):
    t = np.arange(0, time, dt)
    states1 = np.zeros((len(t), 2))
    states2 = np.zeros((len(t), 2))

    states1[0] = initial_state1
    states2[0] = initial_state2

    for i in range(1, len(t)):
        state1 = states1[i - 1]
        state2 = states2[i - 1]

        # Calculate the coupling term
        if coupling == "complex":
            w12 = 2 * np.pi * omega1 * 180 / 360
            w21 = 2 * np.pi * omega2 * 180 / 360
            coupling_term1 = np.array([np.cos(w12 * t[i]), np.sin(w12 * t[i])])
            coupling_term2 = np.array([np.cos(w21 * t[i]), np.sin(w21 * t[i])])
        elif coupling == "power":
            w12 = 2 * np.pi * omega1 * 180 / 360
            w21 = 2 * np.pi * omega2 * 180 / 360
            coupling_term1 = np.array([np.cos(w12), np.sin(w12)])
            coupling_term2 = np.array([np.cos(w21), np.sin(w21)])

        # Calculate the derivatives for both oscillators
        dx1, dy1 = hopf_oscillator(state1, t[i], mu1)
        dx2, dy2 = hopf_oscillator(state2, t[i], mu2)

        # Update states with coupling
        states1[i] = state1 + np.array([dx1, dy1]) * dt + coupling_term1
        states2[i] = state2 + np.array([dx2, dy2]) * dt + coupling_term2

    return states1, states2,t

# Initial conditions for the oscillators
initial_state1 = [0.5, 0.5]
initial_state2 = [0.5, -0.5]

# Simulate complex coupling with a phase difference of 47 degrees
states1_complex, states2_complex, t_complex = simulate_coupled_oscillators(0.2, 0.2, initial_state1, initial_state2, "complex")
plt.figure(figsize=(10, 6))
plt.plot(t_complex, np.arctan2(states1_complex[:, 1], states1_complex[:, 0]), label='Oscillator 1',color='red')
plt.plot(t_complex, np.arctan2(states2_complex[:, 1], states2_complex[:, 0]), label='Oscillator 2', color='blue')
plt.xlim([0,10])

plt.title("Complex Coupling - Phase Difference: 47 degrees")
plt.xlabel('Time')
plt.ylabel('Phase')
plt.legend()
plt.show()

