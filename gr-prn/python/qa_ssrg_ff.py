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
from ssrg_f import ssrg_f

class qa_ssrg_ff (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        init_reg = [1,1,1,1]
        fb = [0,1,0,1]
        # Expected results for two periods of code, means for 12 iterations
        expected_result = [1,1,1,1,0,0,1,1,1,1,0,0]
        coder = ssrg_f(init_reg,fb)
        snk = blocks.vector_sink_b()
        self.tb.connect(coder, snk)
        self.tb.run()
        result_data = snk.data()
        self.assertFloatTuplesAlmostEqual(expected_result, result_data, 6)
        # TODO: Assure the coder will run for an exact number of times, 12 in this case.

if __name__ == '__main__':
    gr_unittest.run(qa_ssrg_ff, "qa_ssrg_ff.xml")
