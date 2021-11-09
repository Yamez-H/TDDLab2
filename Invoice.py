class Invoice:

    def __init__(self):
        self.items = {}

    def addProduct(self, qnt, price, discount, tax):
        self.items['qnt'] = qnt
        self.items['unit_price'] = price
        self.items['discount'] = discount
        self.items['tax'] = tax
        return self.items

    def totalImpurePrice(self, products):
        total_impure_price = sum(v['qnt'] * v['unit_price'] for v in products.values())
        return total_impure_price

    def totalDiscount(self, products):
        total_discount = sum((v['discount']/100) * v['qnt'] * v['unit_price'] for v in products.values())
        return total_discount

    def totalPurePrice(self, products):
        total_pure_price = self.totalImpurePrice(products) - self.totalDiscount(products)
        total_pure_price = round(total_pure_price, 2)
        return total_pure_price

    def totalWithTaxPrice(self, products):
        total_tax = 0
        for k, v in products.items():
            raw_price = v['qnt'] * v['unit_price']
            discount_price = raw_price - ((v['discount']/100) * raw_price)
            total_tax += discount_price * (v['tax']/100)
        total_with_tax = self.totalPurePrice(products) + total_tax
        total_with_tax = round(total_with_tax, 2)
        return total_with_tax

    def inputAnswer(self, input_value):
        while True:
            userInput = input(input_value)
            if userInput in ['y', 'n']:
                return userInput
                break
            print("y or n! Try again.")

    def inputNumber(self, input_value):
        while True:
            try:
                userInput = float(input(input_value))
            except ValueError:
                print("Not a number! Try again.")
                continue
            else:
                return userInput
                break
