
capital = 50000
monthly_expenses = 15000
for i in range(1, 13):
    if (capital - monthly_expenses) > 0:
        capital -= monthly_expenses
        print(i)
        print(capital)
    elif capital < 0:
        print("Mu bankrytu")
        break

deposit = 10000
interest_rate = 0.12
years = 5
for i in range(1, years+1):
    deposit += deposit * interest_rate
    print(f"Рік {1}: на рахунку {round (deposit, 2) } грн")

base_revenue = 50000
growth_per_month = 2000
bonus_rate = 0.10

for i in range(3, 12+1, 3):
    bonus = bonus_rate*(base_revenue+growth_per_month*i)
    print(f"Місяць {i}: виторг = {base_revenue+(growth_per_month*3)},  премія = {bonus}")


portfolio = ["Apple", "Intel", "Microsoft", "Netflix"]
portfolio [1] = "Nvidia"
portfolio.append("Amazon")
print  (portfolio)
print  (len(portfolio))


transactions = [300, 150, 45, 800, 120]
transactions[0] = 0
transactions.append(1500)
print(transactions[-3:])

n = int(input())
word_list = input()
result = word_list.split()
new_list = list(result)

int_list = list(map(int, new_list))
a = 0
for i in range(1, len(int_list)):
    if int_list[i] % 2 == 0:
        if int_list[i] > a:
             a = int_list[i]
if a > 0:
    print(a)
else:
    print("Nan")