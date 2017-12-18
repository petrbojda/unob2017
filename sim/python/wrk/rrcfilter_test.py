#!/usr/bin/env python

"""
This is a test bed script to plot a bitsteam with its
symbols shaped.
"""
import sys
sys.path.append("../../python")

import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
from siggens import train_pulse as gen
from utils import freqaxis_shape as ut
from filters import TF_pulse_shaping as flt

##################### Parameters ######################
f_sampl = 50e3 		# sampling frequency in kHz
T_int = 1 			# entire signal length in ms

##################### Simulation TAU = 1 ######################
t = np.arange(0,T_int,1/f_sampl)	# time axis
f = ut.freq_fr_time (t)				# frequency axis
tc = ut.corr_fr_time (t)			# correlation time axis
cd = np.array([1,1,1,0,1,1,1,1,0,1,0,1,1,0,1])	# code

tau = 1								# time acceleration factor
Tstr = 10e-3						# transmitted symbol interval
Ts = Tstr/tau						# Nyquist's symbol interval
td = 0.01							# initial delay of the sequence (time offset)

# Time Domain
a1 = gen.rcos_tr(t,Tstr,td + Tstr/2,cd,Ts,1.0)
b1 = gen.rect_tr(t,Tstr,0,td,cd)
# a2 = gen.rcos_tr(t,Tstr,td + Tstr/2,cd,Ts,0.5)
# a3 = gen.rcos_tr(t,Tstr,td + Tstr/2,cd,Ts,0.0)
# c  = gen.rect_tr(t,Tstr,0,td,cd)




# # Correlate processor
# A1_c = signal.correlate(a1,a1,'full')
# A2_c = signal.correlate(a2,a2,'full')
# A3_c = signal.correlate(a3,a3,'full')
# C1_c = signal.correlate( c,a1,'full')
# C2_c = signal.correlate( c,a2,'full')
# C3_c = signal.correlate( c,a3,'full')

# CC_c = signal.correlate( c, c,'full')

# Signal Frequency Spectrum
A1_fft = np.fft.fft(np.real(a1))
B1_fft = np.fft.fft(np.real(b1))

# RRC filter Transfer Function
RRC = flt.root_raised_cosine(f, Tstr, alpha=0.8)


##################### Plots ###########################
f1 = plt.figure(1)

#  Time domain
f1ax1 = f1.add_subplot(211)
f1ax1.plot(t, a1,'-g', label='$h_{rcos}(t), \\beta = 1.0$')
f1ax1.plot(t, b1,'-b', label='$h_{rect}(t)')
f1ax1.grid(True)
lgd = f1ax1.legend(loc='upper right', bbox_to_anchor=(1.12, 1.35))
plt.title('Pulse-shaped baseband signal', loc='left')
f1ax1.set_ylabel('Baseband - voltage')
f1ax1.axis([0, 0.15, -0.3, 1.3])

#  Frequency Domain
f1ax2 = f1.add_subplot(212)
f1ax2.plot(f, A1_fft,'-g', label='$H_{rcos}(f), \\beta = 1.0$')
f1ax2.plot(f, B1_fft,'-b', label='$H_{rect}(f)')
f1ax2.grid(True)
lgd = f1ax2.legend(loc='upper right', bbox_to_anchor=(1.05,1.15))
plt.title('Pulse-shaped Frequency Spectrum', loc='left')
f1ax2.set_ylabel('Baseband - magnitude')
f1ax2.axis([-500, 1000, -1400, 2500])


f2 = plt.figure(2)

#  RRC Filter Transfer Function and Signal Spectra
f2ax1 = f2.add_subplot(211)
f2ax1.plot(f, RRC,'-g', label='$H_{RRC}(f), \\alpha = 0.8$')
f2ax1.grid(True)
lgd = f2ax1.legend(loc='upper right', bbox_to_anchor=(1.05,1.15))
plt.title('RRC Filter  Transfer Function', loc='left')
f2ax1.set_ylabel('Baseband - voltage')
f2ax1.axis([-500, 1000, -0.14, 0.15])
plt.show()

