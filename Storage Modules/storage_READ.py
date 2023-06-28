with open('embedded-data.txt', 'r') as data:
    for line in data:
        if 'Fuel' in line:
            fuel_storage = int(line.split(':')[1].strip())
            print('Fuel :', fuel_storage)

with open('embedded-data.txt', 'r') as data:
    for line in data:
        if 'Water' in line:
            water_storage = int(line.split(':')[1].strip())
            print('Water:', water_storage)

with open('embedded-data.txt', 'r') as data:
    for line in data:
        if 'Oil' in line:
            oil_storage = int(line.split(':')[1].strip())
            print('Oil:', oil_storage)
