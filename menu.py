# функція меню
# функція виводитиме користувачу меню доступних опцій і
# проситиме його зробити свій вибір. Після того як користувач
# зробив вибіа - функція повертатиме назовні вибір користувача.

# визначаємо функцію під назвою 'menu', функція приймає два аргументи
# list - це буде список опцій
# question - це стрічка, питання до користувача, щоб він зробив вибір
def menu(list, question):
    # пробігаємось по усіх опціях списку і роздрукуємо їх користувачу
    # на екран для подальшого вибору
    for entry in list:
        # будь-який пітонівський список має метод index,
        # цей метод приймає елемент списку як аргумент і повертає
        # індекс даного елементу списку
        # таким чином у рядку нижче ми виводимо на екран поточний
        # елемент entry у списку list, збільшуємо його на одиничку, щоб
        # для користувача списосок починався з 1, а не з 0 (адже
        # пам'ятаємо в пітоні індекси елементів у списку починаються з 0)
        print 1 + list.index(entry)
        # закриваємо номер опції дужкою, ну і звичайно не забуваємо
        # вивести після дужки саму назву опції
        print ")" + entry
    
    # після того якми ввели усі доступні опції, час і запитати користувача
    # зробити свій вибір - вивівши на екран питанняю
    # Зауважте, ми віднімаємо одиничку від отриманого від користувача
    # вибору, щоб отримати справжню позицію елемента зі списку (пам'ятаємо
    # у рядочках вище ми спеціально цю одиничку додавали при вводі опцій)
    return input(questin) - 1
  
