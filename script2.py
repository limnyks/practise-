import tkinter as tk

# Наша база карток (Тема: Програмування)
flashcards = [
    {"q": "Що поверне оператор 5 // 2 у Python?", "a": "2 (Цілочисельне ділення, округлює вниз)"},
    {"q": "Який оператор знаходить остачу від ділення?", "a": "% (Наприклад, 5 % 2 дасть 1)"},
    {"q": "Що робить оператор `break` у циклах?", "a": "Повністю зупиняє виконання циклу та виходить із нього"},
    {"q": "Що поверне індекс мого_списку[-1]?", "a": "Останній елемент списку"},
    {"q": "Чи можна змінити один символ у рядку типу `text[0] = 'A'`?", "a": "Ні, рядки в Python є незмінними (immutable)"}
]

current_card = 0
show_answer = False

def update_card():
    global show_answer
    show_answer = False
    card_label.config(text=f"ЗАПИТАННЯ:\n\n{flashcards[current_card]['q']}", bg="#e6f2ff")

def flip_card():
    global show_answer
    if not show_answer:
        card_label.config(text=f"ВІДПОВІДЬ:\n\n{flashcards[current_card]['a']}", bg="#e6ffe6")
        show_answer = True
    else:
        update_card()

def next_card():
    global current_card
    current_card = (current_card + 1) % len(flashcards)
    update_card()

# Налаштування графічного вікна
root = tk.Tk()
root.title("Флеш-картки: Python Basics")
root.geometry("400x300")

card_label = tk.Label(root, text="", font=("Arial", 14), width=35, height=8, relief="solid", wraplength=300)
card_label.pack(pady=20)

btn_flip = tk.Button(root, text="Перевернути", font=("Arial", 12), command=flip_card)
btn_flip.pack(side="left", padx=40)

btn_next = tk.Button(root, text="Наступна ➡️", font=("Arial", 12), command=next_card)
btn_next.pack(side="right", padx=40)

update_card()
root.mainloop()