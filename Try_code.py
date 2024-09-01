# Shree
import numpy as np

k = 1
istep = 0.01
ImpCur = np.arange(0, 0.61, 0.01)  # Applied Current ?

print(ImpCur)

gkmax = 0.36
vk = -77
gnamax = 1.20
vna = 50
gl = 0.003
vl = -54.387
cm = .01
dt = 0.01
niter = 50000

t = []

# An array t consisting of i*t
for i in range(1, niter):
    t.append(i * dt)

iapp = ImpCur * (np.ones(niter))

print(iapp)

v = -64.9964
m = 0.0530
h = 0.5960
n = 0.3177
