import numpy as np
import matplotlib.pyplot as plt

# Suppoting code to check the I1 and I2 values

# Initializing important parametres
a = 0.5
b, r = 0.1, 0.1

# Setting the time interval
lim_lw = 0
lim_up = 101
t_tot = lim_up - lim_lw
n = 1000000  # no fo points
dt = (t_tot) / n

# Defining lambda functions for dv/dt and dw/dt
f = lambda v: v * (a - v) * (v - 1)
dvdt = lambda v, w, I: f(v) - w + I
dwdt = lambda v, w: b * v - r * w


# Euler Integration
def euler_integrate(v0, w0, Ia0):
    # Defining arrays to store values of v(t) and w(t) for each iteration of Euler Integration
    v_arr = np.ones(n)
    w_arr = np.ones(n)
    # Initial Conditions
    Ia = Ia0
    v_arr[0] = v0
    w_arr[0] = w0
    for i in range(n):
        if (i < (n - 1)):
            v_arr[i + 1] = v_arr[i] + ((dvdt(v_arr[i], w_arr[i], Ia)) * dt)
            w_arr[i + 1] = w_arr[i] + ((dwdt(v_arr[i], w_arr[i])) * dt)
    return (v_arr, w_arr)


# Defining function to plot voltage vs time graphs
def plot_voltage_vs_time(y, title="", x=None):
    plt.figure()
    plt.title(title)
    color_pellet = ['darkviolet', 'cadetblue', 'slategray', 'navy', 'crimson', 'lightcoral', 'maroon', 'olive', 'khaki',
                    'springgreen']
    if not x:
        for i in y:
            plt.plot(i)
    else:
        for i, j in enumerate(y):
            plt.plot(x, j, color=color_pellet[i])
        plt.xlabel("Time (in sec)")
    plt.ylabel("Voltage")
    plt.legend(["V(t)", "W(t)"])
    plt.minorticks_on()
    plt.grid()
    plt.show()


low_bound = float(input("Enter lower bound :"))
upper_bound = float(input("Enter lower bound :"))
step_size = float(input("Enter step size :"))
ia_aaray = np.arange(low_bound, upper_bound, step_size)
for i in ia_aaray:
    x = list(np.linspace(0, 101, 1000000))
    vhist, whist = euler_integrate(0.4, 0, i)
    plot_voltage_vs_time([vhist, whist], f"I={i}", x)
