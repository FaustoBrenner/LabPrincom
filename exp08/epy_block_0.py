"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr


class blk(gr.sync_block):

    def __init__(self, passo=1):
        gr.sync_block.__init__(
            self,
            name='Decisor: SGN(in)',   # will show up in GRC
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.passo = passo

    def work(self, input_items, output_items):
        """example: multiply with constant"""
        output_items[0][:] = np.sign(input_items[0]) * self.passo
        return len(output_items[0])
