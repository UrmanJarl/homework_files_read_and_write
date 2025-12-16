from pprint import pprint
cook_book = {}

with open('recipes.txt', "r", encoding='UTF-8') as f:
    strings = f.read().split('\n\n')
    for item in strings:
        dish = item.split('\n')[0]
        # quantity = item.split('\n')[1]
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
    pprint(cook_book)
