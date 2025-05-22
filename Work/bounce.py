# bounce.py
#
# Exercise 1.5

height = 100
bounces = 0

while bounces < 10:
    height = height /5 *3
    bounces +=1
    print(f'{bounces} {round(height, 4)}')

    