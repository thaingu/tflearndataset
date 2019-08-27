import csv

makes = []
with open('amazon_baby.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Ignore first row

    for row in reader:
        makes.append(row[1])

labels = []
for idx, item in enumerate(makes):
    if int(item) >= 3:
        labels.append("1")
    else:
        labels.append("0")

with open('amazon_baby_binary.txt', 'w') as f:
    for item in labels:
        f.write("%s\n" % item)