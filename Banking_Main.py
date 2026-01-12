# Banking Application Main Module

# Imports
import json
import CBbox


class Transaction():

    def __init__(self, trans_title, trans_amount, trans_type, trans_note=""):

        self.transaction_title = trans_title
        self.amount = trans_amount
        self.transaction_type = trans_type
        self.transaction_note = trans_note

    # Display Transaction Info
    def display_info(self):

        return f"{self.transaction_title}, Amount: {self.amount}, Type: {self.transaction_type}, Note: {self.transaction_note}"


class BankingApp():

    def __init__(self):

        self.cust_wallet = []

    # Add Transaction
    def add_transaction(self, transaction):

        self.cust_wallet.append(transaction)

    # Remove Transaction
    def remove_transaction(self, trans_title):

        for trans in self.cust_wallet:

            if trans.transaction_title.lower() == trans_title.lower():

                self.cust_wallet.remove(trans)

                return f"Transaction {trans_title} removed."

        return f"Transaction {trans_title} not found."

    # Display Transactions
    def display_transactions(self):

        if not self.cust_wallet:

            return "No transactions available."

        return f"\n".join([trans.display_info() for trans in self.cust_wallet])

    # Search Transaction
    def search_transaction(self, query):

        results = [trans for trans in self.cust_wallet if query.lower(
        ) in trans.transaction_title.lower() or query.lower() in trans.transaction_type.lower()]

        if not results:

            return "No matching transactions found."

        return f"\n".join([trans.display_info() for trans in results])

    # Save Transactions to File
    def save_transactions(self, filename="transactions.json"):

        data = [{"Transaction": trans.transaction_title, "Amount": trans.amount,
                 "Type": trans.transaction_type, "Note": trans.transaction_note} for trans in self.cust_wallet]

        with open(filename, "w") as file:

            json.dump(data, file, indent=4)

    # Load Transactions from File
    def load_transactions(self, filename="transactions.json"):

        try:

            with open(filename, "r") as file:

                data = json.load(file)

                self.cust_wallet = [Transaction(
                    trans["Transaction"], trans["Amount"], trans["Type"], trans["Note"]) for trans in data]

        except FileNotFoundError:

            print("File Not Found...")

        except Exception:

            print("An error occurred while loading transactions.")


bank_menu = [" --- Banking Application Menu ---",
             "                                 ",
             "1. Add Transaction",
             "2. Remove Transaction",
             "3. Display Transactions",
             "4. Search Transaction",
             "5. Save Transactions",
             "6. Load Transactions",
             "7. Exit"]

# Main Function
def main():

    account = BankingApp()


    while True:

        CBbox.d_box(bank_menu)

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            title = str(input("Enter transaction title: "))
            amount = float(input("Enter amount: "))
            type = str(input("Enter transaction type 1. Credit  2. Debit): "))

            if type == "1":
                type = "Credit"

            elif type == "2":
                type = "Debit"

            else:
                print("Invalid transaction type. Please try again.")
                continue

            note = str(input("Enter transaction note (optional): "))
            transaction = Transaction(title, amount, type, note)
            account.add_transaction(transaction)

            print("Transaction added successfully.")

        elif choice == "2":
            title = str(input("Enter transaction title to remove: "))
            print(account.remove_transaction(title))

        elif choice == "3":
            print("Transactions:")

            CBbox.d_box(["--- Transactions List ---"] +
                        account.display_transactions().split("\n"))

        elif choice == "4":
            query = str(input("Enter search query: "))
            print("Search Results:")
            print(account.search_transaction(query))

        elif choice == "5":
            account.save_transactions()
            print("Transactions saved successfully.")

        elif choice == "6":
            account.load_transactions()
            print("Transactions loaded successfully.")

        elif choice == "7":
            print("Exiting the application. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
