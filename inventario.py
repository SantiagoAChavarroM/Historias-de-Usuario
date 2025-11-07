
#------------Task 2 entrada de datos----------------#

# Se crea el ciclo while para cada variable con input y su clase de variable, utilizamo True and Except para ejecutar si en caso de un error
while True:
    try:
        nombre = str(input("ingresa tu nombre: "))
        break
    except ValueError:
        print("por favor ingresa un nombre válido")

while True:
    try:
        precio = float(input("escribe el precio: "))
        break
    except ValueError:
        print("por favor ingresa un valor nuevamente")

while True:
    try:
        cantidad = int(input("indica la cantidad: "))
        break
    except ValueError:
        print("por favor ingresa las unidades nuevamente")

print(type(nombre))
print(type(precio))
print(type(cantidad))
    
print(f"hola {nombre}, el precio acordado es {precio} para {cantidad} unidades, generando un total de {precio * cantidad}")