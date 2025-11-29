def r_file():
    with open('pets', 'r') as file:
        content = file.read()
        content = content.split()
        print(len(content))
r_file()