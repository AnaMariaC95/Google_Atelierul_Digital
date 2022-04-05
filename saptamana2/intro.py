print("mesaj")
# aici se pun comentarile
a = 2
variabila_b = 5
#variabila trebuie sa fie cu litera mica si daca vrem sa aiba doua nume punem _
# numele nu poate incepe cu cifra
# cu litera mare se csrie la op
# == e pt comparare iar = e pt asignare
print(variabila_b)
# putem declara o valoare ca None pt variabile temporare din interiorul unei instructiuni

mesaj = "ana are mere"
print(type(mesaj))
mesaje = "'\tana\n 's are mere"
print(mesaje)

numar_mere = 5
mesaj = f"Ana are {numar_mere} mere"
print(mesaj)

test = "ana are {0} mere si {1} si {0} portocale".format(numar_mere, a)
print(test)

# ex liste
lista = [2, 3, 4, 'ana']
#lista.append('2')
print(len(lista))
print(lista[2])
print(lista[-1])
#slice
print(lista[1:])

#tuple
# cand la tuplu declarat pui un sg element type va fi tipul de element returnat
# ca sa fie tuplu trebuie sa punem ,
tuplu = (1, 7, 3, 'n')
print(type(tuplu))

#dictionare
dict = {"cheie":2, "cheie2":5}
print(dict)
print(dict["cheie"])
print(dict.get("cheie3", 3))
dict.update({"cheie4": "6"})
print(dict)
print(len(dict.items()))

# fac ordinea din paranteza la afisare
#le ordoneaza numeric
# putem uni doua seturi cu union

#instructiuni
var = 6
if var < 5 :
    print(" my var este mai mic ")
elif var > 5:
    print(" var e mai mare")
else:
    print("orice altceva")

# e bine sa nu folosim else
#cum putem schimba blocul de conditionare

#structuri repetitive
while True:
    print("set instructiuni")
    break
# aici face un loop daca nu ii punem ceva sa iasa
# break opreste
# incrementare : var+=1 inseamna var= var+1

# cuvant = 'ana are mere'
# for i in cuvant:
#     print(i)



