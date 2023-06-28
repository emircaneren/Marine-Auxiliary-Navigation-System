fuel_storage = int(input("Enter Actuel Fuel Level: "))
water_storage = int(input("Enter Actuel Water Level: "))
oil_storage = int(input("Enter Actuel oil_storage Level: "))

with open('embedded-data.txt', 'w') as data:
    data.write(f"Fuel: {fuel_storage}\n")
    data.write(f"Water: {water_storage}\n")
    data.write(f"Oil: {oil_storage}\n")