import random  #Импорт библиотеки для генерации случайных чисел
import string  #Импорт библиотеки для работы со строками
length = int(input("Укажите длину пароля: "))  #Спрашиваем с клавиатуры длину пароля
def generate_password(length):      #Создаём функцию генерации случайного пароля
    lower = string.ascii_lowercase  # возвращает список всех букв в нижнем регистре от «a» до «z»
    upper = string.ascii_uppercase  # возвращает список всех букв в верхнем регистре от «A» до «Z»
    digits = string.digits          # возвращает список цифр
    symbols = string.punctuation    # возвращает список символов
    # Добавляем случайным образом по одному символу каждого типа в наш пароль, так чтобы не повторялась буква
    password = [random.choice(upper),random.choice(digits), random.choice(lower), random.choice(symbols)] 
    all_chars = lower + upper + digits + symbols  # Заполняем оставшуюся длину пароля случайными символами  
    while len(password) < length:  
        next_char = random.choice(all_chars)  
        if not password or next_char != password[-1]:   # Проверяем, чтобы не было последовательных одинаковых символов  
            password.append(next_char)    
    random.shuffle(password)   # Перемешиваем список, чтобы первые 4 символа не были предсказуемы  
    return ''.join(password)   # Получаем наш пароль
print(generate_password(length))  
