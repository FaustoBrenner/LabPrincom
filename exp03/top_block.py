#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Wed Sep 16 19:58:42 2020
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
        self.samp_rate = samp_rate = 240000

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_time_sink_x_0_2_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_0_2_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_2_0.set_y_axis(-2.5, 2.5)
        
        self.qtgui_time_sink_x_0_2_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0_2_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_2_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_2_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_2_0.enable_grid(True)
        self.qtgui_time_sink_x_0_2_0.enable_control_panel(True)
        
        if not True:
          self.qtgui_time_sink_x_0_2_0.disable_legend()
        
        labels = ["mQ(t)", "m^Q(t)", "mI(t)", "mQ(t)", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["dark red", "blue", "dark red", "Dark Blue", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [2, 1, 2, 2, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_2_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_2_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_2_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_2_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_2_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_2_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_2_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_2_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_2_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_2_0_win)
        self.qtgui_time_sink_x_0_2 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_0_2.set_update_time(0.10)
        self.qtgui_time_sink_x_0_2.set_y_axis(-2.5, 2.5)
        
        self.qtgui_time_sink_x_0_2.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0_2.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_2.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_2.enable_autoscale(False)
        self.qtgui_time_sink_x_0_2.enable_grid(True)
        self.qtgui_time_sink_x_0_2.enable_control_panel(True)
        
        if not True:
          self.qtgui_time_sink_x_0_2.disable_legend()
        
        labels = ["mI(t)", "m^I(t)", "mI(t)", "mQ(t)", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["dark red", "blue", "dark red", "Dark Blue", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [2, 1, 2, 2, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(2):
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
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_2_win)
        self.low_pass_filter_0_1 = filter.fir_filter_fff(1, firdes.low_pass(
        	1, samp_rate, 7000, 100, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0_0 = filter.fir_filter_fff(1, firdes.low_pass(
        	1, samp_rate, 7000, 100, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0 = filter.fir_filter_fff(1, firdes.low_pass(
        	1, samp_rate, 7000, 100, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0 = filter.fir_filter_fff(1, firdes.low_pass(
        	1, samp_rate, 7000, 100, firdes.WIN_HAMMING, 6.76))
        self.blocks_multiply_xx_0_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_delay_0_0 = blocks.delay(gr.sizeof_float*1, 2)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, 2)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_sig_source_x_1_2 = analog.sig_source_f(samp_rate, analog.GR_SQR_WAVE, 700, 2, -1)
        self.analog_sig_source_x_1_1 = analog.sig_source_f(samp_rate, analog.GR_TRI_WAVE, 1000, 2, -1)
        self.analog_sig_source_x_1_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, 10000, 0.285714286, 0)
        self.analog_sig_source_x_1 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, 10000, 7, 0)
        self.analog_sig_source_x_0_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 10000, 0.285714286, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 10000, 7, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 0))    
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_delay_0, 0))    
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_multiply_xx_0_0, 1))    
        self.connect((self.analog_sig_source_x_1_0, 0), (self.blocks_delay_0_0, 0))    
        self.connect((self.analog_sig_source_x_1_1, 0), (self.low_pass_filter_0_0_0, 0))    
        self.connect((self.analog_sig_source_x_1_2, 0), (self.low_pass_filter_0_1, 0))    
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_xx_0_0_0, 0))    
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_xx_0_1, 1))    
        self.connect((self.blocks_delay_0, 0), (self.blocks_multiply_xx_0_1, 0))    
        self.connect((self.blocks_delay_0_0, 0), (self.blocks_multiply_xx_0_0_0, 1))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_add_xx_0, 0))    
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_add_xx_0, 1))    
        self.connect((self.blocks_multiply_xx_0_0_0, 0), (self.low_pass_filter_0_0, 0))    
        self.connect((self.blocks_multiply_xx_0_1, 0), (self.low_pass_filter_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_time_sink_x_0_2, 1))    
        self.connect((self.low_pass_filter_0_0, 0), (self.qtgui_time_sink_x_0_2_0, 1))    
        self.connect((self.low_pass_filter_0_0_0, 0), (self.blocks_multiply_xx_0_0, 0))    
        self.connect((self.low_pass_filter_0_0_0, 0), (self.qtgui_time_sink_x_0_2_0, 0))    
        self.connect((self.low_pass_filter_0_1, 0), (self.blocks_multiply_xx_0, 1))    
        self.connect((self.low_pass_filter_0_1, 0), (self.qtgui_time_sink_x_0_2, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1_2.set_sampling_freq(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 7000, 100, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, 7000, 100, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0_0.set_taps(firdes.low_pass(1, self.samp_rate, 7000, 100, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_1.set_taps(firdes.low_pass(1, self.samp_rate, 7000, 100, firdes.WIN_HAMMING, 6.76))
        self.qtgui_time_sink_x_0_2.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_2_0.set_samp_rate(self.samp_rate)


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
