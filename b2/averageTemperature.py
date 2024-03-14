def averageTemperature(a):
    temp =0
    above_average =0
    for i in a:
        temp += i
    average_day=temp/len(a)
    for i in a:
        if i > average_day:
            above_average+= 1
    print(f"Average = {average_day}")
    print(f"{above_average} day(s) above average")
    
day = []
temperature_list=int(input("How many day's temperature: "))
for i in range (0,temperature_list):
    temp= int(input(f"Day {i+1} high temp: "))
    day.append(temp)
averageTemperature(day)
