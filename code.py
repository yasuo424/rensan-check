import csv
#csvファイルを読み込む
f = csv.reader(open("test.csv"),dialect='excel')
#空のディクショナリを作成		
d={}

#keyとvalueをそれぞれ格納
for line in f:
	key = line[0]
	value = line[1]
	if key in d:
		v = d[key]
		v.append(value)
	else:
		d[key] = [value, ]

#keyに対して対応するvalueを紐付け
key = "a"
t=[]
while True :
	t.append(key)
	if key in d:
		value = d[key]
		key = value[0]
	else:
		break
print(t)


