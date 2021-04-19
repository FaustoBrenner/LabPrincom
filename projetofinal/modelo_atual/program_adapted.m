
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

ranges = [((maxrange+minrange)/2)];

% Set all target amplitudes to one
amps=ones(size(ranges));

% Create chirp and return signal using radar.m 
chirp=dtFMchirp(p,T*W);                   
signal_in=radar_adapted(chirp,p*W/1e6,T_0,g,T_window,T_ref,fc,ranges,amps);
[M,N]=size(signal_in);

% Add white noise (Gaussian) with std dev of 2 (twice amplitude of signal)
signal = signal_in + AN*sqrt(2)*randn(M,N);
signal = signal + AN*1i*sqrt(2)*randn(M,N);

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

% Display ranges and velocities of found targets
range

% Display outputs on graph
%figure(1)

%clf
%hold on
%mr = maxrange*Rmul;
%mv = maxvelocity*Vmul;
%plot([minrange maxrange maxrange minrange minrange ], ...
%     maxvelocity*[-1 -1 1 1 -1],'--')
%axis([0 mr])
%xlabel('range (km)')
%plot(ranges,'o')


% Display targets and their peak number
%title('o = real targets in, x = detected targets')
%plot(range,velocity,'x')
%for k=1:length(Rlocs)
%  han=text(range(k)+.5,velocity(k),sprintf('%4.2g',Rpeaknums(k)));
%  set(han,'FontSize',8)
%  set(han,'Color',[1 0 1]);
%end
