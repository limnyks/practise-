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