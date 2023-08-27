## Currency_Converter.py
def convert_currency(amount, exchange_rate):
    converted_amount = amount * exchange_rate
    return converted_amount

print("Enter the exchange: ")
print("1.INR to USD")
print("2.INR to EURO")
print("3.INR to DIRHAM")

choice = int(input("Enter the choice of currency exchange: "))
inr_amount = float(input("Enter the amount: "))

if choice == 1:
    exchange_rate = 0.012
    converted_amount = convert_currency(inr_amount, exchange_rate)
    print(f"Equivalant amount in USD is: {converted_amount} Dollars")

if choice == 2:
    exchange_rate = 0.011
    converted_amount = convert_currency(inr_amount, exchange_rate)
    print(f"Equivalant amount in EURO is: {converted_amount} Euros")

if choice == 3:
    exchange_rate = 0.044
    converted_amount = convert_currency(inr_amount, exchange_rate)
    print(f"Equivalant amount in DIRHAM is: {converted_amount} Dirhams")

