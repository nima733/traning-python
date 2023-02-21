def rials_dollars(money):
    dollars = money * 0.000024
    print(dollars)


def dollar_rials(money):
    rial = money * 42250.00
    print(rial)


try:
    user_choice = int(input('choice rials to dollar (enter 1)'
                            ' and convert dollar to rails (enter 2): '))
    if user_choice == 1:
        rials = float(input('Enter amount in rial: '))
        rials_dollars(rials)
    elif user_choice == 2:
        dollar = float(input('Enter amount in dollar'))
        dollar_rials(dollar)
except ValueError:
    print('enter int number')

else:
    print("your input is not correct")
