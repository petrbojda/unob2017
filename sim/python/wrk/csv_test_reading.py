import csv
import numpy as np


def main():

    inp,out = read_csv("test_data_ssrg_bpsk_01.csv")
    print("Test data for a baseband SSRG signal mapped to BPSK:")
    print("Input:",inp)
    print("Output:",out)


def read_csv(filename):
    inp = []
    out = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            inp.append(int(row['input_of_reg']))
            out.append(complex(row['output_of_reg']))
    input_data = np.array(inp)
    output_data = np.array(out)
    return input_data,output_data


def write_csv(bb, n_of_bits, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(('iteration', 'input_of_reg', 'output_of_reg'))
        for i1 in range(0, n_of_bits):
            writer.writerow((i1, 1, bb[int(i1 / 2)]))
            writer.writerow((i1, 0, bb[int(i1 / 2)]))

if __name__ == '__main__':
    main()
