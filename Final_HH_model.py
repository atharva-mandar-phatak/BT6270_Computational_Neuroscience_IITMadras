import sys
import numpy as np
from math import exp
from tqdm import tqdm
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

current_range = np.arange(0, 1, 0.01)   
npeaks_hist = np.zeros(current_range.shape)


def find_peak(v_array):
    peak, _ = find_peaks(v_array, height=10)
    return len(peak)


def hh_model(cur_iter):
    gkmax = 0.36
    vk = -77
    gnamax = 1.20
    vna = 50
    gl = 0.003
    vl = -54.387
    cm = 0.01

    dt = 0.01
    niter = 50000
    t = np.arange(1, niter, dt)

    v = -64.9964
    m = 0.0530
    h = 0.5960
    n = 0.3177

    gnahist = np.zeros((niter))
    gkhist = np.zeros((niter))
    vhist = np.zeros((niter))
    mhist = np.zeros((niter))
    hhist = np.zeros((niter))
    nhist = np.zeros((niter))

    for iteration in range(niter):
        gna = gnamax * m ** 3 * h
        gk = gkmax * n ** 4
        gtot = gna + gk + gl
        vinf = ((gna * vna + gk * vk + gl * vl) + current_range[cur_iter]) / gtot
        tauv = cm / gtot

        v = vinf + (v - vinf) * exp(-dt / tauv)

        alpham = 0.1 * (v + 40) / (1 - exp(-(v + 40) / 10))
        betam = 4 * exp(-0.0556 * (v + 65))

        alphan = 0.01 * (v + 55) / (1 - exp(-(v + 55) / 10))
        betan = 0.125 * exp(-(v + 65) / 80)

        alphah = 0.07 * exp(-0.05 * (v + 65))
        betah = 1 / (1 + exp(-0.1 * (v + 35)))

        taum = 1 / (alpham + betam)
        tauh = 1 / (alphah + betah)
        taun = 1 / (alphan + betan)

        minf = alpham * taum
        hinf = alphah * tauh
        ninf = alphan * taun

        m = minf + (m - minf) * exp(-dt / taum)
        h = hinf + (h - hinf) * exp(-dt / tauh)
        n = ninf + (n - ninf) * exp(-dt / taun)

        vhist[iteration] = v
        mhist[iteration] = m
        hhist[iteration] = h
        nhist[iteration] = n

    npeaks_hist[cur_iter] = find_peak(vhist)


for ext_curr in tqdm(range((current_range.size))):
    hh_model(ext_curr)


I1_var = 0.0224*np.ones(len(npeaks_hist))
I2_var = 0.0625*np.ones(len(npeaks_hist))
I3_var = 0.4578*np.ones(len(npeaks_hist))

plt.plot(I1_var,npeaks_hist)
plt.plot(I2_var,npeaks_hist)
plt.plot(I3_var,npeaks_hist)
plt.plot(current_range,npeaks_hist, color='black')
plt.title('Spike Frequency vs External Current')
plt.xlabel("ExternalCurrent Values")
plt.ylabel("Frequency")
plt.show()
