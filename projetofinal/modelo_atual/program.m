% Line of sight radar signal processor for Matlab
% Anil Thomas Maliyekkel
% Shannon Nicholas McGarr
% Jason Thomas Nearing
% Robert Wyatt Pickel
% 
% Elec 431 w/ Richard Baranuik
% December 16, 1995
% 
y = 1;                                    % yes
n = 0;                                    % no
c = 3e8;                                  % speed of light
T=7e-6;					  % length of burst in seconds
W=7e6;					  % bandwidth of burst (Hz)
p=2;					  % oversampling rate for burst
Np=5;				          % number of bursts 
z=205;					  % time between starts of bursts (microseconds) 
T_0=z*(0:(Np-1));                         % start times of each burst (microseconds)
g=ones(1,Np);                             % gain factor for each burst
T_window=[25,200];			  % start and recceived window (microseconds)
T_ref=0;				  % Referance time (microseconds)
fc =7000;				  % Center frequency of radar (MHz)
AN=1;					  % Noise scaling factor relative to stdev = 2
Rthres = 0.6;				  % Threshold for target determination
Vthres = 0.9;				  % Threshold for velocity determination
Vmul = 1.5;                               % Extra range for graphs 
Rmul = 1.2; 

% calculate theoretical limits on radar distance and velocity ranges 
maxrange = (T_window(2)*1e-6-T)/2*c/1000; 
minrange = T_window(1)*1e-6/2*c/1000;
maxvelocity = c/4/z/fc;     


% Ask user for options
velaliasing = input('Do you want to see velocity aliasing? ');
graphin = input('Do you want graphical input? ');

% If user wants graphical input
if graphin
% Initialize
  ranges = [];
  vels = [];

% Set up window used for input
  figure(1)
  clf
  hold on
  mr = maxrange*Rmul;
  mv = maxvelocity*Vmul;
  plot([minrange maxrange maxrange minrange minrange ], ...
       maxvelocity*[-1 -1 1 1 -1],'--')
  axis([0 mr -mv mv])
  title('Please enter up to 20 targets using mouse or click outside to continue')
  xlabel('range (km)')
  ylabel('velocity (m/s)')

% Loop for getting upto 20 target points 
% We stop getting new targets if the user clicks in the graph margins
  R = 0;
  V = 0;
  for k=1:20
    [R,V] = ginput(1);
    if R < 0 | R > mr | V < -mv | V > mv 
      break
    end
    plot(R,V,'o')
    ranges = [ranges R];
    vels = [vels V];
  end

% othersize get input from keyboard
else
  ranges = input('Enter range vector for up to twenty targets: ');
  vels = input('Enter correponsing velocity vector: ');
  if length(ranges) ~= length(vels)
    error('You need the same number of velocities and ranges')
  end
end

% Set all target amplitudes to one
amps=ones(size(ranges));

% Create chirp and return signal using radar.m 
chirp=dtFMchirp(p,T*W);                   
signal_in=radar(chirp,p*W/1e6,T_0,g,T_window,T_ref,fc,ranges,amps,vels);
[M,N]=size(signal_in);

% Add white noise (Gaussian) with std dev of 2 (twice amplitude of signal)
signal = signal_in + AN*sqrt(2)*randn(M,N);
signal = signal + AN*j*sqrt(2)*randn(M,N);

% Create matched filter for signal and process each return
h = conj(fliplr(chirp));
y = [];
for i=1:Np
  y(:,i)=conv(signal(:,i),h);
end

%%%%%%%%%%%%% RANGE %%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Select up to 30 peaks from output containing 
% at least 0.6 of theoretical maximum output for a single target
[Rpeaks,Rlocs]=pkpicker( abs(y(:,1)), Rthres*length(chirp), 30);

% Calculate peak strengths relative to perfect target
Rpeaknums = (Rpeaks / length(chirp));

% Calculate time delay for signal return and distance in km to target 
delay = (Rlocs-length(chirp))/(p*W)+T_window(1)*1e-6;
range = c/2*delay/1000;

%%%%%%%%%%%%% VELOCITY %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Select peaks of targets from all return bursts
yd=y(Rlocs,:);

% Initialize variables for velocity determination loop
fd = [];
velocity = [];
for k=1:length(Rlocs)

% Calculate dtft for signal oversampled several times
  [HV,WV] = dtft(yd(k,:),Np*64);

% If we are demonstrating aliasing in doppler shifts
% then the dtft with frequency axis changed to velocity
  if velaliasing
    figure(2)
    plot(c/2*WV/(z*1e-6)/2/pi/(fc*1e6),abs(HV));
    title(sprintf('Velocity from DTFT for target %d',k))
    xlabel('velocity (m/s)')
    ylabel('|H(v))|');
    pause(2); 
  end 

% Find location of peak in dtft
  [peakH,loc]=max(abs(HV));

% calculate doppler shift and velocity
  fd(k) = WV(loc)/(z*1e-6)/2/pi/(fc*1e6);
  velocity(k)=c/2*fd(k);
end


% Display ranges and velocities of found targets
range
velocity

% Display outputs on graph
figure(1)

% If we did not use graphical input graph must be created
if graphin == 0
  clf
  hold on
  mr = maxrange*Rmul;
  mv = maxvelocity*Vmul;
  plot([minrange maxrange maxrange minrange minrange ], ...
       maxvelocity*[-1 -1 1 1 -1],'--')
  axis([0 mr -mv mv])
  xlabel('range (km)')
  ylabel('velocity (m/s)')
  plot(ranges,vels,'o')
end

% Display targets and their peak number
title('o = real targets in, x = detected targets')
plot(range,velocity,'x')
for k=1:length(Rlocs)
  han=text(range(k)+.5,velocity(k),sprintf('%4.2g',Rpeaknums(k)));
  set(han,'FontSize',8)
  set(han,'Color',[1 0 1]);
end

