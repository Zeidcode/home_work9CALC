

def Intface(i:str):
    match i:
        case "Welcome":
            print('---------------------------------------------')
            print('Здравствуйте')
        case "Menu":
            print('---------------------------------------------')
            print('Варианты работы программы')
            print('1. Калькулятор для работы с рациональными числами')
            print('2. Калькулятор для работы с комплексными числами')
            print('3. Вывод лога работы программы')
            print('4. Выход из программы')
        case "End":
            print('----------------------------------------------')
            print('Выберите дальнейшее действие')
            print('1. Выход в главное меню')
            print('2. Выход из программы')
