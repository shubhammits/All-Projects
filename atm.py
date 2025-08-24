balance = 1000

while True:
    print("""
    Welcome to ATM Machine

    Choose Transaction

    1) BALANCE
    2) WITHDRAW
    3) DEPOSIT
    4) EXIT
    """)

    option = int(input("Enter Transaction: "))

    if option == 1:
        print("Your balance is:", balance)

    elif option == 2:
        withdraw = float(input("Enter amount to withdraw: "))
        if withdraw <= balance:
            balance -= withdraw
            print("✅ Withdrawal Successful")
            print("Your new balance is:", balance)
        else:
            print("❌ Insufficient Balance")

    elif option == 3:
        deposit = float(input("Enter amount to deposit: "))
        balance += deposit
        print("✅ Deposit Successful")
        print("Your new balance is:", balance)

    elif option == 4:
        print("Thank you for using ATM. Goodbye!")
        break

    else:
        print("❌ Invalid option. Please try again.")
1