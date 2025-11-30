import csv
def read_file():
    with open('books.csv') as file:
        books = csv.reader(file)
        next(books)
        arr = []
        for line in books:
            arr.append(line)
        return arr
def write():
    for line in read_file():
        with open(f'books_{line[2]}.txt','w') as file:
            title = line[0]
            author = line[1]
            genre = line[2]
            year = line[3]
            file.write(f'Title: {title}, Author: {author}, Genre: {genre}, Year: {year}\n')

write()
