
import sys
#the script just removed the space, but the comma is there in the input file
infile = "train.txt"
outfile = "train.csv"
with open(infile, 'rb') as in_file:
    with open(outfile, 'wb') as out_file:
        for line in in_file.readlines():
            line = line.strip()
            line = line.replace(b', ', b',')
            if not line or b',' not in line:
                continue
            if line[-1] == b'.':
                line = line[:-1]
            line += '\n'
            out_file.write(line)
