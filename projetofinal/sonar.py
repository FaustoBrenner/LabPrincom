from gnuradio import gr, gru
from gnuradio.wxgui import stdgui, fftsink, form, slider, scopesink
from gnuradio import eng_notation
from gnuradio import usrp
from gnuradio.eng_option import eng_option
from optparse import OptionParser
import wx
import math
import sys
#import Numeric
import numpy as np

class ptt_graph(stdgui.gui_flow_graph):
    def __init__(self, frame, panel, vbox, argv):
        stdgui.gui_flow_graph.__init__ (self, frame, panel,
                                        vbox, argv)
        self.frame = frame
        #
        print "GUI building"
        self._build_gui(frame, panel, vbox, argv, options.no_gui)
    def set_transmit(self, enabled):
        self.txpath.set_enable(enabled)
        self.rxpath.set_enable(not(enabled))
    def _build_gui(self, frame, panel, vbox, argv, no_gui):
        self.panel = panel
        vbox.Add(wx.Button(panel, -1, 'Button1'), 1, wx.ALL | wx.ALIGN_CENTER |
            wx.EXPAND, 5 )
        vbox.Add(wx.Button(panel, -1, 'Button2'), 1, wx.ALL | wx.ALIGN_CENTER |
            wx.EXPAND, 5 )
        vbox.Add(wx.Button(panel, -1, 'Button3'), 1, wx.ALL | wx.ALIGN_CENTER |
            wx.EXPAND, 5 )
        panel.SetFocus()

    
class transmit_path(gr.hier_block):
    def __init__(self, fg):
        interp = 500            #interp rate to produce 1 ms waveform
        nchan = 1               #number of complex channels
        #duc1 set to zero because the waveform is being created at baseband.
        #Change this value to make use of the mixer in the AD9860.
        duc1 = 0
        fs = 256e3              #2nd sample rate usb -> dac
        max_dev = 32e3          #1st sample rate
        self.gain = 32e3
        self.pri_time = 0.01    #pri in seconds
        self.pri_ticks = int(self.pri_time*64e6)
        k = 2 * math.pi * max_dev / fs
        #
        #monochromatic pulse 40kHz [1.28]*256
        vec1 = np.arange (1.248, 1.312, 0.00025)
        #vector source block takes in linear array to make chirp.
        vsource = gr.vector_source_f(vec1, False)
        thr1 = gr.throttle(gr.sizeof_float, fs)
        #fmmod generates chirp samples
        fmmod = gr.frequency_modulator_fc (k)
        #self.amp adds software gain
        self.amp = gr.multiply_const_cc(self.gain)
        #creates sink and specifies custom FPGA build to use.
        usrp_tx = usrp.sink_c (0, interp, nchan, fpga_filename =
                                'usrp_std_27-11-07(2).rbf' )
        #setup to use BASIC_TX_B daughterboard
        tx_subdev_spec = usrp.pick_tx_subdevice(usrp_tx)
        m = usrp.determine_tx_mux_value(usrp_tx, tx_subdev_spec)
        self.subdev = usrp.selected_subdev(usrp_tx, tx_subdev_spec)
        self.subdev.set_gain(0) # set max Tx gain
        usrp_tx.set_mux(m)
        #sets IF for mixer on AD9860.
        usrp_tx.set_tx_freq (1, duc1)
        #sets rx window size in terms of rx samples
        usrp_tx._write_fpga_reg(usrp.FR_USER_12, 2048)

        #sets maximum samples to send. related to padding.
        usrp_tx._write_fpga_reg(usrp.FR_USER_13, 256)
        #sets prf value. 20 bit was 16ms.
        usrp_tx._write_fpga_reg(usrp.FR_USER_14, self.pri_ticks)
        #sets delay value in rx samples to discard after the prf has occured.
        usrp_tx._write_fpga_reg(usrp.FR_USER_15, 0)
        #setup and enable debug output(disabled).
        #usrp_tx._write_oe(1, 0xffff, 0xffff)
        #usrp_tx._write_fpga_reg(FR_DEBUG_EN, bmFR_DEBUG_EN_TX_B)
        print "transmitter connecting now"
        fg.connect (vsource, thr1, fmmod, self.amp, usrp_tx)
        gr.hier_block.__init__(self, fg, None, None)
    def set_enable(self, enable):
        # set H/W Tx enable
        self.subdev.set_enable(enable)
        if enable:
            self.amp.set_k (self.gain)
        else:
            self.amp.set_k (self.gain)


class receive_path(gr.hier_block):
    def __init__(self, fg):
        # build the graph
        self.u = usrp.source_c(decim_rate=250, nchan=1 , fpga_filename =
                                'usrp_std_27-11-07(2).rbf' )
        filename = "output.bin"
        nsamples = 128000
        self.RX_fs = 256e3
        rx_subdev_spec = usrp.pick_rx_subdevice(self.u)
        self.u.set_mux(usrp.determine_rx_mux_value
                        (self.u, rx_subdev_spec))
        # determine the daughterboard subdevice we're using
        self.subdev = usrp.selected_subdev(self.u, rx_subdev_spec)
        input_rate = self.u.adc_freq() / self.u.decim_rate()
        # gain / mute block
        self.io_gain = gr.multiply_const_cc(1)
        self.head = gr.head(gr.sizeof_gr_complex, int(nsamples))
        #filesink
        self.dst = gr.file_sink(gr.sizeof_gr_complex, filename)
        #dead = gr.null_sink(gr.sizeof_gr_complex)
        fg.connect(self.u, self.io_gain, self.head, self.dst)
        gr.hier_block.__init__(self, fg, None, None)
        g = self.subdev.gain_range()
        gain = g[0]
        self.subdev.set_gain(gain)
        freq = 0
        r = self.u.tune(0, self.subdev, freq)
        if r:
            print "receiver ready..."
        else:
            sys.stderr.write('Failed to set frequency\n')
            raise SystemExit, 1
    def set_enable(self, enable):
        self.enabled = enable

def main():
    app = stdgui.stdapp(ptt_graph, "SONAR Application")

app.MainLoop()
if __name__ == '__main__':
    main()
