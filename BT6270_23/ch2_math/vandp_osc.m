% This is simulation code for Van Der Pol Oscilltor written as part of
% BT6270 - Computational Neuroscience Course.
% 
% The parameter mu here controls the dynamics of the oscillator. Any
% positive value of mu exhibits limit cycle oscillation.

% Equations: 
% Vander Pol Equation : dx^2/dt^2 + mu(x^2-1)dx/dt + x =0
% dx/dt=y; dy/dt=mu*(1-x^2)*y - x;


clear all; 
close all; 
clc;

niter = 500000;

x  = rand(1,1);%2;%0.1*rand - 0.5; % Initial Condition for x
dx =  0;

y  = 1 ;% 0;%0.1*rand - 0.5; % Initial Condition for y 
dy = 0;
dt=0.0001;

mu=0.05;  % For any positive values of mu the vander pol osc exhibit limit cycle oscillation.

% Solving the differential equations for dx/dt and dy/dt

    for iter = 1:niter
        dx = dt*(y);
        dy = dt*(-x+mu*(1-x^2)*y);
        x  = dx+ x;
        y=y+dy;
        xarr(iter)=x;
        yarr(iter)=y;
    end


% Plotting

% x(t) & y(t)

figure(1)
plotname = sprintf('Solution of van der Pol Equation with mu =%d', mu);
plot(1:niter, xarr,'b',1:niter, yarr,'r');
xlabel('Time t');
ylabel('Activity');
legend('x(t)','y(t)')
title(plotname)

% Plase Plane Plot
figure(2)
plot(xarr,yarr)
title('Phase plane plot')
xlabel('x');
ylabel('y');

