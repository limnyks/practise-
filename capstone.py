TAX_RATE = 0.20

def apply_tax(price):
    # ВАШ КОД: поверніть ціну з доданим податком TAX_RATE
    total_price = price+ price * TAX_RATE
    return total_price
prices = []
print("=== Касовий Апарат ===")
print("Введіть ціни товарів. Щоб завершити чек, введіть 0.")

while True:
    user_input = int(input("Ціна: "))
    if user_input == 0:
        break
    prices.append(user_input)

print(f"\nСирі дані з каси: {prices}")

# ==========================================
# ОБРОБКА ДАНИХ
# ==========================================
# 3. Використайте map() та вашу функцію apply_tax,
# щоб розрахувати ціни з податком для всіх товарів у списку prices
price_with_tax = list(map(apply_tax, prices))

# 4. Використайте filter() та lambda,
# щоб залишити ТІЛЬКИ ті ціни, які більші за 100
final_prices = list(filter(lambda x: x > 100, price_with_tax))

# 5. Розрахуйте загальну суму чека
total_amount = sum(final_prices)


print(f"Ціни з урахуванням податків {price_with_tax}")
print(f"Фінальні ціни у чеку: {final_prices}")
print(f"До сплати: {total_amount}")