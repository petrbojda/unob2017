#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2017 Petr BOJDA.
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

from gnuradio import gr, gr_unittest
from gnuradio import blocks
from ssrg_bpsk_fc import ssrg_bpsk_fc
import csv

class qa_ssrg_bpsk_fc (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        src_data,expected_result = self.read_csv("test_data_ssrg_bpsk_01.csv")
        init_register = [1,1,1,1]
        feedback = [0,1,0,1]
        src = blocks.vector_source_f(src_data)
        bpsk = ssrg_bpsk_fc(init_register,feedback,2,-1)
        dst = blocks.vector_sink_c()
        self.tb.connect(src, bpsk)
        self.tb.connect(bpsk, dst)
        self.tb.run()
        result_data = dst.data()
        print result_data
        print expected_result
        self.assertFloatTuplesAlmostEqual(expected_result, result_data, 6)

    def read_csv(self, filename):
        inp = []
        out = []
        with open(filename) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                inp.append(int(row['input_of_reg']))
                out.append(complex(row['output_of_reg']))
        return inp, out


if __name__ == '__main__':
    gr_unittest.run(qa_ssrg_bpsk_fc, "qa_ssrg_bpsk_fc.xml")
