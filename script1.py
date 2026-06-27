#a = int(input())
#b = int(input())

#p = 2*(a+b)
#s = a*b
#print(p)
#print(s)

#x = int(input())
#y = ((2*x)/ (x**2 + 1)**0.5) - ((x**2 + 1)**0.5 / x**3)
#print(y)


#y = int(input())
#x = int(input())
#z = ((x**2 + y**2)**0.5) / ((x - y)**2) - (2*y*x) / ((x**2 + y**2)**0.5)
#print(z)

#n = int(input())

#s = n // 100        # Сотні (3)
#d = (n // 10) % 10  # Десятки (4)
#o = n % 10          # Одиниці (5)

#sum = (s + o +d)
#print(sum)

#print("Сотні:", s)
#print("Десятки:", d)
#print("Одиниці:", o)

import math
#n = int(input())
#word  = input()
#for i in range(n):
 #   print (f"- {word}")

#k = int(input())
#print (math.ceil( k//8 ))

#body = int(input())
#rate = float(input())
#t = int(input())
#a = body * (math.e)**(rate/100)*t
#print(a)


#x1, y1 = map(int, input("Enter warehouse coordinates (x y):").split())
#x2, y2 = map(int, input("Enter customer coordinates (x y):").split())
#base_cost = int(input("Enter base fee (USD):"))
#per_km_rate = int(input("Enter rate per km (USD):"))

#d = ((x2-x1)**2+(y2-y1)**2)**(1/2)
#cost = (base_cost + d*per_km_rate)
#print (f"Distance: {(round(d, 2))} km. Final delivery cost: {math.ceil(cost)} USD")



#a, b = map(float, input().split())
#if b % a == 0:
#    print ("1")
#else:
#    print ("0")

#a, b, c = map(int, input().split())
#if b == c or a == b or a == c:
#    print (a+b+c)
#else:
#    print ("NO")

#a = int(input())
#if a > 0 and a % 2 == 0 or a < 0 and a % 2 != 0:
#    print ("No")
#else:
#    print("Yes")


#a = int(input())
#if  0 < a < 10000:
#    print (f"Calculated income tax: 0.00 USD")
#elif  10000.01 < a < 50000:
#    print (f"Calculated income tax: {(a - 10000)/ 100 * 15} USD")
#elif   a > 50000:
#    print (f"Calculated income tax: {6000 + (a - 50000)/ 100 * 25} USD")


#stock_price = float(input("Enter current stock price (USD):"))
#mov_a = float(input("Enter 50-day moving average (USD):"))
#RSI = float(input("Enter RSI value (0-100):"))

#if stock_price >= mov_a and stock_price >= 70:
#    print ("SELL (Overbought).")
#elif stock_price <= mov_a and stock_price <= 30:
#    print ("BUY (Oversold)")
#else:
#    print("Hold")


#string = "i love"
#for ch in string:
#    print(ch)


#transactions = [150.5, 2000.0, 35.0, 400.25]
#for i in range(0, len(transactions)):
#    i = transactions[i]
#    print(f"Сума транзакції: {i}")


#messy_companies = ['  apple Inc.', 'GOOGLE ', ' tEsLa', ' microsoft  ']
#clean_companies = []
#for c in messy_companies:
#    c = c.strip()
#    c = c.title()
#    clean_companies.append(c)
#print(clean_companies)

#raw_emails = [' user1@kse.ua ', 'Admin@KSE.UA', '  guest@kse.ua', 'CEO@company.com  ']
#clean_emails = []
#for e in raw_emails:
#    e = e.strip().lower()
#    clean_emails.append(e)
#print(clean_emails)


#all_accounts = ["UA1234567890", "PL0987654321", "UA1111111111", "GB2222222222", "UA9999999999"]
#ukrainian_accounts = []
#for a in all_accounts:
 #   if a[:2] == "UA":
