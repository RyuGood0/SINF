solutions = 0
a = int(input("Entrez la valeur du coefficient a : "))
b = int(input("Entrez la valeur du coefficient b : "))
c = int(input("Entrez la valeur du coefficient c : "))
max = int(input("Entrez la valeur maximale pour x et y : "))

for x in range(1,max):
    for y in range(1,max):
        if a*x + b*y == c:
            print("x =", x, " y =", y)
            solutions += 1

if solutions == 0:
    print("Aucune solution trouvee")
else:
    print(solutions, "solutions trouvees")