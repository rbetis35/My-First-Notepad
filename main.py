"""
Proyecto Python MySQL:
 - Abrir asistente
 -Login o registro
 - Si elegimos registro, creara un usuario en la BD
 - Si elegimos login, identificara el usuario
 - Crear notas, mostrar notas, borrar las notas
"""
from usuarios import acciones

print("""
Acciones disponibles:
      - Registro
      - Login
      """)


hazEl = acciones.Acciones()
accion = input("¿Que quieres hacer: ")

if accion == "registro":
    hazEl.registro()

elif accion == "login":
    hazEl.login()

