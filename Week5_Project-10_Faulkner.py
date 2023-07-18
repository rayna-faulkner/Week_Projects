def calculate_payment_schedule(purchase_price):
    down_payment = purchase_price * 0.1
    balance = purchase_price - down_payment
    interest_rate = 0.12
    monthly_payment = (purchase_price - down_payment) * 0.05

    print("Tidbit Computer Store Lifetime Loan Payment Schedule")
    print("Month\tTotal Balance\tInterest\tPrincipal\tPayment\tRemaining Bal")

    month = 1
    while balance > 0:
        interest = balance * interest_rate / 12
        principal = monthly_payment - interest
        remaining_balance = balance - principal

        print(f"{month}\t{balance:.2f}\t\t{interest:.2f}\t\t{principal:.2f}\t\t{monthly_payment:.2f}\t{remaining_balance:.2f}")

        balance = remaining_balance
        month += 1

purchase_price = float(input("Please enter the purchase price: "))


calculate_payment_schedule(purchase_price)
