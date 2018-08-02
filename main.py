def get_shop_list_by_dishes(dishes, person_count, cook_book):
    result_dict = {}

    for list_dishes in dishes:

        if list_dishes not in cook_book:
            print('Блюдо {} не найдено'.format(list_dishes))
            continue

        for k in cook_book[list_dishes]:
            ingredient_name = k['ingredient_name']
            current_quantity = k['quantity'] * person_count
            if ingredient_name in result_dict:
                result_dict[ingredient_name]['quantity'] += current_quantity
            else:
                result_dict[ingredient_name] = {'measure': k['measure'], 'quantity': current_quantity}

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
            if current_state == READ_EMPTY_LINE:
                dish = data_line_without_space
                current_state = READ_DISH
            elif current_state == READ_DISH:
                current_state = READ_INGREDIENT
            elif current_state == READ_INGREDIENT:
                list_ingredients = data_line.split('|')
                if dish not in cook_book:
                    cook_book[dish] = list()
                cook_book[dish].append(
                    {
                        'ingredient_name': list_ingredients[0].strip(),
                        'quantity': int(list_ingredients[1].strip()),
                        'measure': list_ingredients[2].strip()
                    })
    print(cook_book)  # Задание 1
    return cook_book


get_shop_list_by_dishes(['Фахитос', 'Омлет'], 3, get_cook_book('file.dat'))  # Задание 2
