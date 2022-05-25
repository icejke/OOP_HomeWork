from pprint import pprint

FILE_NAME = 'recipes.txt'


def parsing_cook_book(file_name):
    with open(file_name, 'r', encoding='utf8') as file:
        total_res = {}
        dish = file.readline().strip()
        for line in file:
            quantity = int(line)
            ingredients = []
            for i in range(quantity):
                file_data = file.readline().strip().split(' | ')
                ingredients.append(
                    {'ingredient_name': file_data[0], 'quantity': int(file_data[1]), 'measure': file_data[2]})
            total_res[dish] = ingredients
            file.readline()
            dish = file.readline().strip()
        return total_res


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in my_cook_book:
            for dish_ingr in my_cook_book[dish]:
                name = dish_ingr['ingredient_name']
                measure = dish_ingr['measure']
                quantity = int(dish_ingr['quantity'])
                if dish_ingr['ingredient_name'] not in shop_list:
                    shop_list[name] = {'measure': measure, 'quantity': quantity * person_count}
                else:
                    shop_list[name]['quantity'] += (dish_ingr['quantity'] * person_count)

        else:
            print(f'Блюда "{dish}" нет в списке. Добавлять в список покупок не будем.\n')
    return shop_list


my_cook_book = parsing_cook_book(FILE_NAME)
pprint(get_shop_list_by_dishes(['Омлет', 'Омлет'], 1))
