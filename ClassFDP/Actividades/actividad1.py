# Variables y Validación de Acceso
usuariov = "pedrito"
contraseñav = 1234

print("¡Bienvenido a Pyflix!")
usuario = input("Ingresa tu nombre de usuario")
contraseña = input("Ingresa tu contraseña")

if usuario == usuariov and contraseña == contraseñav:
    print("Sesion Iniciada")
elif usuario == usuariov and contraseña != contraseñav: 
    print("Contraseña Incorrecta, pista: 1")
else:
    print("Credenciales Incorrectas")