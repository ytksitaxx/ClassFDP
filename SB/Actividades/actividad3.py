# Operadores y Verificador de Playlist
duracion = float(input("Ingresa la duracion de la cancion en minutos"))
genero = str(input("Ingresa el genero musical de la cancion "))
año = int(input("Ingresa el año de lanzamiento de la cancion "))

duracionv = int(2.5 <= duracion <= 4.5)
generov = genero in["rock", "pop", "indie"]
añov = año > 2010

if duracionv and generov and añov:
    print("La cancion cumple con los requisitos, ¡puedes agregarla a la playlist!")
else:
    print("La cancion NO cumple con los requisitos para entrar a la playlist")

if duracionv == False:
    print("La duracion de la cancion no cumple con los requisitos")
elif generov == False:
    print("El genero de la cancion no cumple con los requisitos")
elif añov == False:
    print("El año de la cancion no cumple con los requisitos")
