def luhn_checker(card_number):
    card_number = list(map(int, str(card_number)))
    for i, digit in enumerate(card_number[::-1]):
        if i % 2 != 0:
            digit = digit*2
            if digit > 9:
                digit = int(str(digit)[0]) + int(str(digit)[1])
            card_number[-i-1] = digit
    return sum(card_number) % 10 == 0

