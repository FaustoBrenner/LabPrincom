function y = radar_adapted( x, fs, T_0, g, T_out, T_ref, fc, r, a )
%RADAR      simulate radar returns from a single pulse
%-----
%  Usage:
%    R = radar( X, Fs, T_0, G, T_out, T_ref, Fc, R, A, V )
%
%      X:      input pulse (vector containing one pulse for burst)
%      Fs:     sampling frequency of input pulse(s)      [in MHz]
%      T_0:    start time(s) of input pulse(s)         [microsec]
%      G:      complex gains; # pulses = length(g)
%      T_out:  2-vector [T_min,T_max] defines output
%                window delay times w.r.t. start of pulse
%      T_ref:  system "reference" time, needed to simulate
%                 burst returns. THIS IS THE "t=0" TIME !!!
%      Fc:     center freq. of the radar.                [in MHz]
%      R:      vector of ranges to target(s)         [kilometers]
%      A:      (complex) vector of target amplitudes
%      V:      vector of target velocities (optional)  [in m/sec]
%
%  note(1): VELOCITY in meters/sec !!!
%           distances in km, times in microsec, BW in MegaHz.

%  note(2): assumes each pulse is constant (complex) amplitude
%  note(3): will accommodate up to quadratic phase pulses
%  note(4): vector of ranges, R, allows DISTRIBUTED targets
%

%---------------------------------------------------------------
% copyright 1994, by C.S. Burrus, J.H. McClellan, A.V. Oppenheim,
% T.W. Parks, R.W. Schafer, & H.W. Schussler.  For use with the book
% "Computer-Based Exercises for Signal Processing Using MATLAB"
% (Prentice-Hall, 1994).
%---------------------------------------------------------------

J = sqrt(-1);
c = 0.3;         % velocity of light in km/microsec
r = r(:);   a = a(:);
[Mx, Nx] = size(x);
if Mx == 1
   old_Nx = Nx;   Mx = Nx;   Nx = 1;  x = x.';
end
if Nx ~= 1,    error('MATRIX x NOT ALLOWED !!!'),  end
g = g(:).';      %-- gains of each pulse in burst
delta_t = 1/fs;
T_p = Mx*delta_t;     % length of input pulse
t_x = (delta_t)*[0:(Mx-1)]';
x_ph = unwrap(angle(x));       %-- find phase modulation
q = polyfit( t_x, x_ph, 2 );   %-- assume LFM signal
xfit = polyval( q, t_x );
if (x_ph'*xfit)/norm(x_ph)/norm(xfit) < 0.99   %-- correlation coeff
   disp(' no quadratic phase match')
   %keyboard
end
%
%---  output matrix ---
%
t_y = [ T_out(1):delta_t:T_out(2) ]';  % output sampling times
Mr = length(t_y);  Nr = length(g);     % output samples in a matrix
y = zeros(Mr,Nr);
for  i = 1:length(r)
   ri = r(i);   
 for j = 1:length(g)
   tau = ri./(c/2);   tmax = tau + T_p;
   if tau >= T_out(2) | tmax <= T_out(1)
      disp('COMPLETELY OUT OF range window'),  ri=ri, i
   else
      t_in_pulse = t_y - tau;
      n_out = find( t_in_pulse >= 0  &  t_in_pulse < T_p );
      if tau < T_out(1)
         disp('BEFORE range window'),  ri,  end
      if tmax > T_out(2)
         disp('AFTER range window'),  ri,   end
      if length(n_out) < 1
         disp('NO OVERLAP ???'),  %keyboard
      else
%-------------------------------
 %keyboard
  y(n_out,j) = y(n_out,j) + a(i) * g(j) * ...
        [ exp( J*2*pi*2*fc*(-ri))]  ...
     .* [ exp( J*polyval(q,t_in_pulse(n_out)) )  ];
%-------------------------------
      end
   end
 end
end