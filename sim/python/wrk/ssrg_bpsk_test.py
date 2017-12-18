# import sys
# sys.path.append("../sim")
import csv
import numpy as np
from siggens import PRN_bitstreams as prn
from modulators import constallation_mappers as cm

def main():
    # Setting up the coder's initialization and feedback vector
    init = np.array ([1,1,1,1])
    fb = np.array   ([0,1,0,1])
    n_of_bits = 40
    # Running the coder
    out_seq = prn.ssrg(init,fb,n_bits=n_of_bits,verbosity=True)
    code = [int(elem)for elem in out_seq]
    # Mapping the code into symbols of two bits
    sym = map_4ary_symbols(code)
    bb = 2*sym[:,0]-1 + 0j
    # Prepare a csv file to test GNU Radio module
    write_csv(bb,40,"test_data_ssrg_bpsk_01.csv")

def map_4ary_symbols(data):
    tup = 2  # number of bits in one tuple
    n_d = tup - (np.size(data) % tup)
    data = np.append(data, np.zeros(n_d))  # appends zero to get odd number of bits
    data_2s = data.reshape(-1, tup)  # reshaping the data vector into matrix
    return data_2s

def write_csv(bb,n_of_bits,filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(('iteration', 'input_of_reg', 'output_of_reg'))
        for i1 in range (0,n_of_bits):
            writer.writerow((i1, 1, bb[int(i1/2)]))
            writer.writerow((i1, 0, bb[int(i1 / 2)]))
    # TODO: Indexing of the bb vector is not correct

if __name__ == '__main__':
    main()
