import pandas as pd
from modules.luhnsalgo import is_valid_credit_card
from modules.binfile import checkbin
import json
from datetime import datetime
while True:
    try:
        card_number = int(input("Enter Card Number: "))
        break
    except ValueError:
        print("Please enter a valid card number.")
try:
    check_luhn = is_valid_credit_card(card_number)
    def is_none(value):
        return value != "None"
except Exception as e:
    with open("logs/log.txt", "a") as log_file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"[{timestamp}] {e}\n")

    pass
if check_luhn == False:
    print("Card not satisfies luhns Algorithm")
try:
    is_bin_json = checkbin(str(card_number))

    for key, value in is_bin_json.items():
        if is_none(value):
            print(f"{key}: {value}")
except Exception as e:
    print(is_bin_json)
    error_message = is_bin_json
    with open("logs/log.txt", "a") as log_file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"[{timestamp}] {error_message}\n")

    pass

