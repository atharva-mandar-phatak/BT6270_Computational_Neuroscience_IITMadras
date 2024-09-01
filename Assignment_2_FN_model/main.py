import numpy as np
import matplotlib.pyplot as plt

# Initializing important parametres
a = 0.5
b, r = 0.1, 0.1

# Setting the time interval
lim_lw = 0
lim_up = 101
t_tot = lim_up - lim_lw
n = 1000000  # no fo points
dt = (t_tot) / n

#Defining lambda functions for dv/dt and dw/dt
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

#Defining function for nullclines
def nullclines(I, v):
    vnc = f(v) + I
    wnc = b * v / r
    return vnc, wnc

#Defining function to plot voltage vs time graphs
def plot_voltage_vs_time(y, title="", ylim=(), x=None, xlim=()):
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
    if ylim: plt.ylim(ylim)
    if xlim: plt.xlim(xlim)
    plt.xlabel("Time (in sec)")
    plt.ylabel("Voltage")
    plt.legend(["V(t)", "W(t)"])
    plt.minorticks_on()
    plt.grid()
    plt.show()

#Defining function to plot nullclines
def plot_nullclines(I, xlim, ylim, positions):
    color_pellet = ['darkviolet', 'cadetblue', 'slategray', 'navy', 'crimson', 'lightcoral', 'maroon', 'olive', 'khaki',
                    'springgreen']*3
    v = np.linspace(xlim[0], xlim[1], 100)
    w = np.linspace(xlim[0], xlim[1], 100)

    v_mesh, w_mesh = np.meshgrid(v, w)
    v_vel = dvdt(v_mesh, w_mesh, I)
    w_vel = dwdt(v_mesh, w_mesh)

    vnc, wnc = nullclines(I, v)

    plt.figure()
    plt.plot(v, vnc, 'b')
    plt.plot(v, wnc, 'r')
    plt.legend(['v nullcline', 'w nullcline'])
    plt.ylim(ylim[0], ylim[1])
    title = f"Phase Plot for I={I}"
    plt.title(title)
    plt.xlabel('v-values')
    plt.ylabel('w-vaues')

    if positions:
        for i in range(len(positions)):
            plt.streamplot(v_mesh, w_mesh, v_vel, w_vel, density=2, start_points=[positions[i]], color=color_pellet[i],
                           integration_direction="forward", arrowsize=2)
    else:
        plt.streamplot(v_mesh, w_mesh, v_vel, w_vel, color=color_pellet[0])
    plt.grid()
    plt.show()


# Plotting for various cases

#||||||||||||||||||||||||||||||||

# Case 1: I_ext = 0
I = 0

# Nullclines
plot_nullclines(I, (-0.5, 1.5), (-0.45, 0.45), [])
plot_nullclines(I, (-0.5, 1.5), (-0.45, 0.45), [[0, 0], [0.4, 0], [0.6, 0], [1, 0]])

# Subcase 1: V(0) < a and W(0) = 0
x = list(np.linspace(0, 101, 1000000))
vhist, whist = euler_integrate(0.4, 0, I)
plot_voltage_vs_time([vhist, whist], "I=0, Subcase 1: V(0) < a and W(0) = 0", (-0.2, 0.75), x)

# Subcase 2: V(0) > a and W(0) = 0
vhist, whist = euler_integrate(0.6, 0, I)
plot_voltage_vs_time([vhist, whist], "I=0, Subcase 2: V(0) > a and W(0) = 0", (-0.2, 0.75), x)

#||||||||||||||||||||||||||||||||

# Case 2: I_ext = 0.51
I = 0.51

# Nullclines
plot_nullclines(I, (-0.5, 1.5), (0.15, 0.95), [])
plot_nullclines(I, (-0.5, 1.5), (0.15, 0.95), [[0, 0], [0.4, 0], [0.6, 0], [1, 0]])

# Plotting v(t) and w(t) graphs
x = list(np.linspace(0, 101, 1000000))
vhist, whist = euler_integrate(0.4, 0, I)
plot_voltage_vs_time([vhist, whist], "v(t) and w(t) graphs for I =0.51", (-0.2, 1.5), x)

#||||||||||||||||||||||||||||||||
# Case 3: I_ext = 0.81
I = 0.81

# Nullclines
plot_nullclines(I, (-0.5, 1.5), (0.55, 1.45), [])
plot_nullclines(I, (-0.5, 1.5), (0.55, 1.45),
                [[0, 0.6], [0.4, 0.6], [0.6, 0.6], [1, 0.6], [0, 1.4], [0.4, 1.4], [0.6, 1.4], [1, 1.4]])

# Plotting v(t) and w(t) graphs
x = list(np.linspace(0, 101, 1000000))
vhist, whist = euler_integrate(0.4, 0, I)
plot_voltage_vs_time([vhist, whist], "v(t) and w(t) graphs", (-0.2, 2), x)

#||||||||||||||||||||||||||||||||
# Case 4: I_ext = 0.021
I = 0.021

# Choosing parameters
b, r = 0.011, 0.81

# Nullclines
plot_nullclines(I, (-0.5, 1.5), (-0.45, 0.45), [])
plot_nullclines(I, (-0.5, 1.5), (-0.45, 0.45),
                [[0, 0.4], [0.1, 0.4], [-0.1, 0.4], [0, -0.4], [0.4, 0.4], [0.6, 0.4], [1, 0.4], [0.1, -0.4],
                 [-0.1, -0.4], [0.4, -0.4], [0.6, -0.4], [1, -0.4]])

# Plotting v(t) and w(t) graphs
x = list(np.linspace(0, 101, 1000000))
vhist, whist = euler_integrate(0.4, 0, I)
plot_voltage_vs_time([vhist, whist], "v(t) and w(t) graphs" , (-0.2, 2), x)
