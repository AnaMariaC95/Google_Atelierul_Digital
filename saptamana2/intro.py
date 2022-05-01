# print("mesaj")
# # aici se pun comentarile
# a = 2
# variabila_b = 5
# #variabila trebuie sa fie cu litera mica si daca vrem sa aiba doua nume punem _
# # numele nu poate incepe cu cifra
# # cu litera mare se csrie la op
# # == e pt comparare iar = e pt asignare
# print(variabila_b)
# # putem declara o valoare ca None pt variabile temporare din interiorul unei instructiuni
#
# mesaj = "ana are mere"
# print(type(mesaj))
# mesaje = "'\tana\n 's are mere"
# print(mesaje)
#
# numar_mere = 5
# mesaj = f"Ana are {numar_mere} mere"
# print(mesaj)
#
# test = "ana are {0} mere si {1} si {0} portocale".format(numar_mere, a)
# print(test)
#
# # ex liste
# lista = [2, 3, 4, 'ana']
# #lista.append('2')
# print(len(lista))
# print(lista[2])
# print(lista[-1])
# #slice
# print(lista[1:])
#
# #tuple
# # cand la tuplu declarat pui un sg element type va fi tipul de element returnat
# # ca sa fie tuplu trebuie sa punem ,
# tuplu = (1, 7, 3, 'n')
# print(type(tuplu))
#
# #dictionare
# dict = {"cheie":2, "cheie2":5}
# print(dict)
# print(dict["cheie"])
# print(dict.get("cheie3", 3))
# dict.update({"cheie4": "6"})
# print(dict)
# print(len(dict.items()))
#
# # fac ordinea din paranteza la afisare
# #le ordoneaza numeric
# # putem uni doua seturi cu union
#
# #instructiuni
# var = 6
# if var < 5 :
#     print(" my var este mai mic ")
# elif var > 5:
#     print(" var e mai mare")
# else:
#     print("orice altceva")
#
# # e bine sa nu folosim else
# #cum putem schimba blocul de conditionare
#
# #structuri repetitive
# while True:
#     print("set instructiuni")
#     break
# # aici face un loop daca nu ii punem ceva sa iasa
# # break opreste
# # incrementare : var+=1 inseamna var= var+1
#
# # cuvant = 'ana are mere'
# # for i in cuvant:
# #     print(i)

# print("mesaj")
# a = 1
# variabila_a = 6
# mesaj = " ana's are mere "
# print(type(mesaj))
# print(mesaj)
# mesaj_2 = "\ttestul e mare \nsi destul de greu"
# print(mesaj_2)
# nr_mere = 2
# nr_pere = 3
# # mesaj = f"ana are {nr_mere} mere "
# # mesaj = "ana are {0} mere si {1} pere ".format(nr_mere, nr_pere)
# mesaj = "ana are " + str(nr_mere) + " mere"
# print(mesaj)

# lista = [2, 3, 4, 'ana']
# # lista.append('2')
# print(lista[1:])
# # print(len(lista))
# lista[0] = 'mere'
# print(lista)

# # tuplu = (1, 7, -3, 's')
# tuplu = (2, 3)
# print(type(tuplu))
# string_nou = "ana are mere"
# lista_noua = list(tuplu)
# print(lista_noua)

# dictionar = {"cheie1": 1, "cheie2": 2}
# print(dictionar["cheie1"])
# print(dictionar.get("cheie2"))
# print(dictionar.get("cheie3", "ana"))
# dictionar["cheie3"] = "3"
# print(dictionar)
# dictionar.update({"cheie4": 4})
# print(dictionar)
# print(dictionar.keys())
# print(dictionar.values())

# my_set = {"item1", 2, 3}
# my_set1 = {"item2", 3, 6}
# print(my_set)
# print(my_set.union(my_set1))

# my_var = 5
# mesaj = "5=5"
# if my_var < 5:
#     mesaj= "e ok"
# elif my_var > 5:
#     mesaj = "nu e ok"
# # else:
# #     print("5=5")
# print(mesaj)
# var = 1
# while var < 3:
#     print("asa e")
#     var += 1

# cuvant = "ana are mere"
# for i, value in enumerate(cuvant):
#     print(i, value)

# for i in range(5):
#     print(i)

