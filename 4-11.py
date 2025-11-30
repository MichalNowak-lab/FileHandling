with open('powers.txt', 'w') as file:
    for i in range(1,101):
        number = i
        squared = i**2
        cubed = i**3
        file.write(f'{number},{squared},{cubed}\n')
        print(number,squared,cubed)