import numpy as np
import matplotlib.pyplot as plt
Dt = 0.01               # timestep Delta t
X1_start = 0.5            
Y1_start = 0.5           

X2_start = 0.5                    
Y2_start =0.5           

t_start = 0             # starttime
t_end = 60              # endtime
n_steps = int(round((t_end-t_start)/Dt))    # number of timesteps

#Parameters
w12=-0.5
w21=-0.5
w1=5
w2=5

X1_arr = np.zeros(n_steps + 1)   # create an array of zeros for Y
Y1_arr = np.zeros(n_steps + 1)   # create an array of zeros for Y
X2_arr = np.zeros(n_steps + 1)   # create an array of zeros for Y
Y2_arr = np.zeros(n_steps + 1)   # create an array of zeros for Y

t_arr = np.zeros(n_steps + 1)   # create an array of zeros for t

t_arr[0] = t_start              # add starttime to array
X1_arr[0] = X1_start              # add initial value of Y to array
X2_arr[0] = X2_start
Y1_arr[0] = Y1_start
Y2_arr[0] = Y2_start              

# Euler's method
for i in range (1, n_steps + 1):  

   X1 = X1_arr[i-1]
   Y1 = X1_arr[i-1]
   X2 = X1_arr[i-1]
   Y2 = X1_arr[i-1]
   t = t_arr[i-1]
   
   dX1dt = (1-(X1**2)+(Y1**2))*X1+((w21*X2)-(w1*Y1))
   print("dX1dt",dX1dt)
   dY1dt = (1-(X1**2)+(Y1**2))*Y1+(w1*X1)
   dX2dt = (1-(X2**2)+(Y2**2))*X2+((w12*X1)-(w2*Y2))
   dY2dt = (1-(X2**2)+(Y2**2))*Y2+(w2*X2)

   
   X1_arr[i] = X1 + Dt*(dX1dt)  # calc. Y at next timestep,add to array
   print("x1",X1)
   Y1_arr[i] = Y1 + Dt*(dY1dt)
   X2_arr[i] = X2 + Dt*(dX2dt)
   Y2_arr[i] = Y2 + Dt*(dY2dt)
   t_arr[i] = t + Dt       # add new value of t to array

print(X1_arr)
print("#####")
print(X2_arr)
print("#####")
print(Y1_arr)


# plotting the result
fig = plt.figure()                                  # create figure
plt.plot(t_arr, X1_arr, linewidth = 4, label = 'X1')    # plot Y to t 
plt.plot(t_arr, X2_arr, linewidth = 4, label = 'X2')    # plot P to t

plt.title('Title', fontsize = 12)    # add some title to your plot
plt.xlabel('t (in seconds)', fontsize = 12)
plt.ylabel('Y(t), P(t)', fontsize = 12)
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)

plt.grid(True)                        # show grid
#plt.axis([t_start, t_end, 0, 50])     # show axes measures
plt.legend()
plt.show()