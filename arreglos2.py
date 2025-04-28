playlistdelcurso = [
    "Beat-it.mp3",
    "Loba.mp3",
    "15b.mp3",
    "Diva virtual.mp3",
    "Pokemon jontho.mp3"]

print(playlistdelcurso)
print()
print(playlistdelcurso[1])

print("TAMAÑO DEL ARREGLO")
listsize = len(playlistdelcurso)
print(listsize)

print(playlistdelcurso[-1])

#Imprimir todas las letras de una palabra
nuevapalabra = "GIRAFARIG".lower()
for i in range(len(nuevapalabra)):
    print(nuevapalabra[i])

if nuevapalabra == nuevapalabra[::-1]:
    print("Tu palabra es palíndromo")
else:
    print("Tu palabra no es palíndromo")

#esPalíndromo
