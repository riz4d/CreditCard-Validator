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