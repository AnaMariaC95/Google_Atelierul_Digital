# memory savers , files, web scraping
# memory savers
# memoria e gestionata de python memory management
#FUNCTIA LAMBDA - indeplineste  singura instructiune si poate primi orice nr de parametri
# spre deosebire de def, ocupa memorie doar in momentul rularii si e stearsa dupa
# my_lambda = lambda x, y : x +y
#
# my_sum = my_lambda(1, 2)
# print(my_sum)

# a = lambda :1
#
# print(f'id(a) = {id(a)}')
# print(f'lamdba unnasigned : {id(lambda : 5)}')
# print(f'lamdba unnasigned : {id(lambda : 10)}')

# players = [{ "first_name": "Ion", "last_name": "Doe", "rank": 3},
#            {"first_name": "Kevin", "last_name": "McDonald", "rank": 1},
#            {"first_name": "Bradd", "last_name": "Kelvin", "rank": 2}]
#
# sorted_players = sorted(players, key=lambda player: player ["rank"])
# print(sorted_players)

# x = lambda a : a +5
# print(x(4))

# def my_function(n):
#     return lambda a: a * n
#
#suma = my_function(5)
# print(suma(3))
# def functie(x):
#     return lambda x: x
#
# numar = functie(4)
# print(numar(6))
# nr = lambda x : x
# print(nr(3))

# functia MAP : modifica fiecare element din lista
# import copy
#
# players = [{ "first_name": "Ion", "last_name": "Doe", "rank": 3},
#            {"first_name": "Kevin", "last_name": "McDonald", "rank": 1},
#            {"first_name": "Bradd", "last_name": "Kelvin", "rank": 2}]
#
#
#
# def check_top_3_player(player):
#     updated_player = copy.deepcopy(player)
#     updated_player["is_top_3"] = True if updated_player["rank"] <= 3 else False
#     return updated_player
#
# players_with_top_three_values = map(check_top_3_player, players)
# print('players_with_top_three_values =', list(players_with_top_three_values))

#FUNCTIA FILTER

# players = [{ "first_name": "Ion", "last_name": "Doe", "rank": 3},
#            {"first_name": "Kevin", "last_name": "McDonald", "rank": 1},
#            {"first_name": "Bradd", "last_name": "Kelvin", "rank": 2}]

# def filter_all_mcdonalds(player):
#     if player["last_name"] == "McDonald":
#         return True
#     return False
#
# all_mcdonalds = filter(filter_all_mcdonalds, players)
# print("all_mc", list(all_mcdonalds))

# FUNCTIA ZIP returneaza un zip format din tupluri
# list_1 = [1, 10, 100]
# list_2 = [2, 20, 200]
# list_3 = [3, 30, 300]
# for zip_item in zip(list_1, list_2, list_3):
#     # print(zip_item)
#     list_1_element, list_2_element, list_3_element = zip_item
#     print(list_1_element, list_2_element, list_3_element)

#list comprehension - obtii o lista noua de la o lista existenta

# my_numbers = [1, 2, 3, 4, 5]
# squared_numbers = [item * 2 for item in my_numbers]
# print('my_numbers', my_numbers)
# print('squared_numbers sunt ', squared_numbers)

#LUCRUL CU FISIERELE

# file = open('data.txt', 'w')
# file.write("hello word")
# file.close()
#
# file = open('data.txt', 'a')
# try:
#     file.write("Buna ziua")
# finally:
#     file.close()
#
# with open('data.txt', 'a') as file:
#    file.write("buna seara")
#
# with open('data.txt', 'r') as file:
#     for line in file.readlines():
#         print("line are:", line)
#
# with open("data.txt", 'r') as file:
#     while True:
#         line = file.readline()
#         if not line:
#             break
#         print('line is:', line)

#fisiere csv (comma separated values)



# new_cars = [
#     ['dacia', 'logan', 2005, 75],
#     ['renault', 'clio', 2005, 75]
#     ]
# with open('data.csv', 'a') as csv_file:
#     csv_writer = csv.writer(csv_file, delimiter = ',')
#
#     for new_car in new_cars:
#         csv_writer.writerow(new_car)
#         csv_writer.writerow(['ana'])
# import csv
# with open('data.csv', 'a') as csv_file:
#     data_writer = csv.writer(csv_file, delimiter = ',')
#     data_writer.writerow(['ana', 'are', 'mere'])

#lucrul cu fisierele
# os si os.path ajuta la lucrul cu fisierele ce tin de sist de operare

# import os
# print(os.getcwd())


#pip si virtual enviroment venv



