calc = input("Do you want to find speed, dist or time: ")

class speed:
    speedunit = input("Choose your unit: m/s or km/h:   ")
    dist = int(input("Enter dist (don't enter unit): "))
    time = int(input("Enter time (don't enter unit): "))
    x = "speed =", dist/time, speedunit

class distance:
    distunit = input("Choose unit: m or km:   ")
    speed = int(input("Enter speed (don't enter unit): "))
    time = int(input("Enter time (don't enter unit): "))
    y = "dist =", (speed*time), distunit

class time:
    timeunit = input("Choose unit: s or h:   ")
    speed = int(input("Enter speed (don't enter unit): "))
    dist = int(input("Enter dist (don't enter unit): "))
    z = "time =", (dist/speed), timeunit

if calc == "speed":
    sp = speed()
    print(sp.x)
    

elif calc == "distance" or "dist":
    dist = distance()
    print(dist.y)
    

elif calc == "time":
    time = time()
    print(time.z)
    
