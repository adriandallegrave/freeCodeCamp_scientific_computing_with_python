def create_spend_chart(categories):
    return True

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

    def deposit(self, amount, description = ""):
        newObj = {}
        newObj["amount"] = amount
        newObj["description"] = description
        self.ledger.append(newObj) 

    def withdraw(self, amount, description = ""):
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



'''
x = Category("Adrian")
z = Category("Dallegrave")

x.deposit(40, "teste")
x.withdraw(20, "saque")
x.transfer(10, "Dallegrave")

y = x

print(y)
'''






