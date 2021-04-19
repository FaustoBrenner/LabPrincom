function s = dtFMchirp(p,TW)

% DCHIRP generate a sampled chirp signal
% usage s = dchirp(TW,p)
% s : samples of a digital "chirp" signal
% 	exp(j(W/T)pi*t^2)  -T/2 <= t < T/2
% TW : time-bandwidth product
% p : sample at p times the Nyquist rate (W)

N = p*TW;
n = 0:N;
alpha = 1/(2*p*p*TW);
s = exp(j*2*pi*alpha*((n-.5*N).^2));