#        ukrainian_accounts.append(a)
#print(ukrainian_accounts)


#logs = [
  #   "ERROR: Не вдалося підключитися до бази даних",
#    "WARNING: Закінчується вільне місце",
#    "INFO: Оплата пройшла успішно",
#    "ERROR: Час очікування вичерпано"
#]
#for bug in logs:
#    if bug[:5]=="ERROR":
#        print(bug)

#raw_prices = ["$1,250.50", "300.00", "$4,500.25", "$50.00"]
#total_revenue = 0
#clean_prices = []
#for r in range(len(raw_prices)):
#    new_text = raw_prices[r].replace(",", "")  # 1. Прибираємо кому з оригіналу
 #   new_text = new_text.replace("$", "")       # 2. Прибираємо $ з того, що вийшло
#    clean_prices.append(new_text)
#    total_revenue += float(clean_prices[r])

#print(total_revenue)


#csv_records = [
#    "2023-10-01,AAPL,150.25",
#    "2023-10-01,MSFT,310.15",
#    "2023-10-01,TSLA,240.50"
#]
#for i  in csv_records:
  #  i=i.split(",")
 #   print(f"Компанія: {i[1]}, Ціна: {i[2]}")


import sys

# sys.argv — це список рядків (аргументів), які передали при запуску!
# sys.argv[0] — це назва самого файлу, а sys.argv[1] — перший аргумент
#print(f"Генерую звіт за рік: {sys.argv[1]}")

#a = input()
#new_a = a.split(" ")
#b = 0

#for i in range(len(new_a)):
#    new_a[i] = float(new_a[i])

#for i in range(len(new_a)):
#    if new_a[i]  != 0:
#        b += 1

#print (b)



#a = input()
#new_a = a.split(" ")
#a = 0

#for i in range(len(new_a)):
#    new_a[i] = float(new_a[i])


#for i in range(len(new_a)):
#    if new_a[i]  % 2 == 0:
#        a += new_a[i]
#print (a)

#total_r = 0
#n = int(input("Enter a number: "))
#for i in range (1, n+1):
#    rev = int(input(f"Enter revenue for month {i}:"))
#    total_r += rev
#print (f"Total revenue: {total_r} USD")
#print (f"Average revenue: : {round(total_r/n, 2)} USD")

#a, b = map(int, input().split())
#for i in range (1, a+1):
#    print ("#"*b)


#n = int(input("Enter a number: "))
#a = 1
#numbers = [a]
#for i in range (1, n+1):
#    a += 2
#    numbers.append(a)
#print (*numbers, sep=' ')


#principal = float(input("Enter principal amount (USD):"))
#annual_interest_rate = float(input("Enter annual interest rate (in percent):"))
#target_amount = float(input("Enter target amount (USD):"))
#years = 0
#if principal >= target_amount:
#    print("Target reached in 0 years")
#else:
#while (target_amount >= principal):
#    principal += principal * (annual_interest_rate//100)
#    years  = years + 1
#print(f"Target reached in {years} years")

#n = int(input())
#new_list = []
#int_list = []
#numbers = input().split()
#for i in numbers:
#    int_list.append(int(i))
#for i in int_list:
#    if i % 2 == 0:
#        new_list.append(i)
#if new_list == []:
#    print("NO")
#else:
#    print(len(new_list))

   # print(*new_list[::-1], sep=' ')


#n = int(input())
#new_list = []
#int_list = []
#small_list = []
#numbers = list(map(int, input().split()))
#for i in  numbers:
#    if i < 0:
#        small_list.append(i)
#        small_list.sort()
#if small_list == []:
#    print ("NO")
#else:
#    print (len(small_list))
#    print (small_list[0])

#n = input()
#a, b = map(int, input().split())

#V = n.replace(n[a:b], "")
#print(V)

new = input()
final_world  = ""
for i  in new:
      print(i)
      final_world += (i*2)
print (final_world)

