import csv
with open('clothing.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for line in csv_reader:
        if float(line[5])<60 and int(line[6])<40:
            print(line)