from Invoice import Invoice

products = {}
total_amount = 0
repeat = ''
while True:
    product = input('What is your product : ')
    unit_price = Invoice().inputNumber("Please enter unit price : ")
    qnt = Invoice().inputNumber("Please enter amount of product : ")
    discount = Invoice().inputNumber("Discount percent (%) : ")
    tax = Invoice().inputNumber("Tax percent (%) : ")
    repeat = Invoice().inputAnswer("Another  product? (y,n) : ")
    result = Invoice().addProduct(qnt, unit_price, discount, tax)
    products[product] = result
    if repeat == "n":
        break

pre_tax_total_amount = Invoice().totalPurePrice(products)
post_tax_total_amount = Invoice().totalWithTaxPrice(products)
print("Your total price before tax is: ", pre_tax_total_amount)
print("Your total price after tax is: ", post_tax_total_amount)
