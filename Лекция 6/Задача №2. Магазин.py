def main():  
    # Начальный список покупок  
    shopping_list = {  
        "молоко": 5,  
        "хлеб": 10,  
        "варенье": 7,  
        "мёд": 3   }  
    while True:  
        print("\n Вы можете:")  
        print("1. Добавить товар")  
        print("2. Убрать товар")  
        print("3. Показать список")  
        print("4. Закончить")  
        print("-------------------------------")  
        choice = input("Выберите действие: ")  
          
        if choice == "1":  
            add_item(shopping_list)  
        elif choice == "2":  
            remove_item(shopping_list)  
        elif choice == "3":  
            show_list(shopping_list)  
        elif choice == "4":  
            print("Спасибо. До скорой встречи в нашем магазине")
            print("............................................")
            break  
        else:  
            print("Неверный выбор. Попробуйте ещё раз.")  
  
def add_item(shopping_list):  
    item = input("Введите название товара: ").lower()  
    try:  
        quantity = int(input("Введите количество: "))  
        if quantity > 0:  
            if item in shopping_list:  
                shopping_list[item] += quantity  
            else:  
                shopping_list[item] = quantity  
            print(f"Добавлено {quantity}  шт.")  
        else:  
            print("Количество должно быть положительным числом.")  
    except ValueError:  
        print("Ошибка: введите число.")  
  
def remove_item(shopping_list):  
    item = input("Введите название товара для удаления: ").lower()  
    if item in shopping_list:  
        del shopping_list[item]  
        print(f"{item} удален из списка")  
    else:  
        print("Товар не найден в списке")  
  
def show_list(shopping_list):  
    if not shopping_list:  
        print("Список покупок пуст")  
    else:  
        print("\nСписок покупок:")  
        for item, quantity in shopping_list.items():  
            print(f"{item}: {quantity}")  
  
if __name__ == "__main__":  
    main()  
