fra = input("Dime una frase: ")
let = input("Dime una letra: ")
cont = 0
for i in fra:
    if i == let:
        cont += 1
print("La letra '%s' aparece %2i veces en la frase '%s'." % (let, cont, fra))