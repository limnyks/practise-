def cul_profit(rev, cost):
    if cost > rev:
        return (rev - cost)  - (rev - cost * 0.18)
rev = 500000
fi_cost = 3500000

net = cul_profit(rev, fi_cost)

def cred(income, debt):
    if  income <= 0:
        return "Refuse: noot enough funds"
    credit_load = (debt / income ) * 100
    if credit_load > 40:
        return False
    else:
        return True
income = 10000
debt = 500000


if cred(income, debt):
    print("Credit Card is valid")
else:
    print("Credit Card is not valid")


def conv(amount, rate, fee = 0):
    total_sum = amount * rate
    fee_sum = total_sum - fee
    return total_sum - fee_sum

suma = 1000
ratee = 45

print(f"Your money is {conv(suma, ratee, 0.5)}")

conv (10000, 0.05)



def bonus(sum_s, bon_rate, bon_m=1500):
    if (sum_s*bon_rate) < bon_m:
        return bon_m
    else:
        return sum_s*bon_rate

bonus_f = bonus(50000, 0.05)
print(f"Your bonus is {bonus_f}")

bonus_f = bonus(10000, 0.05, bon_m = 3000 )
print(f"Your bonus is {bonus_f}")


def calculate_total(*args):
    total_bonus = 0

    for n in args:
        if n < 10000:
            total_bonus += 0
        elif 10000 <= n <= 50000:
            total_bonus += n * 0.05
        elif n > 50000:
            total_bonus += n * 0.1


    return total_bonus

calculate_total(5000, 12000, 60000, 8000)
print(f"Your total is {calculate_total(5000, 12000, 60000, 8000)}")
