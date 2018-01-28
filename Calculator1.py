# -*- coding: utf-8 -*-
# програма Калькулятор

# ця функція виводитиме меню нашого калькулятора, а також 
# запитує і передає вибір користувача про дію у головну програму
def menu():
    print " "
    print "Вітаємо!"
    # роздрукуємо нашому користувачеві всеможливі дії
    print "Набір наступних дій"
    print "1) Додавання"
    print "2) Віднімання"
    print "3) Множення"
    print "4) Ділення"
    print "5) Закрити Калькулятор"
    print " "
    # тут ми просимо користувача ввести/обрати дію, і віддаємо його вибір назад
    # у головну програму
    return input("Оберіть вашу дію: ")
 
# нижче визначаємо функції дій з числами, у них ми не повертаємо ніяких значень, а лише
# виводимо на екран результат їхніх дій

# додаємо два числа
def add(num1, num2): #функція приймає два параметри, два числа
    # і виводить результат їхнього додавання у зручному для користувача форматі
    # пам'ятаємо print може мати більше ніж один аргумент через кому
    print num1, " + ", num2, " = ", num1 + num2

# віднімання
def sub(num1, num2):
    print num2, " - ", num1, " = ", num2 - num1

# множення
def mul(num1, num2):
    print num1, " * ", num2, " = ", num1 * num2

# Ділення
def div(num1, num2):
    print num1, " / ", num2, " = ", num1 / num2

# після того як ми визначили всі необхідні функції, починаємо основну програму

# ця змінна скаже коли циклу треба зупинитися
loop = 1

# цю змінну використаємо для запам'ятовування варіанту дії обраної користувачем
choice = 0

# використовуємо цикл "while" який працюватиме доти доки змінна loop є 1
while loop == 1:    
    
    # отже запитаємо яку ж дію хоче здійснити наш користувач
    # і замап'ятаємо його вибір у змінній choice
    choice = menu()
    if choice == 1: # додавання
        # тут ми у скорочено вигляді отримуємо значення чисел, а також обрахуємо їх
        # та роздрукуїмо на екран - усе в одну стрічку, завдяки використанню наших
        # визначених напередодні функцій.

        # отже викликаємо функцію add передаючи їй два числавведені користувачем
        add(input("Додати це число: "), input("до цього: "))
                
    elif choice == 2: # віднімання
        # теж саме з відніманням
        sub(input("Віднімаємо число: "), input("від: "))
        
    elif choice == 3: # множення
        mul(input("Множимо число: "), input("на: "))
       
    elif choice == 4: # ділення
        div(input("Ділимо число: "), input("на: "))
        
    elif choice == 5: # користува побажав вийти з калькулятора
        # щоб закінчити цикл програми достатньо встановити значення змінної 
        # loop у будь-яке значення відмінне від 1 
        loop = 0

# і на кінець прощаємся з нашим користувачем
print"Дякуємо за користування нашим калькулятором! Приходьте ще!"
