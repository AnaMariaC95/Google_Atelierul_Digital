# #tema joi 7/04
# #ex 1
# lista = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6 ]
# print("Aceasta este lista data:")
# print(lista)
#
# #ex 2
# #afișarea unei alte liste ordonată ascendent (lista inițială trebuie păstrată în aceeași formă)
# lista_ordonata = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
# print("Aceasta este lista ordonata:")
# lista_ordonata.sort()
# print(lista_ordonata)
#
# # ex 3
# #afișarea unei alte liste ordonată descendente (lista inițială trebuie păstrată în aceeași formă)
# lista_descendenta= lista_ordonata
# print("Aceasta este lista descendenta:")
# lista_descendenta.reverse()
# print(lista_descendenta)
#
# #ex 4
# #afișarea numerelor pare din listă (folosind DOAR slice, altă metodă va fi considerată invalidă)
# lista_nr_pare = lista_ordonata
# print("Aceasta este lista numerelor pare:")
# print(lista_nr_pare[0:10:2])
# # # ex 5
# # #afișarea numerelor impare din listă (folosind DOAR slice, altă metodă va fi considerată invalidă
# lista_nr_impare = lista_ordonata
# print("Aceasta este lista numerelor impare:")
# print(lista_nr_impare[1:10:2])
#
# # #ex 6
# # # afișarea elementelor multipli ai lui 3
# lista_multipli_3 = lista_ordonata
# print("Aceasta este lista numerelor cu multipli lui 3:")
# print(lista_multipli_3[1:8:3])


#FUNCTII IFLOOPS

# Să se scrie o funcție care citește de la tastatură și returnează valoarea dacă aceasta este
# un număr întreg, altfel returnează
# valoarea 0.

# print("Introduceti numarul:")
# numar: str = input()
# if nr == type(int()):
#     print(f"Numarul introdus este {numar}")
# else:
#     print("0")

#Să se scrie o funcție recursivă care primește ca parametru un număr întreg și returnează:
# a) suma tuturor numerelor de la [0, n]

# def get_sum(nr):
#     if nr == 0:
#         return 0
#     return nr + get_sum(nr - 1)
#
# suma = get_sum(4)
# print(suma)

#b) suma numerelor pare de la [0, n]

# def sum_nr_pare(n):
#     if n  == 0:
#         return 0
#     if n % 2 == 0:
#         return n +sum_nr_pare(n - 2)
#     else:
#         print("Avem un nr impar introdus")
#
# suma_para = sum_nr_pare(5)
# print(suma_para)

#c) suma numerelor impare de la [0. n]

# def sum_nr_impare(num):
#     if num <= 0:
#         return 0
#     if num % 2 != 0:
#         return num +sum_nr_impare(num - 2)
#     else:
#         print("a fost introdus un nr par")
#         return  sum_nr_impare(num - 1)
#
# suma_impara = sum_nr_impare(6)
# print("Suma va fi:")
# print(suma_impara)


#Să se scrie o funcție care primește un număr nedefinit de parametrii și să se calculeze suma parametrilor care reprezintă
#numere întregi sau reale.

# a)your_function(1, 5, -3, ‘abc’, [12, 56, ‘cad’]) va returna 3 (1 + 5 - 3)

# def functie(param):
#      for nr in param:
#          for nr  type(int) or type(float):
#              print(nr)
#          continuee
#          if nr != type(int) or type(float):
#              return 0
#
#
# enumerare =1, 5, -3, "abc", [12, 56, "cad"]
# suma_func1 = functie(enumerare)
# print(suma_func1)

#b) your_function() va returna 0

# def functie1():
#     return 0
#
# suma_func2 = functie1()
# print(suma_func2)

#c) your_function(2, 4, ‘abc’, param_1=2) va returna 6 (2 + 4).

# def functie3(p1, p2, p3, **kwargs):
#     if p1 == type(int) or type(float):
#         if p2 == type(int) or type(float):
#                 if p3 != type(str):
#                   sum = p1 + p2
#                 elif p3 == type(int) or type(float):
#                     sum = p1 + p2 +p3
#                 print(sum)
#
#
# suma = functie3(2, 4, "abd", param_1=2 )
# print(suma)










#
