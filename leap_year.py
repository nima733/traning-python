def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f'{year} is leap year')
            else:
                print(f'{year} is NOT leap year')
        else:
            print(f'{year} is leap year')
    else:
        print(f'{year} is NOT leap year')


leap_year(int(input('enter year: ')))
