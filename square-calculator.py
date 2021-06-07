#!/usr/bin/env python3
import datetime
timestamp = datetime.datetime.now().strftime("%Y-%m-%d hat %H:%M:%S")
print (timestamp)

self_employed_tax = .15

# grab the type of transaction
print()
payment_type = input('Is this an Invoice, Reader, or a Card On File? ')

if payment_type.lower() == 'invoice':
    # squares invoice fee is 2.9% + .30
    square_fee_percent = .029
    square_fee_cents = .30
    # the amount you want to actually be paid for your work
    print()
    amount_desired = input('How much do you want to be paid? $')
    print()
    # subtract the current tax rate from 1
    amount_with_tax = float(amount_desired) / (1 - self_employed_tax)
    # we'll add the cents and subtract the percent fee from 1 
    amount_to_charge = (amount_with_tax + square_fee_cents) / (1 - square_fee_percent)
    irs_cut = amount_with_tax - float(amount_desired)
    square_cut = amount_to_charge - amount_with_tax
    print('If you want to be paid $' + amount_desired + ', you should charge: $' + ("{:0.2f}".format(amount_to_charge)))
    print()
    print('$' + ("{:0.2f}".format(irs_cut)) + ' goes to the IRS and $' + ("{:0.2f}".format(square_cut)) + ' goes to Square')
    print()
elif payment_type.lower() in ('tap', 'chip', 'swipe', 'reader'):
    # squares reader fee is 2.6% + .10
    square_fee_percent = .026
    square_fee_cents = .10
    # the amount you want to actually be paid for your work
    print()
    amount_desired = input('How much do you want to be paid? $')
    print()
    # subtract the current tax rate from 1
    amount_with_tax = float(amount_desired) / (1 - self_employed_tax)
    # we'll add the cents and subtract the percent fee from 1
    amount_to_charge = ((amount_with_tax + square_fee_cents) / (1 - square_fee_percent))
    irs_cut = amount_with_tax - float(amount_desired)
    square_cut = amount_to_charge - amount_with_tax
    print('If you want to be paid $' + amount_desired + ', you should charge: $' + ("{:0.2f}".format(amount_to_charge)))
    print()
    print('$' + ("{:0.2f}".format(irs_cut)) + ' goes to the IRS and $' + ("{:0.2f}".format(square_cut)) + ' goes to Square')
    print()
elif payment_type.lower() in ('card on file', 'on file', 'saved', 'stored', 'on-file', 'cof', 'c-o-f', 'card on', 'other'):
    # squares invoice fee is 3.5% + .15
    square_fee_percent = .035
    square_fee_cents = .15
    # the amount you want to actually be paid for your work
    print()
    amount_desired = input('How much do you want to be paid? $')
    print()
    # subtract the current tax rate from 1
    amount_with_tax = float(amount_desired) / (1 - self_employed_tax)
    # we'll add the cents and subtract the percent fee from 1
    amount_to_charge = ((amount_with_tax + square_fee_cents) / (1 - square_fee_percent))
    irs_cut = amount_with_tax - float(amount_desired)
    square_cut = amount_to_charge - amount_with_tax
    print('If you want to be paid $' + amount_desired + ', you should charge: $' + ("{:0.2f}".format(amount_to_charge)))
    print()
    print('$' + ("{:0.2f}".format(irs_cut)) + ' goes to the IRS and $' + ("{:0.2f}".format(square_cut)) + ' goes to Square')
    print() 
else:
    print('\nSorry, transaction type ' + '"' + payment_type + '"' ' not found. \nPlease correct and try again.\n') #double quotes for emphasis