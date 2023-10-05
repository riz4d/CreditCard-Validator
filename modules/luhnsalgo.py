def is_valid_credit_card(card_number):
    card_digits = [int(digit) for digit in str(card_number)][::-1]
    for i in range(1, len(card_digits), 2):
        card_digits[i] *= 2
        if card_digits[i] > 9:
            card_digits[i] -= 9
    total_sum = sum(card_digits)
    return total_sum % 10 == 0
