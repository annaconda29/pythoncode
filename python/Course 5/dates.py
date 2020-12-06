import datetime

x = datetime.datetime.now()
print("Todays date and time: ", x)
print("Current year: ", x.year)
print("Todays day: ", x.strftime("%A"))

#A few str formattings for date and time module.
y = datetime.datetime(2020, 11, 18)
print("Todays month: ", x.strftime("%B"))
print("AM or PM?: ", x.strftime("%p"))
print("Todays day number if Sunday = 0: ", x.strftime("%w"))
print("Todays day (short ver.): ", x.strftime("%a"))
