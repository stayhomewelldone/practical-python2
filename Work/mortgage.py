# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000


while principal > 0:

    if months >= extra_payment_start_month and months <= extra_payment_end_month:
        principal -= extra_payment
        total_paid+=extra_payment
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    months+=1
    if principal < 0:
        
        total_paid+=principal
        principal = 0

    print(f'{months} {round(total_paid,2)} {round(principal,2)}')

print(f'Number of months required: {months}. Total paid: {round(total_paid,2)}' )