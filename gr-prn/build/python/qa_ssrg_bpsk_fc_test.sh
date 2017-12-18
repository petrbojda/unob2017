#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/petr/Projects/Bajer/unob2017/gr-prn/python
export PATH=/home/petr/Projects/Bajer/unob2017/gr-prn/build/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH
export PYTHONPATH=/home/petr/Projects/Bajer/unob2017/gr-prn/build/swig:$PYTHONPATH
/usr/bin/python2 /home/petr/Projects/Bajer/unob2017/gr-prn/python/qa_ssrg_bpsk_fc.py 
