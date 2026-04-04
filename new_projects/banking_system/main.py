from bankmanager import BankManager, AccountIDError
from accounts import InsufficientFundsError


def get_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def main():
    manager = BankManager()
    print("Welcome to the Banking Management System")

    while True:
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                name = input("Customer name: ")
                amount = get_float("Initial deposit: ")
                account = manager.create_account(name, amount)
                print(f"Account created. ID: {account.account_number}")

            elif choice == "2":
                acc_id = input("Account ID: ")
                amount = get_float("Deposit amount: ")
                print("New balance:", manager.deposit(acc_id, amount))

            elif choice == "3":
                acc_id = input("Account ID: ")
                amount = get_float("Withdrawal amount: ")
                print("New balance:", manager.withdraw(acc_id, amount))

            elif choice == "4":
                acc_id = input("Account ID: ")
                print("Balance:", manager.get_balance(acc_id))

            elif choice == "5":
                print("Goodbye!")
                break

            else:
                print("Invalid option.")

        except (AccountIDError, InsufficientFundsError, ValueError) as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
