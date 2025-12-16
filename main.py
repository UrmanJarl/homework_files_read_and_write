from pprint import pprint
cook_book = {}

with open('recipes.txt', "r", encoding='UTF-8') as f:
    strings = f.read().split('\n\n')
    for item in strings:
        dish = item.split('\n')[0]
        ingredients = item.split('\n')[2:]
        cook_book[dish] = ingredients
    for dish_title in cook_book.keys():
        for i in range(len(cook_book[dish_title])):
            cook_book[dish_title][i] = cook_book[dish_title][i].split(' | ')
            cook_book[dish_title][i][1] = int(cook_book[dish_title][i][1])
            ingredient_dict = dict.fromkeys(['ingredient_name', 'quantity', 'measure'], '')
            ingredient_dict['ingredient_name'] = cook_book[dish_title][i][0]
            ingredient_dict['quantity'] = cook_book[dish_title][i][1]
            ingredient_dict['measure'] = cook_book[dish_title][i][2]
            cook_book[dish_title][i] = ingredient_dict
    # pprint(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book.keys():
            for ingredient in cook_book[dish]:
                shop_list[ingredient['ingredient_name']] = dict.fromkeys(['measure', 'quantity'], [])
                shop_list[ingredient['ingredient_name']]['measure'] = ingredient['measure']
                shop_list[ingredient['ingredient_name']]['quantity'].append(ingredient['quantity'] * person_count)
                shop_list[ingredient['ingredient_name']]['quantity'] = sum(shop_list[ingredient['ingredient_name']]['quantity'])
                # Не понимаю, почему не работает добавление в список через append.
                # Перепробовал множество вариантов, кроме этого, чтобы добавить второе количество помидоров, но не получилось.
                # Помогите, пожалуйста, разобраться, что я не учёл и где делаю неправильно.
        else:
            print(f'Блюдо {dish} отсутствует в списке')
    pprint(shop_list)

get_shop_list_by_dishes(['Фахитос', 'Рыба', 'Омлет'], 2)
