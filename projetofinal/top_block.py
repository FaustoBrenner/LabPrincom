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
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
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
        self.p = p = 10
        self.W = W = 2e3
        self.Tp = Tp = 0.5e-3
        self.N = N = p*Tp*W
        self.n = n = np.arange(0,N)
        self.alpha = alpha = 1/(2*p*p*Tp*W)
        self.z = z = 500e-3
        self.samp_rate = samp_rate = p*W
        self.chirp = chirp = np.exp(1j*2*np.pi*alpha*(n-0.5*N)**2)
        self.Np = Np = 5

        ##################################################
        # Blocks
        ##################################################
        self._z_range = Range(1e-3, 1, 1e-3, 500e-3, 200)
        self._z_win = RangeWidget(self._z_range, self.set_z, "z", "counter_slider", float)
        self.top_grid_layout.addWidget(self._z_win)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"Chirp", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(2):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_win)
        self.blocks_vector_source_x_0 = blocks.vector_source_c(chirp, True, 1, [])
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self._W_range = Range(1e3, 100e3, 1e3, 2e3, 200)
        self._W_win = RangeWidget(self._W_range, self.set_W, "W", "counter_slider", float)
        self.top_grid_layout.addWidget(self._W_win)
        self._Tp_range = Range(1e-5, 0.025, 1e-5, 0.5e-3, 200)
        self._Tp_win = RangeWidget(self._Tp_range, self.set_Tp, "Tp", "counter_slider", float)
        self.top_grid_layout.addWidget(self._Tp_win)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_throttle_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_p(self):
        return self.p

    def set_p(self, p):
        self.p = p
        self.set_samp_rate(self.p*self.W)
        self.set_alpha(1/(2*self.p*self.p*self.Tp*self.W))
        self.set_N(self.p*self.Tp*self.W)

    def get_W(self):
        return self.W

    def set_W(self, W):
        self.W = W
        self.set_samp_rate(self.p*self.W)
        self.set_alpha(1/(2*self.p*self.p*self.Tp*self.W))
        self.set_N(self.p*self.Tp*self.W)

    def get_Tp(self):
        return self.Tp

    def set_Tp(self, Tp):
        self.Tp = Tp
        self.set_alpha(1/(2*self.p*self.p*self.Tp*self.W))
        self.set_N(self.p*self.Tp*self.W)

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

    def get_alpha(self):
        return self.alpha

    def set_alpha(self, alpha):
        self.alpha = alpha
        self.set_chirp(np.exp(1j*2*np.pi*self.alpha*(self.n-0.5*self.N)**2))

    def get_z(self):
        return self.z

    def set_z(self, z):
        self.z = z

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_chirp(self):
        return self.chirp

    def set_chirp(self, chirp):
        self.chirp = chirp
        self.blocks_vector_source_x_0.set_data(self.chirp, [])

    def get_Np(self):
        return self.Np

    def set_Np(self, Np):
        self.Np = Np


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
