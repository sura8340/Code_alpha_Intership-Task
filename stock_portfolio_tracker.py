print("=== Stock Portfolio Tracker ===")

stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420
}

total = 0

while True:
    stock = input("Enter Stock Name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock in stocks:
        quantity = int(input("Enter Quantity: "))
        value = stocks[stock] * quantity
        total += value
        print(f"{stock} Value = ₹{value}")
    else:
        print("Stock not found!")

print("--------------------------")
print("Total Investment = ₹", total)