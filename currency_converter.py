class CurrencyConverter:
    # Exchange rates relative to USD as a baseline
    RATES = {
        "USD": 1.0,
        "EUR": 0.92,
        "GBP": 0.79,
        "INR": 83.12,
        "JPY": 150.50,
        "CAD": 1.35
    }

    @classmethod
    def convert(cls, amount, from_currency, to_currency):
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        if from_currency not in cls.RATES or to_currency not in cls.RATES:
            raise ValueError("Unsupported currency code.")

        # Convert amount to USD first, then to target currency
        amount_in_usd = amount / cls.RATES[from_currency]
        converted_amount = amount_in_usd * cls.RATES[to_currency]
        return converted_amount


if __name__ == "__main__":
    print("=== Currency Converter ===")
    print(f"Available currencies: {', '.join(CurrencyConverter.RATES.keys())}")

    try:
        amt = float(input("Enter amount to convert: "))
        from_curr = input("From currency (e.g., USD, INR): ")
        to_curr = input("To currency (e.g., EUR, GBP): ")

        result = CurrencyConverter.convert(amt, from_curr, to_curr)
        print(f"\n{amt:.2f} {from_curr.upper()} = {result:.2f} {to_curr.upper()}")
    except ValueError as e:
        print(f"Error: {e}. Please enter valid numbers and currency codes.")
