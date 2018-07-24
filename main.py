def get_shop_list_by_dishes(dishes, person_count, cook_book):

    result_dict = {}

    for list_dishes in dishes:

        if list_dishes not in cook_book:
            print('Блюдо {} не найдено'.format(list_dishes))
            continue

        for k in cook_book[list_dishes]:
            if k['ingredient_name'] in result_dict.keys():
                new_quantity = (int(k['quantity']) * person_count) + int(result_dict[k['ingredient_name']]['quantity'])
                result_dict[k['ingredient_name']] = {'quantity': new_quantity}
            else:
                new_quantity = int(k['quantity']) * person_count
                result_dict[k['ingredient_name']] = {'measure': k['measure'], 'quantity': new_quantity}

    print(result_dict)


def get_cook_book(file_name):


    READ_EMPTY_LINE = 1
    READ_DISH = 2
    READ_INGREDIENT = 3

    cook_book = {}
    current_state = 1

    with open(file_name) as data_file:
        for data_line in data_file:
            data_line_without_space = data_line.strip()
            if not data_line_without_space:
                current_state = READ_EMPTY_LINE
                continue
            if current_state == 1:
                dish = data_line_without_space
                current_state = READ_DISH
            elif current_state == 2:
                current_state = READ_INGREDIENT
            elif current_state == 3:
                list_ingredients = data_line.split('|')
                if dish not in cook_book:
                    cook_book[dish] = list()
                cook_book[dish].append(
                                        {
                                            'ingredient_name': list_ingredients[0].strip(),
                                            'quantity': list_ingredients[1].strip(),
                                            'measure': list_ingredients[2].strip()
                                        })
    return cook_book


cook_book = get_cook_book('file.dat')
print(cook_book)  # Задание 1

get_shop_list_by_dishes(['Фахитос','Омлет'], 3, cook_book)  # Задание 2

