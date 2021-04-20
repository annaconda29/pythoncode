print("This game will tell your star sign if you enter your birthdate :)")
month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
sign_days =  [22, 20, 19, 21, 20, 21, 21, 21, 21, 21, 21, 21]
astro_signs = [ "Sagittarius", "Capricorn","Aquarius","Pisces","Aries","Taurus","Gemini","Cancer","Leo","Virgo","Libra","Scorpio"]
month   = int(input("When is your birth month (1-12): "))
day     = int(input("Enter birth date: (1-31) "))

for month_idx in range(1, 13):
    if month_idx == month:
        if day > 0 and day < month_days[month_idx]:
            if day < sign_days[month_idx]:
                print("You were born on", day, "And your Zodiac sign is", astro_signs[month_idx])
            else:
                if month_idx == 12:
                    print("You were born on", day, "And your Zodiac sign is", astro_signs[0])
                else:
                    print("You were born on", day, "And your Zodiac sign is", astro_signs[month_idx+1])