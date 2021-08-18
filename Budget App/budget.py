class Category:

    def __init__(self, kind):
        self.ledger = []
        self.kind = kind

    def get_balance(self):
        funds = 0
        for x in self.ledger:
            funds = funds + x["amount"]

        return funds

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False

        return True

    def deposit(self, amount, description=""):
        newObj = {}
        newObj["amount"] = amount
        newObj["description"] = description
        self.ledger.append(newObj)

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            newObj = {}
            newObj["amount"] = -1 * amount
            newObj["description"] = description
            self.ledger.append(newObj)
            return True

        return False

    def transfer(self, amount, otherCat):
        if self.check_funds(amount):
            txt = "Transfer to {}"
            txt = txt.format(otherCat.kind)
            self.withdraw(amount, txt)
            txt = "Transfer from {}"
            txt = txt.format(self.kind)
            otherCat.deposit(amount, txt)
            return True

        return False

    def __str__(self):
        # first line
        first = last = []
        for x in range(30):
            first.append("*")
        start = 30 - len(self.kind)
        start = int(start/2)

        for x in str(self.kind):
            first[start] = str(x)
            start += 1

        # last line
        total = self.get_balance()
        last = "Total: {:.2f}"
        last = last.format(total)

        # middle
        key = []
        middle = []
        value = "{:.2f}"

        for x in self.ledger:
            key = []
            description = x["description"][:23]
            key.append(description)

            money = value.format(x["amount"])

            spaces = " " * (30 - len(money) - len(description))
            key.append(spaces)
            key.append(money)

            key = "".join(key)
            middle.append(key)

        # joining answer and returning string
        answer = "".join(first)

        for x in middle:
            answer = answer + "\n" + x

        answer = answer + "\n" + "".join(last)
        return answer


def create_spend_chart(categories):

    # first line
    answer = "Percentage spent by category" + "\n"

    # calculating percentage spent by each category
    perc = []
    total = 0

    for x in categories:
        sum = 0
        for y in x.ledger:
            if y["amount"] < 0:
                sum += y["amount"]
                total += sum
        sum *= -1
        perc.append(sum)

    total = 0
    for x in perc:
        total += x
    i = 0
    for y in perc:
        perc[i] = 100 * y/total
        i += 1

    # add percentage lines
    current = 100
    while current >= 0:
        line = ""
        if current != 100:
            line += " "
        if current == 0:
            line += " "
        line += str(current) + "| "
        for y in perc:
            if y > current:
                line += "o  "
            else:
                line += 3 * " "
        line += "\n"
        answer += line
        current -= 10

    # create line of dashes
    dash = 4 * " "
    dash = dash + "----"
    dash = dash + ("---" * (len(categories) - 1))

    answer += dash + "\n"

    # add name of categories to answer
    large = 0
    for x in categories:
        if len(x.kind) > large:
            large = len(x.kind)

    for x in range(large):
        answer += 5 * " "
        letter = ""
        for y in categories:
            try:
                letter = y.kind[x]
            except Exception:
                answer += 3 * " "
            else:
                answer += letter + (2 * " ")
        if x != large - 1:
            answer += "\n"

    # returns string
    return answer
