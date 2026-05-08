class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({
            "amount": amount,
            "description": description
        })

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):

            self.ledger.append({
                "amount": -amount,
                "description": description
            })

            return True

        return False

    def get_balance(self):
        total = 0

        for item in self.ledger:
            total += item["amount"]

        return total

    def transfer(self, amount, category):

        if self.check_funds(amount):

            self.withdraw(
                amount,
                f"Transfer to {category.name}"
            )

            category.deposit(
                amount,
                f"Transfer from {self.name}"
            )

            return True

        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):

        title = self.name.center(30, "*") + "\n"

        items = ""

        for item in self.ledger:

            description = item["description"][:23]
            amount = f"{item['amount']:.2f}"

            items += f"{description:<23}{amount:>7}\n"

        total = f"Total: {self.get_balance()}"

        return title + items + total


def create_spend_chart(categories):

    withdrawals = []

    total_spent = 0

    for category in categories:

        spent = 0

        for item in category.ledger:

            if item["amount"] < 0:
                spent += abs(item["amount"])

        withdrawals.append(spent)

        total_spent += spent

    percentages = []

    for amount in withdrawals:
        percent = int((amount / total_spent) * 100)

        percentages.append(percent - (percent % 10))

    chart = "Percentage spent by category\n"

    for i in range(100, -1, -10):

        chart += f"{i:>3}|"

        for percent in percentages:

            if percent >= i:
                chart += " o "
            else:
                chart += "   "

        chart += " \n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_length = 0

    for category in categories:

        if len(category.name) > max_length:
            max_length = len(category.name)

    for i in range(max_length):

        chart += "     "

        for category in categories:

            if i < len(category.name):
                chart += category.name[i] + "  "
            else:
                chart += "   "

        if i != max_length - 1:
            chart += "\n"

    return chart


# working ex
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

clothing = Category("Clothing")
food.transfer(50, clothing)

auto = Category("Auto")
auto.deposit(1000)
auto.withdraw(150)

print(food)

print(create_spend_chart([food, clothing, auto]))
