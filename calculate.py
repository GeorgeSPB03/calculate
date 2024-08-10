
import tkinter as tk
import math

# Функция для вычисления выражений
def evaluate_expression(expression):
    try:
        # Заменим '^' на '**' для возведения в степень
        expression = expression.replace('^', '**')
        result = eval(expression, {"__builtins__": None}, math.__dict__)
        return str(result)
    except Exception as e:
        return "Error"

# Функция обработки нажатия кнопок
def on_button_click(value):
    current_text = entry.get()
    if value == "=":
        result = evaluate_expression(current_text)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    elif value == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, value)

# Создание окна приложения
root = tk.Tk()
root.title("Engineering Calculator")

# Текстовое поле для ввода и отображения результата
entry = tk.Entry(root, width=40, borderwidth=5)
entry.grid(row=0, column=0, columnspan=5)

# Определение кнопок калькулятора
buttons = [
    '7', '8', '9', '/', 'sin',
    '4', '5', '6', '*', 'cos',
    '1', '2', '3', '-', 'tan',
    '0', '.', '=', '+', 'log',
    '(', ')', '^', '√', 'C'
]

# Добавление кнопок на экран
row = 1
col = 0
for button in buttons:
    action = lambda x=button: on_button_click(x)
    tk.Button(root, text=button, width=5, command=action).grid(row=row, column=col)
    col += 1
    if col > 4:
        col = 0
        row += 1

root.mainloop()
