#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2017 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy as np
from gnuradio import gr

class ssrg_qpsk_fc(gr.sync_block):
    """
    docstring for block ssrg_qpsk_fc
    """
    def __init__(self, init_reg, fb_reg, ampl, offset):
        gr.sync_block.__init__(self,
            name="ssrg_qpsk_fc",
            in_sig=[np.float32],
            out_sig=[np.complex64])

        self.shift_reg = init_reg
        self.fb = fb_reg
        self.amplitude = ampl
        self.offset = offset


    def shift_register_coder(self):
        in1 = int(np.dot(self.shift_reg, self.fb) % 2)
        self.shift_reg = np.roll(self.shift_reg, 1)
        self.shift_reg[0] = in1


    def positive_edge_detector(self, sample_0, sample_1):
        return sample_0 > sample_1


    def work(self, input_items, output_items):
        out = output_items[0]
        in0 = input_items[0]
        flipflap = 0
        for i in range(0, len(in0)):
            if self.positive_edge_detector(in0[i], in0[i - 1]):
                self.shift_register_coder()
                flipflap += 1
            if flipflap % 2:
                out[i] = self.shift_reg[-1] * self.amplitude + self.offset + \
                         1j * (self.shift_reg[-2] * self.amplitude + self.offset)

        return len(output_items[0])

