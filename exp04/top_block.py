#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Sun Oct  4 23:45:29 2020
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
        self.samp_rate = samp_rate = 240000
        self.fm = fm = 0.5
        self.fc = fc = 10000
        self.Df = Df = 1000
        self.An = An = 0
        self.Am = Am = 1

        ##################################################
        # Blocks
        ##################################################
        self._fc_range = Range(1000, 20000, 1000, 10000, 200)
        self._fc_win = RangeWidget(self._fc_range, self.set_fc, "fc", "counter_slider", float)
        self.top_layout.addWidget(self._fc_win)
        self._Df_range = Range(500, 2000, 100, 1000, 200)
        self._Df_win = RangeWidget(self._Df_range, self.set_Df, "Df", "counter_slider", float)
        self.top_layout.addWidget(self._Df_win)
        self._An_range = Range(0, 5, 0.5, 0, 200)
        self._An_win = RangeWidget(self._An_range, self.set_An, "An", "counter_slider", float)
        self.top_layout.addWidget(self._An_win)
        self._Am_range = Range(0, 10, 0.5, 1, 200)
        self._Am_win = RangeWidget(self._Am_range, self.set_Am, "Am", "counter_slider", float)
        self.top_layout.addWidget(self._Am_win)
        self.v = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, 1, Am, 0)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(True)
        self.qtgui_time_sink_x_0.enable_control_panel(True)
        
        if not True:
          self.qtgui_time_sink_x_0.disable_legend()
        
        labels = ["Re{s(t)}", "Im{s(t)}", "Re{c(t)}", "Im{c(t)}", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 2, 1, 2, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(2*2):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	4096, #size
        	firdes.WIN_RECTANGULAR, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(True)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_control_panel(True)
        
        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)
        
        labels = ["S(f)", "C(f)", "", "", "",
                  "", "", "", "", ""]
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
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self._fm_range = Range(0, 1, 0.02, 0.5, 200)
        self._fm_win = RangeWidget(self._fm_range, self.set_fm, "fm", "counter_slider", float)
        self.top_layout.addWidget(self._fm_win)
        self.blocks_vco_c_0 = blocks.vco_c(samp_rate, 6283.1, 1)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, fc, 1, 0)
        self.analog_pll_refout_cc_0 = analog.pll_refout_cc(0.0628318530717, (fc+Df)*0.0000261799387799, (fc-Df)*0.0000261799387799)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, An, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 1))    
        self.connect((self.analog_pll_refout_cc_0, 0), (self.qtgui_freq_sink_x_0, 1))    
        self.connect((self.analog_pll_refout_cc_0, 0), (self.qtgui_time_sink_x_0, 1))    
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))    
        self.connect((self.blocks_add_xx_0, 0), (self.analog_pll_refout_cc_0, 0))    
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_freq_sink_x_0, 0))    
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_time_sink_x_0, 0))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_add_xx_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.blocks_vco_c_0, 0))    
        self.connect((self.blocks_vco_c_0, 0), (self.blocks_multiply_xx_0, 0))    
        self.connect((self.v, 0), (self.blocks_throttle_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.v.set_sampling_freq(self.samp_rate)

    def get_fm(self):
        return self.fm

    def set_fm(self, fm):
        self.fm = fm

    def get_fc(self):
        return self.fc

    def set_fc(self, fc):
        self.fc = fc
        self.analog_pll_refout_cc_0.set_max_freq((self.fc+self.Df)*0.0000261799387799)
        self.analog_pll_refout_cc_0.set_min_freq((self.fc-self.Df)*0.0000261799387799)
        self.analog_sig_source_x_0.set_frequency(self.fc)

    def get_Df(self):
        return self.Df

    def set_Df(self, Df):
        self.Df = Df
        self.analog_pll_refout_cc_0.set_max_freq((self.fc+self.Df)*0.0000261799387799)
        self.analog_pll_refout_cc_0.set_min_freq((self.fc-self.Df)*0.0000261799387799)

    def get_An(self):
        return self.An

    def set_An(self, An):
        self.An = An
        self.analog_noise_source_x_0.set_amplitude(self.An)

    def get_Am(self):
        return self.Am

    def set_Am(self, Am):
        self.Am = Am
        self.v.set_amplitude(self.Am)


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
