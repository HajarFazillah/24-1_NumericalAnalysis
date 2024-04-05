import mod1
from mod2 import calc_area_circle

nation = 'en'
r_length = 10

mod1.greeting(nation)
area_circle = calc_area_circle(r_length)

print(f"The area of circle with radius = {r_length} is {area_circle}.")

print("This is the END of main.py file!")