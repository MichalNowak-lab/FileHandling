with open('it_company.csv','r') as file:
    company = file.read()
    company_list = company.split('\n')
i = 0
h=5
while i<len(company_list):
    for line in company_list[i:i+h]:
        print(line)
        i+=h
    check = input('press enter: ')
    if check!= '':
        break
        