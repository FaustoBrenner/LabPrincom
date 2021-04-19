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
from gnuradio import analog
from gnuradio import blocks
from gnuradio import channels
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import epy_block_0
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
        self.C_1 = C_1 = np.array([0.0000, 0.0001, 0.0002, 0.0001, -0.0000, -0.0001, -0.0002, -0.0002, 0.0000, 0.0002, 0.0003, 0.0002, -0.0000, -0.0003, -0.0005, -0.0004, 0.0000, 0.0005, 0.0008, 0.0007, -0.0000, -0.0009, -0.0015, -0.0013, 0.0000, 0.0019, 0.0033, 0.0030, -0.0000, -0.0051, -0.0099, -0.0101, 0.0000, 0.0255, 0.0693, 0.1307, 0.2041, 0.2800, 0.3465, 0.3921,0.4082, 0.3921, 0.3465, 0.2800, 0.2041, 0.1307, 0.0693, 0.0255, 0.0000,-0.0101, -0.0099, -0.0051, -0.0000, 0.0030, 0.0033, 0.0019, 0.0000, -0.0013, -0.0015, -0.0009, -0.0000, 0.0007, 0.0008, 0.0005, 0.0000, -0.0004, -0.0005, -0.0003, -0.0000, 0.0002, 0.0003, 0.0002, 0.0000, -0.0002, -0.0002, -0.0001, -0.0000, 0.0001, 0.0002, 0.0001,0.0000])/0.4082
        self.samp_rate = samp_rate = 10000
        self.Sigma = Sigma = 0
        self.R_RZ = R_RZ = 4*[1]+4*[0]
        self.R_NRZ = R_NRZ = 8*[1]
        self.NPTS = NPTS = 8
        self.Iterp_rate = Iterp_rate = len(C_1)
        self.C_3 = C_3 = np.array([0.0000, 0.0071, 0.0137, 0.0186, 0.0209, 0.0201,0.0160, 0.0090, -0.0000, -0.0098, -0.0188, -0.0257, -0.0290, -0.0281, -0.0225, -0.0128, 0.0000, 0.0141, 0.0273, 0.0377,0.0431, 0.0421, 0.0342, 0.0197, -0.0000, -0.0226, -0.0448, -0.0633, -0.0746, -0.0754, -0.0637, -0.0384, 0.0000, 0.0496,0.1071, 0.1682, 0.2279, 0.2810, 0.3229, 0.3496, 0.3588,0.3496, 0.3229, 0.2810, 0.2279, 0.1682, 0.1071, 0.0496,0.0000, -0.0384, -0.0637, -0.0754, -0.0746, -0.0633, -0.0448, -0.0226, -0.0000, 0.0197, 0.0342, 0.0421, 0.0431, 0.0377,0.0273, 0.0141, 0.0000, -0.0128, -0.0225, -0.0281, -0.0290, -0.0257, -0.0188, -0.0098, -0.0000, 0.0090, 0.0160, 0.0201,0.0209, 0.0186, 0.0137, 0.0071, 0.0000])/0.3588
        self.C_2 = C_2 = np.array([0.0000, -0.0001, -0.0003, -0.0007, -0.0010, -0.0012, -0.0011, -0.0007, 0.0000, 0.0008, 0.0016, 0.0021, 0.0022,0.0018, 0.0010, 0.0003, 0.0000, 0.0004, 0.0018, 0.0040,0.0065, 0.0084, 0.0086, 0.0060, -0.0000, -0.0096, -0.0218, -0.0347, -0.0454, -0.0504, -0.0463, -0.0301, 0.0000, 0.0438,0.0992, 0.1621, 0.2269, 0.2868, 0.3353, 0.3670, 0.3780,0.3670, 0.3353, 0.2868, 0.2269, 0.1621, 0.0992, 0.0438,0.0000, -0.0301, -0.0463, -0.0504, -0.0454, -0.0347, -0.0218, -0.0096, -0.0000, 0.0060, 0.0086, 0.0084, 0.0065, 0.0040,0.0018, 0.0004, 0.0000, 0.0003, 0.0010, 0.0018, 0.0022,0.0021, 0.0016, 0.0008, 0.0000, -0.0007, -0.0011, -0.0012, -0.0010, -0.0007, -0.0003, -0.0001, 0.0000])/0.3780

        ##################################################
        # Blocks
        ##################################################
        self._Sigma_range = Range(0, 2, 0.02, 0, 200)
        self._Sigma_win = RangeWidget(self._Sigma_range, self.set_Sigma, "Sigma", "counter_slider", float)
        self.top_grid_layout.addWidget(self._Sigma_win, 3, 0, 1, 3)
        for r in range(3, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_2 = qtgui.time_sink_f(
        	81, #size
        	samp_rate*NPTS*8, #samp_rate
        	"Diagrama de olho", #name
        	10 #number of inputs
        )
        self.qtgui_time_sink_x_0_2.set_update_time(0.10)
        self.qtgui_time_sink_x_0_2.set_y_axis(-1.25, 1.25)

        self.qtgui_time_sink_x_0_2.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_2.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_2.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_2.enable_autoscale(False)
        self.qtgui_time_sink_x_0_2.enable_grid(False)
        self.qtgui_time_sink_x_0_2.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_2.enable_control_panel(False)
        self.qtgui_time_sink_x_0_2.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_2.disable_legend()

        labels = ['Cod Polar', 'Pulsos TX', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["black", "black", "black", "black", "black",
                  "black", "black", "black", "black", "black"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(10):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_2.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_2.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_2.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_2.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_2.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_2.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_2.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_2_win = sip.wrapinstance(self.qtgui_time_sink_x_0_2.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_2_win, 1, 1, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_1_1 = qtgui.time_sink_f(
        	512, #size
        	samp_rate, #samp_rate
        	"Mensagens", #name
        	3 #number of inputs
        )
        self.qtgui_time_sink_x_0_1_1.set_update_time(0.10)
        self.qtgui_time_sink_x_0_1_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_1_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_1_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_1_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_1_1.enable_autoscale(False)
        self.qtgui_time_sink_x_0_1_1.enable_grid(False)
        self.qtgui_time_sink_x_0_1_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_1_1.enable_control_panel(False)
        self.qtgui_time_sink_x_0_1_1.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_1_1.disable_legend()

        labels = ['Recuperada', 'Original', 'Erro', '', '',
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

        for i in xrange(3):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_1_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_1_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_1_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_1_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_1_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_1_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_1_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_1_1_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_1_1_win, 1, 2, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_1 = qtgui.time_sink_f(
        	32, #size
        	samp_rate*NPTS, #samp_rate
        	"Bits Decodificados", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_0_1.set_update_time(0.10)
        self.qtgui_time_sink_x_0_1.set_y_axis(-0.25, 1.25)

        self.qtgui_time_sink_x_0_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_1.enable_autoscale(False)
        self.qtgui_time_sink_x_0_1.enable_grid(False)
        self.qtgui_time_sink_x_0_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_1.enable_control_panel(False)
        self.qtgui_time_sink_x_0_1.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_1.disable_legend()

        labels = ['RX', 'TX', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [0, 0, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [0, 0, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_1_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_1_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
        	128, #size
        	samp_rate*NPTS*8, #samp_rate
        	"Pulso Amostragem e Pulso RX", #name
        	3 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(-1.25, 1.25)

        self.qtgui_time_sink_x_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_0.disable_legend()

        labels = ['Pulso RX', 'Amostrador', 'Amostrado', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 0, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, 0, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(3):
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
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_win, 0, 2, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	128, #size
        	samp_rate*NPTS*Iterp_rate, #samp_rate
        	"Cod. Polar e Pulso TX", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1.25, 1.25)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['Cod Polar', 'Pulsos TX', '', '', '',
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
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_histogram_sink_x_0 = qtgui.histogram_sink_f(
        	2048,
        	300,
                -2,
                2,
        	"Amostras RX",
        	1
        )

        self.qtgui_histogram_sink_x_0.set_update_time(0.10)
        self.qtgui_histogram_sink_x_0.enable_autoscale(True)
        self.qtgui_histogram_sink_x_0.enable_accumulate(True)
        self.qtgui_histogram_sink_x_0.enable_grid(False)
        self.qtgui_histogram_sink_x_0.enable_axis_labels(True)

        if not True:
          self.qtgui_histogram_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_histogram_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_histogram_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_histogram_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_histogram_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_histogram_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_histogram_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_histogram_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_histogram_sink_x_0_win = sip.wrapinstance(self.qtgui_histogram_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_histogram_sink_x_0_win, 2, 0, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_f(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate*NPTS*8, #bw
        	"Espectros", #name
        	2 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()

        if "float" == "float" or "float" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['TX', 'RX', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.interp_fir_filter_xxx_0_0 = filter.interp_fir_filter_fff(Iterp_rate, (C_1))
        self.interp_fir_filter_xxx_0_0.declare_sample_delay(0)
        self.interp_fir_filter_xxx_0 = filter.interp_fir_filter_fff(Iterp_rate, (1*[1]+(Iterp_rate -1)*[0]))
        self.interp_fir_filter_xxx_0.declare_sample_delay(0)
        self.fir_filter_xxx_0 = filter.fir_filter_fff(Iterp_rate, (Iterp_rate*[1]))
        self.fir_filter_xxx_0.declare_sample_delay(0)
        self.epy_block_0 = epy_block_0.blk(passo=1)
        self.channels_quantizer_0 = channels.quantizer(NPTS)
        self.blocks_unpack_k_bits_bb_0 = blocks.unpack_k_bits_bb(NPTS)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_sub_xx_1 = blocks.sub_ff(1)
        self.blocks_pack_k_bits_bb_0 = blocks.pack_k_bits_bb(NPTS)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff((0.5, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((2, ))
        self.blocks_float_to_char_0_0 = blocks.float_to_char(1, 1)
        self.blocks_float_to_char_0 = blocks.float_to_char(1, 128)
        self.blocks_delay_2_4 = blocks.delay(gr.sizeof_float*1, 2*81)
        self.blocks_delay_2_3 = blocks.delay(gr.sizeof_float*1, 3*81)
        self.blocks_delay_2_2_0 = blocks.delay(gr.sizeof_float*1, 7*81)
        self.blocks_delay_2_2 = blocks.delay(gr.sizeof_float*1, 4*81)
        self.blocks_delay_2_1_0 = blocks.delay(gr.sizeof_float*1, 8*81)
        self.blocks_delay_2_1 = blocks.delay(gr.sizeof_float*1, 5*81)
        self.blocks_delay_2_0_0 = blocks.delay(gr.sizeof_float*1, 9*81)
        self.blocks_delay_2_0 = blocks.delay(gr.sizeof_float*1, 6*81)
        self.blocks_delay_2 = blocks.delay(gr.sizeof_float*1, 81)
        self.blocks_delay_1_0_0 = blocks.delay(gr.sizeof_float*1, 1)
        self.blocks_delay_1_0 = blocks.delay(gr.sizeof_float*1, 7)
        self.blocks_delay_1 = blocks.delay(gr.sizeof_float*1, 1)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, Iterp_rate/2)
        self.blocks_char_to_float_0_0 = blocks.char_to_float(1, 128)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.blocks_add_xx_0_0 = blocks.add_vff(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.blocks_add_const_vxx_1 = blocks.add_const_vff((1, ))
        self.blocks_add_const_vxx_0 = blocks.add_const_vff((-0.5, ))
        self.blocks_abs_xx_0 = blocks.abs_ff(1)
        self.analog_sig_source_x_0_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 53, 0.5, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 100, 0.5, 0)
        self.analog_noise_source_x_0 = analog.noise_source_f(analog.GR_GAUSSIAN, Sigma, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0_0, 1))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_abs_xx_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_abs_xx_0, 0), (self.qtgui_time_sink_x_0_0, 1))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_add_const_vxx_1, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.channels_quantizer_0, 0))
        self.connect((self.blocks_add_xx_0_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_add_xx_0_0, 0), (self.qtgui_freq_sink_x_0, 1))
        self.connect((self.blocks_add_xx_0_0, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.blocks_char_to_float_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_char_to_float_0, 0), (self.blocks_delay_1, 0))
        self.connect((self.blocks_char_to_float_0_0, 0), (self.blocks_sub_xx_1, 0))
        self.connect((self.blocks_char_to_float_0_0, 0), (self.qtgui_time_sink_x_0_1_1, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_abs_xx_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_delay_1, 0), (self.qtgui_time_sink_x_0_1, 1))
        self.connect((self.blocks_delay_1_0, 0), (self.blocks_float_to_char_0_0, 0))
        self.connect((self.blocks_delay_1_0_0, 0), (self.blocks_sub_xx_1, 1))
        self.connect((self.blocks_delay_1_0_0, 0), (self.qtgui_time_sink_x_0_1_1, 1))
        self.connect((self.blocks_delay_2, 0), (self.qtgui_time_sink_x_0_2, 1))
        self.connect((self.blocks_delay_2_0, 0), (self.qtgui_time_sink_x_0_2, 6))
        self.connect((self.blocks_delay_2_0_0, 0), (self.qtgui_time_sink_x_0_2, 9))
        self.connect((self.blocks_delay_2_1, 0), (self.qtgui_time_sink_x_0_2, 5))
        self.connect((self.blocks_delay_2_1_0, 0), (self.qtgui_time_sink_x_0_2, 8))
        self.connect((self.blocks_delay_2_2, 0), (self.qtgui_time_sink_x_0_2, 4))
        self.connect((self.blocks_delay_2_2_0, 0), (self.qtgui_time_sink_x_0_2, 7))
        self.connect((self.blocks_delay_2_3, 0), (self.qtgui_time_sink_x_0_2, 3))
        self.connect((self.blocks_delay_2_4, 0), (self.qtgui_time_sink_x_0_2, 2))
        self.connect((self.blocks_float_to_char_0, 0), (self.blocks_unpack_k_bits_bb_0, 0))
        self.connect((self.blocks_float_to_char_0_0, 0), (self.blocks_pack_k_bits_bb_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.interp_fir_filter_xxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.interp_fir_filter_xxx_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_delay_1_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.qtgui_time_sink_x_0_1, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.fir_filter_xxx_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.qtgui_time_sink_x_0_0, 2))
        self.connect((self.blocks_pack_k_bits_bb_0, 0), (self.blocks_char_to_float_0_0, 0))
        self.connect((self.blocks_sub_xx_1, 0), (self.qtgui_time_sink_x_0_1_1, 2))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.channels_quantizer_0, 0), (self.blocks_delay_1_0_0, 0))
        self.connect((self.channels_quantizer_0, 0), (self.blocks_float_to_char_0, 0))
        self.connect((self.epy_block_0, 0), (self.blocks_add_const_vxx_1, 0))
        self.connect((self.fir_filter_xxx_0, 0), (self.epy_block_0, 0))
        self.connect((self.fir_filter_xxx_0, 0), (self.qtgui_histogram_sink_x_0, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.interp_fir_filter_xxx_0_0, 0), (self.blocks_add_xx_0_0, 0))
        self.connect((self.interp_fir_filter_xxx_0_0, 0), (self.blocks_delay_2, 0))
        self.connect((self.interp_fir_filter_xxx_0_0, 0), (self.blocks_delay_2_0, 0))
        self.connect((self.interp_fir_filter_xxx_0_0, 0), (self.blocks_delay_2_0_0, 0))
        self.connect((self.interp_fir_filter_xxx_0_0, 0), (self.blocks_delay_2_1, 0))
        self.connect((self.interp_fir_filter_xxx_0_0, 0), (self.blocks_delay_2_1_0, 0))
        self.connect((self.interp_fir_filter_xxx_0_0, 0), (self.blocks_delay_2_2, 0))
        self.connect((self.interp_fir_filter_xxx_0_0, 0), (self.blocks_delay_2_2_0, 0))
        self.connect((self.interp_fir_filter_xxx_0_0, 0), (self.blocks_delay_2_3, 0))
        self.connect((self.interp_fir_filter_xxx_0_0, 0), (self.blocks_delay_2_4, 0))
        self.connect((self.interp_fir_filter_xxx_0_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.interp_fir_filter_xxx_0_0, 0), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.interp_fir_filter_xxx_0_0, 0), (self.qtgui_time_sink_x_0_2, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_C_1(self):
        return self.C_1

    def set_C_1(self, C_1):
        self.C_1 = C_1
        self.set_Iterp_rate(len(self.C_1))
        self.interp_fir_filter_xxx_0_0.set_taps((self.C_1))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0_2.set_samp_rate(self.samp_rate*self.NPTS*8)
        self.qtgui_time_sink_x_0_1_1.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_1.set_samp_rate(self.samp_rate*self.NPTS)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate*self.NPTS*8)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate*self.NPTS*self.Iterp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate*self.NPTS*8)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_Sigma(self):
        return self.Sigma

    def set_Sigma(self, Sigma):
        self.Sigma = Sigma
        self.analog_noise_source_x_0.set_amplitude(self.Sigma)

    def get_R_RZ(self):
        return self.R_RZ

    def set_R_RZ(self, R_RZ):
        self.R_RZ = R_RZ

    def get_R_NRZ(self):
        return self.R_NRZ

    def set_R_NRZ(self, R_NRZ):
        self.R_NRZ = R_NRZ

    def get_NPTS(self):
        return self.NPTS

    def set_NPTS(self, NPTS):
        self.NPTS = NPTS
        self.qtgui_time_sink_x_0_2.set_samp_rate(self.samp_rate*self.NPTS*8)
        self.qtgui_time_sink_x_0_1.set_samp_rate(self.samp_rate*self.NPTS)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate*self.NPTS*8)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate*self.NPTS*self.Iterp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate*self.NPTS*8)
        self.channels_quantizer_0.set_bits(self.NPTS)

    def get_Iterp_rate(self):
        return self.Iterp_rate

    def set_Iterp_rate(self, Iterp_rate):
        self.Iterp_rate = Iterp_rate
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate*self.NPTS*self.Iterp_rate)
        self.interp_fir_filter_xxx_0.set_taps((1*[1]+(self.Iterp_rate -1)*[0]))
        self.fir_filter_xxx_0.set_taps((self.Iterp_rate*[1]))
        self.blocks_delay_0.set_dly(self.Iterp_rate/2)

    def get_C_3(self):
        return self.C_3

    def set_C_3(self, C_3):
        self.C_3 = C_3

    def get_C_2(self):
        return self.C_2

    def set_C_2(self, C_2):
        self.C_2 = C_2


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
