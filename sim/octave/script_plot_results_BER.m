% Script reads files recorded by GNU radio using "File Sink".
% Two different files are stored for exactly the same signal. One 
% in complex form and one in real form. Script then compares these two 
% in different plots.

%% Reading
clear;
clc;
f_sampling = 32e6;
n_samples = 5e2;
t = 0:1/f_sampling:n_samples / f_sampling;


Rx_data = read_float_binary ('Rx.bin',n_samples +1);
Tx_data = read_float_binary ('Tx.bin',n_samples +1);



%% Plot

h1 = figure(1);title('Comparing Received Data');

subplot(2,1,1); plot(t*1e6,Rx_data,'-r'); grid on;
ylabel('Rx');
subplot(2,1,2); plot(t*1e6,Tx_data,'-k'); grid on;
ylabel('Tx'); xlabel('time [micro seconds]');

%print(h1,'-deps','-color','DME_interr_03.eps');


%figure(2);
%subplot(2,1,1);title("Complex Reading - REAL");
%plot(t,abs(v_interr)); grid on;
%subplot(2,1,2);title("Complex Reading - IMAG");
%plot(t,imag(v_reply)); grid on;

%figure(3);
%subplot(2,1,1);title("Complex Reading - REAL");
%plot(t,real(v_ADSB)); grid on;
%subplot(2,1,2);title("Complex Reading - IMAG");
%plot(t,imag(v_ADSB)); grid on;

%figure(1);
%title("Complex Reading - REAL");
%plot(t,abs(v_complex)); grid on;

