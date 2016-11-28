import sys

new_file = "lower_cased.txt"
read_file = "t.txt"
WRITE = "w"

with open(new_file, WRITE) as nf:
	for line in open(read_file, "r"):
		nf.write(line.lower())

nf.close()




