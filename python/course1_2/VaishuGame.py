print("This game will tell your star sign if you enter your birthdate :)")
month = input("When is your birth month (Start with Capital Letter): ")
day = int(input("Enter birth date: format ex: 22, 31, 3, etc: "))
birthday = month, day
birthday = list(birthday)

if birthday[0] == "December" and birthday[1] < 22:
    astro_sign = 'Sagittarius' 
else: astro_sign = 'Capricorn'

if birthday[0] == "January" and birthday[1] < 20:
    astro_sign = 'Capricorn' 
else: astro_sign = 'Aquarius'

if birthday[0] == "February" and birthday[1] < 19:
    astro_sign = 'Aquarius' 
else: astro_sign = 'Pisces'

if birthday[0] == "March" and birthday[1] < 21:
    astro_sign = 'Pisces' 
else: astro_sign = 'Aries'

if birthday[0] == "April" and birthday[1] < 20:
    astro_sign = 'Aries'
else: astro_sign ='Taurus'

if birthday[0] == "May" and birthday[1] < 21:
    astro_sign = 'Taurus'
else: astro_sign = 'Gemini'

if birthday[0] == "June" and birthday[1] < 21:
    astro_sign = 'Gemini'
else: astro_sign = 'Cancer'

if birthday[0] == "July" and birthday[1] < 21:
    astro_sign = 'Cancer'
else: astro_sign = 'Leo'

if birthday[0] == "August" and birthday[1] < 21:
    astro_sign = 'Leo' 
else: astro_sign = 'Virgo'

if birthday[0] == "September" and birthday[1] < 21:
    astro_sign = 'Virgo'
else: astro_sign = 'Libra'

if birthday[0] == "October" and birthday[1] < 21:
    astro_sign = 'Libra'
else: astro_sign = 'Scorpio'

if birthday[0] == "November" and birthday[1] < 21:
    astro_sign = 'Scorpio'
else: 'Sagittarius'

print("You were born on", birthday, "And your Zodiac sign is", astro_sign)