# variabila = 1
# print("mesajul nr {}".format(variabila))
# raspuns_utilizator = input("care e numele tau")
# print(raspuns_utilizator)
#
# def functia_mea(param_1):
#     pass

# def suma(a, b):
#     return a+ b
#
# # dupa return nu se mai scrie nimic deoarece nu se mai executa
#
# suma_mea = suma(1, 2)
# print(suma_mea)


# def sumaa(a=1, b=1):
#     return a+ b
# suma_mea = suma(3, 4)
# print(suma_mea)
#
# def suma(a, b=1):
#     """
#     :param a: asta e primu
#     :param b: asta e al doilea
#     :return: suma este asta
#     """
#     if type(a) == str:
#         return a
#     return a+ b
# suma_mea = suma(3)
# print(suma_mea)

# return te scoate din functie de fapt

# def my_funct(*param_1):
#     print(type(param_1))
#     return param_1
# print(my_funct("string"))

# a, b = 10, 20
# # min = None
# # if a < b :
# #     min = a
# # else:
# #     min = b
# # print(min)
#
# # min = a if a < b else b
# # inseamna acelasi lucru ca mai sus  dar scris altfel
# # lista_produse = ["ciocolaya", "paine" "mar"]
# # lista_noua = []
# # for x in lista_produse:
# #     if "a" in x:
# #         lista_noua.append(x)
# #
# # print(lista_noua)
#
# #validare cnp exercitiu
# variabila = 1
# print("mesajul nr {} ".format(variabila))
# raspuns_utilizator = input("care e numele tau")


# print(raspuns_utilizator)

# def functia_mea():
#     pass


# def suma(a,b):
#     return a + b
# ce scriem dupa return nu se mai executa in cadrul unei functii
# def suma(a, b=1) -> (list, int):
#     """
#     :param a: primul nr
#     :param b: al doilea
#     :return: suma, diferenta
#     """
#     if type(a) == str:
#         return a, b
#     return a + b, a - b
#
# suma_mea, diferenta = suma(3, 4)
# print(suma_mea, diferenta)

# def my_function(*param_1):
#     print(param_1)
#     return param_1
#
# print(my_function(("string", "string2")))

# def suma_nr_infinite(param1, param2, *var):
#     suma = 0
#     suma = param1 + param2
#     for item in var:
#         suma += item
#     return suma
#
# print(suma_nr_infinite(1, 2, 3, 4))

# def catalog(*args, **kwargs):
#     return args, kwargs
#
# print(catalog(1, 2, nume="ion"))

# def suma(a, b):
#     return a + b
# def diferenta(a,b):
#     return a- b
#
# print(suma(diferenta(1, 2), 2))

# a, b = 10, 20
# min = None
# if a < b:
#     min = a
# else:
#     min = b
# print(min)

#se mai poate scrie asa

# min =a if a < b else b
# print(min)

# lista_produse = ["ciocolata", "mere", "apa"]
# lista_noua = []
# for x in lista_produse:
#     if "a" in x:
#         lista_noua.append(x)
#
# print(lista_noua)

#scris asltfel list comprehension

# lista_noua = [x for x in lista_produse if "a" in x]

