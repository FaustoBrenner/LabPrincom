#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# GNU Radio version: 3.7.13.5
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
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import fft
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import numpy as np
import sip
import sys
from gnuradio import qtgui


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        qtgui.util.check_set_qss()
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

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.z = z = 0.2
        self.p = p = 10
        self.W = W = 2e3
        self.c = c = 1450
        self.Tp = Tp = 0.025
        self.N = N = p*z*W
        self.n = n = np.arange(0,N)
        self.min_range = min_range = (Tp)*c/2
        self.max_range = max_range = (z-Tp)/2*c
        self.alpha = alpha = 1/(2*p*p*z*W)
        self.samp_rate = samp_rate = p*W
        self.fc = fc = 50e3
        self.chirp = chirp = np.exp(1j*2*np.pi*alpha*(n-0.5*N)**2)
        self.R3 = R3 = max_range-min_range
        self.R2 = R2 = 85
        self.R1 = R1 = 60
        self.Np = Np = 5
        self.AN = AN = 2

        ##################################################
        # Blocks
        ##################################################
        self._R1_range = Range(min_range, max_range, 0.05, 60, 200)
        self._R1_win = RangeWidget(self._R1_range, self.set_R1, "R1", "counter_slider", float)
        self.top_grid_layout.addWidget(self._R1_win)
        self._z_range = Range(0.2, 1.45, 0.05, 0.2, 200)
        self._z_win = RangeWidget(self._z_range, self.set_z, "z", "counter_slider", float)
        self.top_grid_layout.addWidget(self._z_win)
        self.qtgui_vector_sink_f_0 = qtgui.vector_sink_f(
            int(N*Np),
            0,
            1.0,
            "x-Axis",
            "y-Axis",
            "",
            1 # Number of inputs
        )
        self.qtgui_vector_sink_f_0.set_update_time(0.10)
        self.qtgui_vector_sink_f_0.set_y_axis(-140, 10)
        self.qtgui_vector_sink_f_0.enable_autoscale(False)
        self.qtgui_vector_sink_f_0.enable_grid(False)
        self.qtgui_vector_sink_f_0.set_x_axis_units("")
        self.qtgui_vector_sink_f_0.set_y_axis_units("")
        self.qtgui_vector_sink_f_0.set_ref_level(0)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_vector_sink_f_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_vector_sink_f_0.set_line_label(i, labels[i])
            self.qtgui_vector_sink_f_0.set_line_width(i, widths[i])
            self.qtgui_vector_sink_f_0.set_line_color(i, colors[i])
            self.qtgui_vector_sink_f_0.set_line_alpha(i, alphas[i])

        self._qtgui_vector_sink_f_0_win = sip.wrapinstance(self.qtgui_vector_sink_f_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_vector_sink_f_0_win)
        self.qtgui_freq_sink_x_0_0_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"RX", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0_0.enable_autoscale(True)
        self.qtgui_freq_sink_x_0_0_0.enable_grid(True)
        self.qtgui_freq_sink_x_0_0_0.set_fft_average(0.05)
        self.qtgui_freq_sink_x_0_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_0_0_win)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"TX", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0.enable_autoscale(True)
        self.qtgui_freq_sink_x_0_0.enable_grid(True)
        self.qtgui_freq_sink_x_0_0.set_fft_average(0.05)
        self.qtgui_freq_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_0_win)
        self.fft_vxx_0_0 = fft.fft_vcc(int(N*Np), True, (window.blackmanharris(1024)), True, 1)
        self.fft_vxx_0 = fft.fft_vcc(int(N*Np), True, (window.blackmanharris(1024)), True, 1)
        self.blocks_vector_source_x_0 = blocks.vector_source_c(np.tile(chirp,Np), False, 1, [])
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_sub_xx_0 = blocks.sub_cc(int(N*Np))
        self.blocks_stream_to_vector_1 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, int(N*Np))
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, int(N*Np))
        self.blocks_nlog10_ff_0 = blocks.nlog10_ff(1, int(N*Np), 0)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, int(2*R1/(c/samp_rate)) )
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(int(N*Np))
        self._R3_range = Range(min_range, max_range, 0.05, max_range-min_range, 200)
        self._R3_win = RangeWidget(self._R3_range, self.set_R3, "R3", "counter_slider", float)
        self.top_grid_layout.addWidget(self._R3_win)
        self._R2_range = Range(min_range, max_range, 0.05, 85, 200)
        self._R2_win = RangeWidget(self._R2_range, self.set_R2, "R2", "counter_slider", float)
        self.top_grid_layout.addWidget(self._R2_win)
        self._AN_range = Range(0, 7, 0.5, 2, 200)
        self._AN_win = RangeWidget(self._AN_range, self.set_AN, "AN", "counter_slider", float)
        self.top_grid_layout.addWidget(self._AN_win)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_complex_to_mag_0, 0), (self.blocks_nlog10_ff_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.qtgui_freq_sink_x_0_0_0, 0))
        self.connect((self.blocks_nlog10_ff_0, 0), (self.qtgui_vector_sink_f_0, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vxx_0, 0))
        self.connect((self.blocks_stream_to_vector_1, 0), (self.fft_vxx_0_0, 0))
        self.connect((self.blocks_sub_xx_0, 0), (self.blocks_complex_to_mag_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_stream_to_vector_1, 0))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_freq_sink_x_0_0, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.fft_vxx_0, 0), (self.blocks_sub_xx_0, 1))
        self.connect((self.fft_vxx_0_0, 0), (self.blocks_sub_xx_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_z(self):
        return self.z

    def set_z(self, z):
        self.z = z
        self.set_max_range((self.z-self.Tp)/2*self.c)
        self.set_N(self.p*self.z*self.W)
        self.set_alpha(1/(2*self.p*self.p*self.z*self.W))

    def get_p(self):
        return self.p

    def set_p(self, p):
        self.p = p
        self.set_samp_rate(self.p*self.W)
        self.set_N(self.p*self.z*self.W)
        self.set_alpha(1/(2*self.p*self.p*self.z*self.W))

    def get_W(self):
        return self.W

    def set_W(self, W):
        self.W = W
        self.set_samp_rate(self.p*self.W)
        self.set_N(self.p*self.z*self.W)
        self.set_alpha(1/(2*self.p*self.p*self.z*self.W))

    def get_c(self):
        return self.c

    def set_c(self, c):
        self.c = c
        self.set_min_range((self.Tp)*self.c/2)
        self.set_max_range((self.z-self.Tp)/2*self.c)
        self.blocks_delay_0.set_dly(int(2*self.R1/(self.c/self.samp_rate)) )

    def get_Tp(self):
        return self.Tp

    def set_Tp(self, Tp):
        self.Tp = Tp
        self.set_min_range((self.Tp)*self.c/2)
        self.set_max_range((self.z-self.Tp)/2*self.c)

    def get_N(self):
        return self.N

    def set_N(self, N):
        self.N = N
        self.set_chirp(np.exp(1j*2*np.pi*self.alpha*(self.n-0.5*self.N)**2))
        self.set_n(np.arange(0,self.N))

    def get_n(self):
        return self.n

    def set_n(self, n):
        self.n = n
        self.set_chirp(np.exp(1j*2*np.pi*self.alpha*(self.n-0.5*self.N)**2))

    def get_min_range(self):
        return self.min_range

    def set_min_range(self, min_range):
        self.min_range = min_range
        self.set_R3(self.max_range-self.min_range)

    def get_max_range(self):
        return self.max_range

    def set_max_range(self, max_range):
        self.max_range = max_range
        self.set_R3(self.max_range-self.min_range)

    def get_alpha(self):
        return self.alpha

    def set_alpha(self, alpha):
        self.alpha = alpha
        self.set_chirp(np.exp(1j*2*np.pi*self.alpha*(self.n-0.5*self.N)**2))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_freq_sink_x_0_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.blocks_delay_0.set_dly(int(2*self.R1/(self.c/self.samp_rate)) )

    def get_fc(self):
        return self.fc

    def set_fc(self, fc):
        self.fc = fc

    def get_chirp(self):
        return self.chirp

    def set_chirp(self, chirp):
        self.chirp = chirp
        self.blocks_vector_source_x_0.set_data(np.tile(self.chirp,self.Np), [])

    def get_R3(self):
        return self.R3

    def set_R3(self, R3):
        self.R3 = R3

    def get_R2(self):
        return self.R2

    def set_R2(self, R2):
        self.R2 = R2

    def get_R1(self):
        return self.R1

    def set_R1(self, R1):
        self.R1 = R1
        self.blocks_delay_0.set_dly(int(2*self.R1/(self.c/self.samp_rate)) )

    def get_Np(self):
        return self.Np

    def set_Np(self, Np):
        self.Np = Np
        self.blocks_vector_source_x_0.set_data(np.tile(self.chirp,self.Np), [])

    def get_AN(self):
        return self.AN

    def set_AN(self, AN):
        self.AN = AN


def main(top_block_cls=top_block, options=None):

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
