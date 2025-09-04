clear
close all

M1 = 40; % kg
M2 = 250; % kg

B = 500; % Ns/m
K1 = 20000; % N/m
K2 = 10000; % N/m

w = logspace(0,3,400);
%s = linspace(-50, 50, 102);
s = 1i*w;

teller = (s*B + K2)*K1;
nevner = (M1*s.^2 + B*s + K2 + K1).*(M2*s.^2 + B*s + K2) - (B*s + K2).^2;

H = teller ./ nevner;
loglog(w, abs(H))
%plot(s, H)
grid on;