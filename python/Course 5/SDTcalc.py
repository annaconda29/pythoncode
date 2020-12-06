
calc = input("Do you want to find speed, dist or time: ")
if calc == "speed":
    speedunit = input("Choose you unit: m/s or km/h:   ")
    #speed = int(input("Enter speed (don't enter unit): "))
    dist = int(input("Enter dist (don't enter unit): "))
    time = int(input("Enter time (don't enter unit): "))
    print("speed =", dist/time, speedunit)
    

elif calc == "distance":
    distunit = input("Choose unit: m or km:   ")
    speed = int(input("Enter speed (don't enter unit): "))
    time = int(input("Enter time (don't enter unit): "))
    print("dist =", speed*time, distunit)

elif calc == "time":
    timeunit = input("Choose unit: s or h:   ")
    speed = int(input("Enter speed (don't enter unit): "))
    dist = int(input("Enter dist (don't enter unit): "))
    print("time =", dist/speed, timeunit)