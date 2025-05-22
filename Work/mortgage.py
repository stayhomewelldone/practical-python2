# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0
extra_payment = 1000


while principal > 0:
    if months < 12:
        principal -= 1000
        total_paid+=1000
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    months+=1

print(f'Number of months required: {months}. Total paid: {round(total_paid,2)}' )