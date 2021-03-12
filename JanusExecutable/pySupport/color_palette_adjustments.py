import csv
import sys


def import_palette(input_file):
    data = {}
    with open(input_file, 'r') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=';')
        # header = ['MEASURE', 'INFORMATIVENESS']
        for line in reader:
            # data[line['c1']] = [4-int(None in line.values())]+list(line.values())
            data[line['c1']] = [1] + list(line.values())
    return data

def main():
    input_file_path = sys.argv[1]

    # input file
    fin = open(input_file_path, "rt")
    # output file to write the result to
    fout = open(input_file_path[:-4]+"-NEW-PALETTE.svg", "wt")
    # for each line in the input file

    print("in:  "+input_file_path)
    print("out: "+input_file_path[:-4]+"-NEW-PALETTE.svg")

    palette = import_palette("hex-palette-list.csv")

    for line in fin:
        # read replace the string and write to output file
        new_line = line
        if any(key in line for key in palette):
            obj = line[line.find("stroke:") + 7:line.find("stroke:") + 14]
            new_obj = palette[obj][palette[obj][0]]
            new_line = new_line.replace(obj, new_obj)
            palette[obj][0] += 1
            if palette[obj][0] > 4-int(None in palette[obj]):
                palette[obj][0] = 1
        fout.write(new_line)

    # close input and output files
    fin.close()
    fout.close()

if __name__ == "__main__":
    main()
