# загрузим содержимое файла в словарь




def get_shop_list_by_dishes(dishes, person_count, cook_book):

    result_dict = {}

    for list_dishes in dishes:
        try:
            cook_book[list_dishes]
        except:
            print('Блюдо {} не найдено'.format(list_dishes))
            continue
        for k in cook_book[list_dishes]:
            if k['ingridient_name'] in result_dict.keys():
                result_dict[k['ingridient_name']] = {'measure': k['measure'], 'quantity': (int(k['quantity'])*person_count)+int(result_dict[k['ingridient_name']]['quantity'])}
            else:
                result_dict[k['ingridient_name']] = {'measure': k['measure'], 'quantity': int(k['quantity'])*person_count}

    print(result_dict)



cook_book = {}

number = 1
with open('file.dat') as data_file:
    for data_line in data_file:


        if data_line.strip() == "":
            number = 1
            continue

        if number == 1:
            dish = data_line.strip()
            number += 1
        elif number == 2:
            count_ingredients = data_line.strip()
            number += 1
        elif number == 3:
            list_ingredients = data_line.split('|')

            if dish not in cook_book.keys():
                cook_book[dish] = list()

            cook_book[dish].append({'ingridient_name':list_ingredients[0].strip(), 'quantity':list_ingredients[1].strip(), 'measure':list_ingredients[2].strip()})

print(cook_book)  # Задание 1

data_file.close()

get_shop_list_by_dishes(['Фахитос','Омлет'], 3, cook_book)  # Задание 2

# Задание 3
#
# JSON используется для обмена данными между различными языками программирования. Содержит данные в формате ключ:значение заключенными в фигурные скобки
# XML текстовый формат, предназначенный для хранения структурированных данных, обмена данными между программами. Может читаться как компьютером так и человек. Содержит данные в <атрибут>значение</атрибут>
# yaml текстовый формат, с древовидой разметкой. Вложенность веток регулируется количестовом табуляций. Есть возможность хранить различные типы данных: строка, массив, многострочный текст
#логический тип и числа.



