def luhn_checker(card_number):
    card_number = list(map(int, str(card_number)))
    for i, digit in enumerate(card_number[::-1]):
        print(f'{i} {digit}')
        if i%2 != 0:
            print(f'for {i} we go:')
            digit = digit*2
            print(f'digit*2 == {digit}')
            if digit > 9:
                print('digit > 9')
                digit = int(str(digit)[0]) + int(str(digit)[1])
                print(f'summed == {digit}')
            card_number[-i-1] = digit
            print(f'list changed {card_number}')
        print(card_number)
    return sum(card_number)%10 == 0


assert(luhn_checker(5488880257595687))

