clear all
close all
[filename1,hfile1]=uigetfile({'./*.csv',},...
 'Select Data File 1');

amu_to_kg = 1.66e-27;
mass = 40*amu_to_kg;             %kg
MM = 40;               %gmol^-1
density = 1.4e6/1000;            %kgm^-3      
Na = 6.022e23;      %mol^-1

atomicdensity=Na*density/MM;
Kb=1.3806488e-23;                   %JK^-1
T=297;                              %K

data		= importdata(fullfile(hfile1, filename1));

N = length(data.data(5,:));
fs=100; %s^-1
dt=1/100;
t=(0:N-1)/fs;
xdft=abs(fft(data.data(5,:)));

freq=(0:N-1)*(fs/N);   %s^-1


DOS = .5 * mass .* xdft .* atomicdensity / Kb / T ; 

plot(freq.*2*pi,DOS); grid on;
title('DOS using FFT')
xlabel('Frequency (rad s^-1)')
ylabel('DOS (counts s m^-3)')