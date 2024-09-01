%Ext input = complex sinusoid



niter = 200;
dt = 0.01;
mu = 3;
alfa = -1;
beta = 5;
%omega of the oscillator = 1 + beta*r*r; r = 1, therefore omega = 1+beta
b = alfa + 1i*beta;
lam = 1;

A = 0;
omega = 5;

nomega = 2;
omegamin = 1;
omegamax = 40;
step = (omegamax - omegamin)/nomega;

zarr = zeros(niter, 1);
omeg_arr = zeros(nomega, 1);
amp_arr = zeros(nomega, 1);
omeg_arr = omegamin + step*[1:nomega];

for ii = 1:nomega,
    omega = omeg_arr(ii);
    z = 10 + 2*1i;
for j = 1:niter,
%    dz =dt*((lam+1i)*z + b*z*z*z' + A*exp(1i*omega*j*dt));
     dz = dt*(1i*omega*z + (1 - abs(z)*abs(z))*z);
    z = z + dz;
    zarr(j) = z;
end

[amp, ind] = max(real(zarr(niter/2:niter)));
amp_arr(ii) = amp;
figure(1)
t = [1:niter]*dt;
plot(t, real(zarr))


figure(2)
plot(zarr)

% figure(3)
%[respamp, freq] = dft(real(zarr), 1/dt);
% plot(2*pi*freq, respamp)
% omega_intr = beta + 1;
% str = ['Intrinsic freq = ', num2str(omega_intr),...
%     ';  extrin freq = ', num2str(omega)];
% title(str)
pause(0.1)

end

t = [1:niter]*dt;

% 
% figure(2)
% plot(omeg_arr, amp_arr);
% xlabel('Frequency of forcing function');
% ylabel('Response amplitude')

