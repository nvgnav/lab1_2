def evc(a, b):
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    num1 = int(input("Введите число: "))
    num2 = int(input("Введите число: "))
    result = evc(num1, num2)
    print(f"Наибольший общий делитель {num1} и {num2} равен: {result}")