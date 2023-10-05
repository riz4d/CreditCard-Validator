# CreditCard-Validator
 
Creditcard validator that uses the Luhn algorithm to verify the validity of credit card numbers. It also fetches credit card number data from datasets for testing and analysis.

### What's Luhn's Algorithm??
The Luhn algorithm, also known as the “modulus 10” or “mod 10” algorithm, is a simple checksum formula used to validate a variety of identification numbers, including credit card numbers, IMEI numbers (for mobile phones), and more. Its primary purpose is to check for errors in these numbers and detect typos or accidental mistakes when entering them.

#### Here’s how the Luhn algorithm works:

1.	Starting from the rightmost digit (the least significant digit) and moving left, double the value of every second digit. If doubling a digit results in a number greater than 9, subtract 9 from that number.<br>
2.	Sum all the digits in the modified number, along with the unmodified digits that were not doubled.<br>
3.	If the total sum is a multiple of 10 (i.e., the sum ends in 0), then the number is considered valid according to the Luhn algorithm. Otherwise, it’s invalid.<br>

### Features
- Validates credit card numbers using the Luhn algorithm.
- Fetches credit card number data from datasets

### Requirements
- Python 3.11.6
- pandas

### Usage
Install Dependencies with pip
```
pip install -r requirements.txt
```

run the script with

```
python3 run.py
```

here's a table that includes the CC issuing authority and IIN (Issuer Identification Number) ranges for the credit card networks:

| Issuing Authority                                    | IIN Ranges                            |
|-----------------------------------------------------|---------------------------------------|
| American Express                                     | 34, 37                                |
| Bankcard                                            | 5610, 560221–560225                   |
| BMO ABM Card                                        | 500, 5510                             |
| Canadian Imperial Bank of Commerce Advantage Debit Card | 4506                              |
| China T-Union                                       | 31                                    |
| China UnionPay                                      | 62, 81                                |
| Dankort                                            | 5019, 4571                           |
| Diners Club enRoute                                 | 2014, 2149                           |
| Diners Club International                            | 36, 300–305, 3095, 38–39             |
| Diners Club United States & Canada                   | 54, 55                               |
| Discover Card                                       | 6011, 622126 - 622925, 624000 - 626999, 628200 - 628899, 64, 65 |
| HSBC Bank Canada Card                               | 56                                    |
| InterPayment                                       | 636                                   |
| InstaPayment                                       | 637-639                               |
| JCB                                                | 3528–3589                            |
| LankaPay                                            | 357111                               |
| Laser                                               | 6304, 6706, 6771, 6709               |
| Maestro UK                                          | 6759, 676770, 676774                 |
| Maestro                                            | 50, 56–69                            |
| Mastercard                                         | 2221-2720, 51–55                     |
| MIR                                                | 2200–2204                            |
| NPS Pridnestrovie                                  | 6054740-6054744                       |
| Royal Bank of Canada Client Card                   | 45                                    |
| RuPay                                              | 60, 6521, 6522                       |
| Scotiabank Scotia Card                             | 4536                                 |
| Solo                                               | 6334, 6767                           |
| Switch                                             | 4903, 4905, 4911, 4936, 564182, 633110, 6333, 6759 |
| TD Canada Trust Access Card                       | 4724                                 |
| Troy                                               | 979200–979289                        |
| UATP                                               | 1                                    |
| UkrCard                                            | 6040, 6041                           |
| Visa                                               | 4                                    |
| Verve                                              | 506099–506198, 650002–650027         |


### License

This project is licensed under [MIT License](LICENSE).

