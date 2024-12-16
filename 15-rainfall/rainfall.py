rain = {}
while True:
    question = print("Input a city and tell me how much rain has fallen. I'll keep track of it.\n")
    city = input('Input the name of the city: ')
    if not city:
        break
    try:
        mm_rain = int(input('Input the amount of rain in mm: '))
    except ValueError:
        print("You stoopid.")
        continue
        
    rain[city]= rain.get(city, 0) + int(mm_rain)
    
for c, r in rain.items():
        print(f"{c}: {r} mm of rain.")
