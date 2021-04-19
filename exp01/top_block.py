#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Mon Aug 31 15:26:01 2020
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
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import sip
import sys


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
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
        self.samp_rate = samp_rate = 200000
        self.Gain = Gain = 1

        ##################################################
        # Blocks
        ##################################################
        self.aba = Qt.QTabWidget()
        self.aba_widget_0 = Qt.QWidget()
        self.aba_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.aba_widget_0)
        self.aba_grid_layout_0 = Qt.QGridLayout()
        self.aba_layout_0.addLayout(self.aba_grid_layout_0)
        self.aba.addTab(self.aba_widget_0, "X")
        self.aba_widget_1 = Qt.QWidget()
        self.aba_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.aba_widget_1)
        self.aba_grid_layout_1 = Qt.QGridLayout()
        self.aba_layout_1.addLayout(self.aba_grid_layout_1)
        self.aba.addTab(self.aba_widget_1, "I")
        self.aba_widget_2 = Qt.QWidget()
        self.aba_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.aba_widget_2)
        self.aba_grid_layout_2 = Qt.QGridLayout()
        self.aba_layout_2.addLayout(self.aba_grid_layout_2)
        self.aba.addTab(self.aba_widget_2, "RMS")
        self.top_layout.addWidget(self.aba)
        self._Gain_range = Range(1, 10, 0.5, 1, 200)
        self._Gain_win = RangeWidget(self._Gain_range, self.set_Gain, "Gain", "counter_slider", float)
        self.aba_layout_0.addWidget(self._Gain_win)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(-10, 10)
        
        self.qtgui_time_sink_x_0_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_AUTO, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0.enable_grid(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(True)
        
        if not True:
          self.qtgui_time_sink_x_0_0.disable_legend()
        
        labels = ["I", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["red", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
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
        self.aba_layout_0.addWidget(self._qtgui_time_sink_x_0_0_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-10, 10)
        
        self.qtgui_time_sink_x_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_AUTO, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(True)
        self.qtgui_time_sink_x_0.enable_control_panel(True)
        
        if not True:
          self.qtgui_time_sink_x_0.disable_legend()
        
        labels = ["I", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["red", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
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
        self.aba_layout_1.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_freq_sink_x_0_1_0 = qtgui.freq_sink_f(
        	4096, #size
        	firdes.WIN_RECTANGULAR, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_1_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_1_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_1_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_1_0.enable_grid(True)
        self.qtgui_freq_sink_x_0_1_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_1_0.enable_control_panel(True)
        
        if not True:
          self.qtgui_freq_sink_x_0_1_0.disable_legend()
        
        if "float" == "float" or "float" == "msg_float":
          self.qtgui_freq_sink_x_0_1_0.set_plot_pos_half(not True)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["red", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_1_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_1_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_1_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_1_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_1_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_1_0.pyqwidget(), Qt.QWidget)
        self.aba_layout_0.addWidget(self._qtgui_freq_sink_x_0_1_0_win)
        self.qtgui_freq_sink_x_0_1 = qtgui.freq_sink_f(
        	4096, #size
        	firdes.WIN_RECTANGULAR, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_1.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_1.enable_grid(True)
        self.qtgui_freq_sink_x_0_1.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_1.enable_control_panel(True)
        
        if not True:
          self.qtgui_freq_sink_x_0_1.disable_legend()
        
        if "float" == "float" or "float" == "msg_float":
          self.qtgui_freq_sink_x_0_1.set_plot_pos_half(not True)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["red", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_1.pyqwidget(), Qt.QWidget)
        self.aba_layout_1.addWidget(self._qtgui_freq_sink_x_0_1_win)
        self.low_pass_filter_0 = filter.fir_filter_fff(1, firdes.low_pass(
        	Gain, samp_rate, 2000, 200, firdes.WIN_HAMMING, 6.76))
        self.blocks_rms_xx_0_0_3_1_0_1 = blocks.rms_ff(0.0001)
        self.blocks_rms_xx_0_0_3_1_0_0_1_0 = blocks.rms_ff(0.0001)
        self.blocks_rms_xx_0_0_3_1_0_0_1 = blocks.rms_ff(0.0001)
        self.blocks_rms_xx_0_0_3_1_0_0_0_1 = blocks.rms_ff(0.0001)
        self.blocks_rms_xx_0_0_3_1_0_0_0_0_0 = blocks.rms_ff(0.0001)
        self.blocks_rms_xx_0_0_3_1_0_0_0_0 = blocks.rms_ff(0.0001)
        self.blocks_rms_xx_0_0_3_1_0_0_0 = blocks.rms_ff(0.0001)
        self.blocks_rms_xx_0_0_3_1_0_0 = blocks.rms_ff(0.0001)
        self.blocks_rms_xx_0_0_3_1_0 = blocks.rms_ff(0.0001)
        self.blocks_multiply_xx_0_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.band_pass_filter_0 = filter.fir_filter_fff(1, firdes.band_pass(
        	1, samp_rate, 15000, 17000, 200, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_1_0_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 16000, 4, 0)
        self.analog_sig_source_x_1_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 10000, 2, 0)
        self.analog_sig_source_x_1 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 6000, 5, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_TRI_WAVE, 100, 2, -1)
        self.RMS_1 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.RMS_1.set_update_time(0.10)
        self.RMS_1.set_title("")
        
        labels = ["RMS", "", "", "", "",
                  "", "", "", "", ""]
        units = ["V", "", "", "", "",
                 "", "", "", "", ""]
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.RMS_1.set_min(i, -5)
            self.RMS_1.set_max(i, 5)
            self.RMS_1.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.RMS_1.set_label(i, "Data {0}".format(i))
            else:
                self.RMS_1.set_label(i, labels[i])
            self.RMS_1.set_unit(i, units[i])
            self.RMS_1.set_factor(i, factor[i])
        
        self.RMS_1.enable_autoscale(True)
        self._RMS_1_win = sip.wrapinstance(self.RMS_1.pyqwidget(), Qt.QWidget)
        self.aba_layout_0.addWidget(self._RMS_1_win)
        self.RMS_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            7
        )
        self.RMS_0.set_update_time(0.10)
        self.RMS_0.set_title("")
        
        labels = ["A", "B", "C", "D", "E",
                  "F", "G", "", "", ""]
        units = ["V", "V", "V", "V", "V",
                 "V", "V", "", "", ""]
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(7):
            self.RMS_0.set_min(i, 0)
            self.RMS_0.set_max(i, 4)
            self.RMS_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.RMS_0.set_label(i, "Data {0}".format(i))
            else:
                self.RMS_0.set_label(i, labels[i])
            self.RMS_0.set_unit(i, units[i])
            self.RMS_0.set_factor(i, factor[i])
        
        self.RMS_0.enable_autoscale(False)
        self._RMS_0_win = sip.wrapinstance(self.RMS_0.pyqwidget(), Qt.QWidget)
        self.aba_layout_2.addWidget(self._RMS_0_win)
        self.RMS = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.RMS.set_update_time(0.10)
        self.RMS.set_title("")
        
        labels = ["RMS", "", "", "", "",
                  "", "", "", "", ""]
        units = ["V", "", "", "", "",
                 "", "", "", "", ""]
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.RMS.set_min(i, -5)
            self.RMS.set_max(i, 5)
            self.RMS.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.RMS.set_label(i, "Data {0}".format(i))
            else:
                self.RMS.set_label(i, labels[i])
            self.RMS.set_unit(i, units[i])
            self.RMS.set_factor(i, factor[i])
        
        self.RMS.enable_autoscale(True)
        self._RMS_win = sip.wrapinstance(self.RMS.pyqwidget(), Qt.QWidget)
        self.aba_layout_1.addWidget(self._RMS_win)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 0))    
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_rms_xx_0_0_3_1_0_0, 0))    
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_multiply_xx_0, 1))    
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_rms_xx_0_0_3_1_0_0_0, 0))    
        self.connect((self.analog_sig_source_x_1_0, 0), (self.blocks_multiply_xx_0_0, 1))    
        self.connect((self.analog_sig_source_x_1_0, 0), (self.blocks_rms_xx_0_0_3_1_0_0_0_0, 0))    
        self.connect((self.analog_sig_source_x_1_0_0, 0), (self.blocks_multiply_xx_0_0_0, 1))    
        self.connect((self.analog_sig_source_x_1_0_0, 0), (self.blocks_rms_xx_0_0_3_1_0_0_0_0_0, 0))    
        self.connect((self.band_pass_filter_0, 0), (self.blocks_multiply_xx_0_0_0, 0))    
        self.connect((self.band_pass_filter_0, 0), (self.blocks_rms_xx_0_0_3_1_0_0_1_0, 0))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_multiply_xx_0_0, 0))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_rms_xx_0_0_3_1_0_0_1, 0))    
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.band_pass_filter_0, 0))    
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_rms_xx_0_0_3_1_0_0_0_1, 0))    
        self.connect((self.blocks_multiply_xx_0_0_0, 0), (self.blocks_rms_xx_0_0_3_1_0_1, 0))    
        self.connect((self.blocks_multiply_xx_0_0_0, 0), (self.low_pass_filter_0, 0))    
        self.connect((self.blocks_multiply_xx_0_0_0, 0), (self.qtgui_freq_sink_x_0_1_0, 0))    
        self.connect((self.blocks_multiply_xx_0_0_0, 0), (self.qtgui_time_sink_x_0_0, 0))    
        self.connect((self.blocks_rms_xx_0_0_3_1_0, 0), (self.RMS, 0))    
        self.connect((self.blocks_rms_xx_0_0_3_1_0_0, 0), (self.RMS_0, 0))    
        self.connect((self.blocks_rms_xx_0_0_3_1_0_0_0, 0), (self.RMS_0, 1))    
        self.connect((self.blocks_rms_xx_0_0_3_1_0_0_0_0, 0), (self.RMS_0, 3))    
        self.connect((self.blocks_rms_xx_0_0_3_1_0_0_0_0_0, 0), (self.RMS_0, 6))    
        self.connect((self.blocks_rms_xx_0_0_3_1_0_0_0_1, 0), (self.RMS_0, 4))    
        self.connect((self.blocks_rms_xx_0_0_3_1_0_0_1, 0), (self.RMS_0, 2))    
        self.connect((self.blocks_rms_xx_0_0_3_1_0_0_1_0, 0), (self.RMS_0, 5))    
        self.connect((self.blocks_rms_xx_0_0_3_1_0_1, 0), (self.RMS_1, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.blocks_rms_xx_0_0_3_1_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_freq_sink_x_0_1, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_time_sink_x_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1_0_0.set_sampling_freq(self.samp_rate)
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, 15000, 17000, 200, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(self.Gain, self.samp_rate, 2000, 200, firdes.WIN_HAMMING, 6.76))
        self.qtgui_freq_sink_x_0_1.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_1_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate)

    def get_Gain(self):
        return self.Gain

    def set_Gain(self, Gain):
        self.Gain = Gain
        self.low_pass_filter_0.set_taps(firdes.low_pass(self.Gain, self.samp_rate, 2000, 200, firdes.WIN_HAMMING, 6.76))


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
