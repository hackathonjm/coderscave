class ExpenseTracker:
    def __init__(self):
        self.expenses = {}
        self.balance = {}

    def add_expense(self, payer, amount, participants):
        if payer not in self.balance:
            self.balance[payer] = 0

        share = amount / len(participants)
        for participant in participants:
            if participant != payer:
                if participant not in self.balance:
                    self.balance[participant] = 0
                self.balance[participant] -= share
                self.balance[payer] += share

        if payer not in self.expenses:
            self.expenses[payer] = []
        self.expenses[payer].append({"amount": amount, "participants": participants})

    def print_balance(self):
        print("Balance:")
        for person, amount in self.balance.items():
            print(f"{person}: ${amount:.2f}")

    def print_expenses(self):
        print("Expenses:")
        for payer, transactions in self.expenses.items():
            for transaction in transactions:
                amount = transaction["amount"]
                participants = ", ".join(transaction["participants"])
                print(f"{payer} paid ${amount:.2f} for {participants}")

def main():
    tracker = ExpenseTracker()

    while True:
        print("\n1. Add expense")
        print("2. Print balance")
        print("3. Print expenses")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            payer = input("Enter payer's name: ")
            amount = float(input("Enter the expense amount: "))
            participants = input("Enter participants (comma-separated): ").split(", ")
            tracker.add_expense(payer, amount, participants)
        elif choice == "2":
            tracker.print_balance()
        elif choice == "3":
            tracker.print_expenses()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
