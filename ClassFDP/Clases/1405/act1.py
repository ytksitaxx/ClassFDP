import random

vidaHeroe = 100
vidaMonstruo = 100

while vidaHeroe > 0 and vidaMonstruo > 0:
    dañoHeroe = random.randint(10,20)
    vidaMonstruo -= dañoHeroe
    print("El heroe ataca y hace:", dañoHeroe, "de daño")

# El heroe ataca
    dañoMonstruo = random.randint(10, 20)
    vidaHeroe -= dañoMonstruo
    print("El monstruo ataca y hace:", dañoMonstruo, "de daño")

# El monstruo ataca
    print("Vida del heroe:", vidaHeroe)
    print("Vida del monstruo:", vidaMonstruo)

    if vidaHeroe <= 0 and vidaMonstruo <= 0:
        print("Ambos han caido al mismo tiempo")
    elif vidaHeroe <= 0:
        print("El heroe ha caido, el mounstruo gana")
    elif vidaMonstruo <= 0:
        print("El heroe ha vencido al monstruo")
    else:
        print("Ambos siguen de pie!, la batalla continua en otro momento...")