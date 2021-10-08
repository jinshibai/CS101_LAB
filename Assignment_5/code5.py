txt = "Linda Hall"
txt1 = 'Library Card Check'
z = txt.center(40)
q = txt1. center(40)
print(z)
print(q)
print('='*40)


def library_card():
    library_card1 = input('Enter your library card number:')
    upp = library_card1.upper()
    print(upp)
    inv = 'Library card is invalid'
    length = len(library_card1)
    if length != 10:
        print(inv)
        print("The number of length given must be 10. Please try again.")
        return library_card()
    f5 = library_card1[0:5]
    x = f5.isnumeric()
    if x is True:
        print(inv)
        print('The first characters must be A-Z, please try again.')
        return library_card()
    f6 = library_card1[5]
    if f6 != '1' and f6 != '2' and f6 != '3':
        print(inv)
        print('The sixth character must be 1, 2 or 3, Please try again.')
        return library_card()
    f7 = library_card1[6]
    if f7 != '1' and f7 != '2' and f7 != '3' and f7 != '4':
        print(inv)
        print('The seventh character must be 1,2,3 or 4, please try again.')
        return library_card()
    f8 = library_card1[8:11]
    y = f8.isnumeric()
    if y is False:
        print(inv)
        print('The eighth, ninth, and tenth characters must be integers from 0-9, please enter again.')
        return library_card()
    while True:
        if f6 == '1':
            f6 = 'School of computing'
        if f6 == '2':
            f6 = 'School of law'
        if f6 == '3':
            f6 = 'College of art and science'
        if f7 == '1':
            f7 = 'freshman'
        if f7 == '2':
            f7 = 'sophomore'
        if f7 == '3':
            f7 = 'junior'
        if f7 == '4':
            f7 = 'senior'
        print('Library card is valid.')
        print('The library card belongs to a student in', f6+'.\n''This card belongs to a', f7+'.')
        break


library_card()