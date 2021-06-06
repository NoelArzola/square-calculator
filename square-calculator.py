# grab the type of transaction
print()
payment_type = input('Is this an Invoice, Reader, or a Card On File? ')

if payment_type.lower() == 'invoice':
    # the amount you want to be paid for your work
    print()
    amount_desired = input('How much do you want to be paid? $')
    print()
    # current tax rate is 15%, 1 - .15 is .85 
    # we use .85 to calculate how to be paid that amount, taking taxes into account
    amount_with_tax = float(amount_desired) / .85
    # squares invoice fee is 2.9% + .30
    # we'll add .30 (the 30 cents) and subtract .029 (2.9%) from 1 to get .971
    amount_to_charge = ((amount_with_tax + .30) / .971)
    print('If you want to be paid $' + amount_desired + ', you should charge: $' + ("{:0.2f}".format(amount_to_charge)))
    print()
elif payment_type.lower() in ('tap', 'chip', 'swipe', 'reader'):
    # the amount you want to be paid for your work
    print()
    amount_desired = input('How much do you want to be paid? $')
    print()
    # current tax rate is 15%, 1 - .15 is .85 
    # we use .85 to calculate how to be paid that amount, taking taxes into account
    amount_with_tax = float(amount_desired) / .85
    # squares invoice fee is 2.6% + .10
    # we'll add .10 (the 10 cents) and subtract .026 (2.6%) from 1 to get .974
    amount_to_charge = ((amount_with_tax + .10) / .974)
    print('If you want to be paid $' + amount_desired + ', you should charge: $' + ("{:0.2f}".format(amount_to_charge)))
    print()
elif payment_type.lower() in ('card on file', 'on file', 'saved', 'stored', 'on-file', 'cof', 'c-o-f', 'card on', 'other'):
    # the amount you want to be paid for your work
    print()
    amount_desired = input('How much do you want to be paid? $')
    print()
    # current tax rate is 15%, 1 - .15 is .85 
    # we use .85 to calculate how to be paid that amount, taking taxes into account
    amount_with_tax = float(amount_desired) / .85
    # squares invoice fee is 3.5% + .15
    # we'll add .15 (the 15 cents) and subtract .035 (3.5%) from 1 to get .965
    amount_to_charge = ((amount_with_tax + .10) / .965)
    print('If you want to be paid $' + amount_desired + ', you should charge: $' + ("{:0.2f}".format(amount_to_charge)))
    print()
else:
    print(payment_type)
    print(payment_type.lower())
    print("Sorry, transaction type not found. \nPlease correct and try again.") #double quotes due to an apostrophe in the string