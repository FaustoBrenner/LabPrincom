filename ='C:\Users\faust\Pessoal\2020-1\LabPRINCOM\projetofinal\modelo_atual\output.bin';
output = read_complex_binary(filename);

filename ='C:\Users\faust\Pessoal\2020-1\LabPRINCOM\projetofinal\modelo_atual\signal_rx.bin';
signal_rx= read_complex_binary(filename);

filename ='C:\Users\faust\Pessoal\2020-1\LabPRINCOM\projetofinal\modelo_atual\chirp.bin';
chirp= read_complex_binary(filename);

filename ='C:\Users\faust\Pessoal\2020-1\LabPRINCOM\projetofinal\modelo_atual\signal_tx.bin';
signal_tx= read_complex_binary(filename);

c=1450;                     % velocidade do som na água
p=10;
W=2000;
T=25e-3;
z=0.5;
fc = 50e+3;

Rthres = 0.65;				  % Threshold para identificação do alvo
                              % ao menos 65% do retorno máximo teórico
Np=5;
n = length(output)/Np;
%y = reshape(output,n,Np);
y = output(1:round(n),1);

%%%%%%%%%%%%% RANGE %%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Identifica a localização dos picos no sinal de saída a partir do 
% threashold determinado
[Rpeaks,Rlocs]=pkpicker(abs(y(:,1)), Rthres*length(chirp), 30);

% Calcula o atraso de tempo dos retornos encontrados
delay = (Rlocs-length(chirp))/(p*W);
range = c/2*delay;
fprintf('%i objeto(s) detectado(s)\n', length(range))
for i=1:length(range)
    fprintf('    objeto %i -> %.2fm\n', i, range(i))
end


%%%%%%%%%%%%% VELOCITY %%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Selciona os picos encontrados na determinação do alcance
%yd=y(Rlocs,:);

% Inicializa as variáveis para o loop de determinação da velocidade
%fd = [];
%velocity = [];

%for k=1:length(Rlocs)

% Calcula a dtft para o sinal
%  [HV,WV] = dtft(yd(k,:),Np*64);

% Encontra o a localização dos picos na dtft
 % [peakH,loc]=max(abs(HV));

% Calcula a variação de frequência pelo efeito doppler e a correspondente
% velocidade
 % fd(k) = WV(loc)/(z)/2/pi/(fc);
 % velocity(k)= 3.6 * c/2*fd(k);
%end

%fprintf('Velocidades:/n')
%for i=1:length(range)
%    fprintf('    objeto %i -> %.2fm\n', i, range(i))
%end



figure
plot(abs(output(:,1)),'r')
title('Sinal após filtragem')


figure
plot(real(signal_rx(:,1)),'green')
title('Sinal recebido')

figure
plot(real(signal_tx(:,1)),'b')
title('Sinal transmitido')
