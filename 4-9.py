import csv
with open('it_company.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        if line[2]=='Graphic Designer':
            print(line[0],line[1],line[3])