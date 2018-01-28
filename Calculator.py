# -*- coding: utf-8 -*-
# програма Калькулятор
print "Вітаємо!"

# ця змінна скаже циклу зупинитися
loop = 1

# цю змінну ми використаємо для запамятовування Варіанту дії обраної користувачем
choice = 0

# використовуємо цикл 'while' який працюватиме доти доки змінна loop є 1
while loop == 1:

    # роздрукуємо користувачеві всеможливі дії
    print "Набір наступних дій"
    print "1) Додавання"
    print "2) Віднімання"
    print "3) Множення"
    print "4) Ділення"
    print "5) Закрити Калькулятор"

    # отже, запитаємо яку ж дію хоче здійснити наш користувач
    # і запам'ятаємо його вибір у змінній choice
    # зверніть увагу, ми використовуємо функцію "input", а не "raw_input"
    # функція "input" перетворить введені дані від користувача в число
    choice = input("Оберіть вашу дію: ")
    if choice == 1: # додавання
        # просимо користувача ввести два числа по черзі
        num1 = input("Додати це число: ")
        num2 = input("до цього: ")

        # роздрукуємо результат додавання отриманих двох чисел
        # зверніть увагу, що як гарно ми форматуємо вивід, щоб користувач у зручному 
        # вигляді побачив, що ж саме сталося, напр. "3 + 4 = 7"
        print num1, " + ", num2, " = ", num1 + num2
    elif choice == 2: # віднімання
        # набір дій приблизно такий як і у попередній гілці "if" за винятком
        # однієї речі - тепер ми передані на два числа віднімаємо один від одного
        num1 = input("Віднімаємо число: ")
        num2 = input("від: ")
        print num2, " - ", num1, " = ", num2 - num1
    elif choice == 3: # множення
        num1 = input("Множимо число: ")
        num2 = input("на: ")
        print num1, " * ", num2, " = ", num1 * num2
    elif choice == 4: # ділення
        num1 = input("Ділимо число: ")
        num2 = input("на: ")
        print num1, " / ", num2, " = ", num1 / num2
    elif choice == 5: # користува побажав вийти з калькулятора
        # щоб закінчити цикл програми достатньо встановити значення змінної 
        # loop у будь-яке значення відмінне від 1 
        loop = 0
# і на кінець прощаємся з нашим користувачем
print"Дякуємо за користування нашим калькулятором! Приходьте ще!"
