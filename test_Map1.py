income = [10, 30, 75]

def double_income(amount):
    return amount*2

new_income = list(map(double_income, income))
print(new_income)
