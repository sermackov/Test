def main():
    print("=== Простой калькулятор ===")
    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        op = input("Выберите операцию (+, -, *, /, ^): ")

        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '*':
            result = a * b
        elif op == '/':
            if b == 0:
                print("Ошибка: деление на ноль!")
                return
            result = a / b
        elif op == '**' or op == '^':
            result = a ** b
        else:
            print("Неизвестная операция!")
            return

        print(f"Результат: {a} {op} {b} = {result}")
    except ValueError:
        print("Пожалуйста, вводите только числа.")

if __name__ == "__main__":
    main()