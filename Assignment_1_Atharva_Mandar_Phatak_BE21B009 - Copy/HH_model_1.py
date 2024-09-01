# Name : Atharva Mandar Phatak
# Roll no : BE21B009
# BT6720 : Computational Assignment
# Given Code 

#Importing the necessary libraries 
import numpy as np
from math import exp
import matplotlib.pyplot as plt


#Setting the constant values
gkmax = 0.36
vk = -77
gnamax = 1.20
vna = 50
gl = 0.003
vl = -54.387
cm = 0.01

dt = 0.01
niter = 50000
t = 0.01*np.arange(0,50000,1)

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

#HH model 
def hh_model (cur_iter):

     
    for iteration in range(niter):
        global m,n,k,h,v;
        gna = gnamax*m**3*h
        gk = gkmax*n**4
        gtot = gna+gk+gl
        vinf = ((gna*vna+gk*vk+gl*vl) + cur_iter)/gtot
        tauv = cm/gtot

        v = vinf+(v-vinf)*exp(-dt/tauv)

        alpham = 0.1*(v+40)/(1-exp(-(v+40)/10))
        betam = 4*exp(-0.0556*(v+65))

        alphan = 0.01*(v+55)/(1-exp(-(v+55)/10))
        betan = 0.125*exp(-(v+65)/80)

        alphah = 0.07*exp(-0.05*(v+65))
        betah = 1/(1+exp(-0.1*(v+35)))

        taum = 1/(alpham+betam)
        tauh = 1/(alphah+betah)
        taun = 1/(alphan+betan)

        minf = alpham*taum
        hinf = alphah*tauh
        ninf = alphan*taun

        m = minf+(m-minf)*exp(-dt/taum)
        h = hinf+(h-hinf)*exp(-dt/tauh)
        n = ninf+(n-ninf)*exp(-dt/taun)

        vhist[iteration] = v
        mhist[iteration] = m
        hhist[iteration] = h
        nhist[iteration] = n

    
#Taking input from the user 
UserImpcur=float(input("Enter the value of current :"))
hh_model(UserImpcur)

#Plotting V vs t 
plt.plot(t,vhist,color='black')
plt.title("Voltage vs. time for current : "+str(UserImpcur)+" mA/mm^2")
plt.xlabel("Time (ms)")
plt.ylabel("Voltage (mV)")
plt.show()

#Plotting gatting variables vs time
plt.plot(t, mhist)
plt.plot(t, hhist)
plt.plot(t, nhist)
plt.title("Gating variables vs. time : "+str(UserImpcur)+" mA/mm^2")
plt.legend(['m','h','n'])
plt.xlabel("Time (ms)")
plt.ylabel("Gating variable probabilities")
plt.show()

#Plotting conductance vs time 
gna = gnamax*(mhist**3)	*hhist
gk = gkmax*nhist**4
plt.plot(t, gna,)
plt.plot(t, gk)
plt.legend(['gna','gk'])
plt.title("Conductance with time for : "+str(UserImpcur)+" mA/mm^2")
plt.xlabel("Time (ms)")
plt.ylabel("Conductance")
plt.show()
