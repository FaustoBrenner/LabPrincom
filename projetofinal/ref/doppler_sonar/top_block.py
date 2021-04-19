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

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import waterfallsink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "C:\Program Files\GNURadio-3.7\share\icons\hicolor\scalable/apps\gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.sonar_freq = sonar_freq = 20000
        self.samp_rate = samp_rate = 48000

        ##################################################
        # Blocks
        ##################################################
        self.wxgui_waterfallsink2_0 = waterfallsink2.waterfall_sink_c(
        	self.GetWin(),
        	baseband_freq=0,
        	dynamic_range=100,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=100,
        	average=False,
        	avg_alpha=None,
        	title='Waterfall Plot',
        )
        self.Add(self.wxgui_waterfallsink2_0.win)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=100,
        	average=False,
        	avg_alpha=None,
        	title='FFT Plot',
        	peak_hold=False,
        )
        self.Add(self.wxgui_fftsink2_0.win)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_float_to_complex_0_0 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.band_pass_filter_0 = filter.fir_filter_ccf(10, firdes.band_pass(
        	1, samp_rate, 10, 4.5e3, 20, firdes.WIN_HAMMING, 6.76))
        self.audio_source_0 = audio.source(samp_rate, '', True)
        self.audio_sink_0 = audio.sink(samp_rate, '', True)
        self.analog_sig_source_x_1 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, sonar_freq, 1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, sonar_freq, 1, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.audio_sink_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_float_to_complex_0_0, 1))
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.audio_source_0, 0), (self.blocks_float_to_complex_0_0, 0))
        self.connect((self.band_pass_filter_0, 0), (self.wxgui_fftsink2_0, 0))
        self.connect((self.band_pass_filter_0, 0), (self.wxgui_waterfallsink2_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_float_to_complex_0_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_multiply_xx_0, 0), (self.band_pass_filter_0, 0))

    def get_sonar_freq(self):
        return self.sonar_freq

    def set_sonar_freq(self, sonar_freq):
        self.sonar_freq = sonar_freq
        self.analog_sig_source_x_1.set_frequency(self.sonar_freq)
        self.analog_sig_source_x_0.set_frequency(self.sonar_freq)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_waterfallsink2_0.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, 10, 4.5e3, 20, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
