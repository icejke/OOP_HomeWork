from pprint import pprint
import re

FILE_NAME = 'recipes.txt'


def parsing_cook_book(file_name):
    with open(file_name, 'r', encoding='utf8') as file:
        total_res = {}
        dish = file.readline().strip()
        for line in file:
            # line = line.strip()
            quantity = int(line)
            ingredients = []
            for i in range(quantity):
                file_data = file.readline().strip().split(' | ')
                ingredients.append(
                    {'ingredient_name': file_data[0], 'quantity': int(file_data[1]), 'measure': file_data[2]})
            total_res[dish] = ingredients
            file.readline()
            dish = file.readline().strip()
        return pprint(total_res)


parsing_cook_book(FILE_NAME)
