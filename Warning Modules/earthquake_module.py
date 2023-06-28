customer_boat_class = #Embedded Customer Info
'''
0 - Sailboat
1 - Catamaran
2 - Any Vessel to12m
3 - Any Vessel to25m
4 - Yacht
5 - +25m type Vessels
'''
earthquake = #earthquakeAPI#  
earthquake_Convert = float(earthquake)
location = ###GPS###
locationConvert = str(location) ###NEED GPS CONVERT MODULE

sendALERT = 1

while sendALERT < 10:
    print(Fore.YELLOW + "\a", "WARNING! SEISMIC ACTIVITY!")
    sendALERT+= 1

print(Fore.WHITE + "Seismic Magnitude = {}, +++ Distance {}".format(earthquake_Convert, locationConvert))
if earthquake_Convert > 5 and customer_boat_class < 3:
    print(Fore.RED + "\a Attention Wave Level Is at a Level That Will Affect You!")
   
else :
    print(Fore.GREEN + "The wave level is too small to affect you")