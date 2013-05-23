import csv
f = csv.reader(open("test.csv"),dialect='excel')
d={}

for line in f:
    if line[0] in d:
		v = d[line[0]]
		v.append(line[1])
	else:
		d[line[0]] = [line[1], ]
	print(d)
print(d["a"])
