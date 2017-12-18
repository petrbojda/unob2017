#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Baseband Generator
# Generated: Sun Dec 17 13:46:34 2017
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import prn
import sip
import sys


class baseband_generator(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Baseband Generator")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Baseband Generator")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "baseband_generator")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.chip_rate = chip_rate = 2e6
        self.sps = sps = 4
        self.samp_rate = samp_rate = 12*chip_rate
        self.init_register = init_register = [1,1,1,1]
        self.feedback = feedback = [0,0,1,1]
        self.excess_bw = excess_bw = 0.35

        ##################################################
        # Blocks
        ##################################################
        self.root_raised_cosine_filter_0 = filter.fir_filter_ccf(1, firdes.root_raised_cosine(
        	1, samp_rate, chip_rate, 0.9, 32))
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
        	1024/4, #size
        	samp_rate, #samp_rate
        	'SSRG qpsk baseband generator', #name
        	5 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(-1.2, 1.3)
        
        self.qtgui_time_sink_x_0_0.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_AUTO, qtgui.TRIG_SLOPE_POS, -0.75, 0, 1, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0.enable_grid(True)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0_0.disable_legend()
        
        labels = ['clock', 'ssrg_0, init[1111]', 'qpsk  i, square', 'qpsk q, square', 'Magnit',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["red", "blue", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(5):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	1024/4, #size
        	samp_rate, #samp_rate
        	'SSRG baseband generator', #name
        	5 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1.2, 1.3)
        
        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_AUTO, qtgui.TRIG_SLOPE_POS, -0.75, 0, 1, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(True)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0.disable_legend()
        
        labels = ['clock', 'ssrg_0, init[1111]', 'baseband i, square', 'baseband i, RRC filtered', 'Magnit',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["red", "blue", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(5):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.prn_ssrg_qpsk_fc_0 = prn.ssrg_qpsk_fc((init_register), (feedback), 2, -1)
        self.prn_ssrg_ff_0 = prn.ssrg_ff((init_register), (feedback),0.5, -1.2)
        self.prn_ssrg_bpsk_fc_0 = prn.ssrg_bpsk_fc((init_register), (feedback), 2, -1)
        self.chiprate_generator_0 = analog.sig_source_f(samp_rate, analog.GR_SQR_WAVE, chip_rate, 0.5, -0.5)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_complex_to_real_0_1 = blocks.complex_to_real(1)
        self.blocks_complex_to_real_0_0 = blocks.complex_to_real(1)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.blocks_complex_to_mag_0_0 = blocks.complex_to_mag(1)
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(1)
        self.blocks_complex_to_imag_0 = blocks.complex_to_imag(1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_complex_to_imag_0, 0), (self.qtgui_time_sink_x_0_0, 3))    
        self.connect((self.blocks_complex_to_mag_0, 0), (self.qtgui_time_sink_x_0_0, 4))    
        self.connect((self.blocks_complex_to_mag_0_0, 0), (self.qtgui_time_sink_x_0, 4))    
        self.connect((self.blocks_complex_to_real_0, 0), (self.qtgui_time_sink_x_0, 2))    
        self.connect((self.blocks_complex_to_real_0_0, 0), (self.qtgui_time_sink_x_0, 3))    
        self.connect((self.blocks_complex_to_real_0_1, 0), (self.qtgui_time_sink_x_0_0, 2))    
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_time_sink_x_0, 0))    
        self.connect((self.chiprate_generator_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.chiprate_generator_0, 0), (self.prn_ssrg_bpsk_fc_0, 0))    
        self.connect((self.chiprate_generator_0, 0), (self.prn_ssrg_ff_0, 0))    
        self.connect((self.chiprate_generator_0, 0), (self.prn_ssrg_qpsk_fc_0, 0))    
        self.connect((self.chiprate_generator_0, 0), (self.qtgui_time_sink_x_0_0, 0))    
        self.connect((self.prn_ssrg_bpsk_fc_0, 0), (self.blocks_complex_to_real_0, 0))    
        self.connect((self.prn_ssrg_bpsk_fc_0, 0), (self.root_raised_cosine_filter_0, 0))    
        self.connect((self.prn_ssrg_ff_0, 0), (self.qtgui_time_sink_x_0, 1))    
        self.connect((self.prn_ssrg_ff_0, 0), (self.qtgui_time_sink_x_0_0, 1))    
        self.connect((self.prn_ssrg_qpsk_fc_0, 0), (self.blocks_complex_to_imag_0, 0))    
        self.connect((self.prn_ssrg_qpsk_fc_0, 0), (self.blocks_complex_to_mag_0, 0))    
        self.connect((self.prn_ssrg_qpsk_fc_0, 0), (self.blocks_complex_to_real_0_1, 0))    
        self.connect((self.root_raised_cosine_filter_0, 0), (self.blocks_complex_to_mag_0_0, 0))    
        self.connect((self.root_raised_cosine_filter_0, 0), (self.blocks_complex_to_real_0_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "baseband_generator")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_chip_rate(self):
        return self.chip_rate

    def set_chip_rate(self, chip_rate):
        self.chip_rate = chip_rate
        self.set_samp_rate(12*self.chip_rate)
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(1, self.samp_rate, self.chip_rate, 0.9, 32))
        self.chiprate_generator_0.set_frequency(self.chip_rate)

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(1, self.samp_rate, self.chip_rate, 0.9, 32))
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.chiprate_generator_0.set_sampling_freq(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_init_register(self):
        return self.init_register

    def set_init_register(self, init_register):
        self.init_register = init_register

    def get_feedback(self):
        return self.feedback

    def set_feedback(self, feedback):
        self.feedback = feedback

    def get_excess_bw(self):
        return self.excess_bw

    def set_excess_bw(self, excess_bw):
        self.excess_bw = excess_bw


def main(top_block_cls=baseband_generator, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
