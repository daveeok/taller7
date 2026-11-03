import msvcrt
import time

catalog = {

    "P01": {
        "nombre": "Cuaderno argollado",
        "precio": 6500,
        "stock": 20,
    },

    "P02": {
        "nombre": "Caja de micropuntas",
        "precio": 18000,
        "stock": 12,
    },

    "P03": {
        "nombre": "Resma de papel",
        "precio": 15000,
        "stock": 8,
    }
}

def showMenu():
    print(f"""
    --------- MENÚ DE CATALOGO ---------
    1. Búsqueda segura.
    2. Ingreso de existencias.
    3. Registro de producto nuevo.
    4. Cálculo de valor de inventario:
    0. Salir
    ------------------------------------
    """)
    selectOption()

def selectOption():
    option = int(input("Seleccione una opción: "))
    if option == 1:
        option1()
    elif option == 2:
        option2()
    elif option == 3:
        option3()
    elif option == 4:
        option4()
    elif option == 0:
        option0()
    else: 
        print("Opción invalida")
        showMenu()

def exitContinue():
    print("Pulse cualquier tecla para continuar/Intentar de nuevo o pulse [Escape] para salir del menú.")
    return msvcrt.getch() != chr(27).encode()  

def option1():
    while True:
        numberKey = input("Ingrese el identificador del producto (Ej. P01): ")
        if numberKey in catalog:
            print(catalog[numberKey])
        else: 
            print("Identificador desconocido")
            if "p" in numberKey:
                            print("la p debe ser mayuscula.")
        if not exitContinue():
            showMenu()
            break

def option2():
    while True:
        numberKey = input("Ingrese el identificador del producto (Ej. P01): ")

        if numberKey in catalog:
            changeStock = int(input("Ingrese la cantidad de nuevas unidades a agregar al stock actual: "))
            actualStock = catalog[numberKey]["stock"]
            changedStock = catalog[numberKey]["stock"] + changeStock
            confirm = input(f"Estas a punto de cambiar el stock de {catalog[numberKey]["nombre"]} de {actualStock} a {changedStock}. ¿Deseas continuar? s/n").lower()

            if not "s" in confirm:
                None
                print("Cancelaste la operación")
            else: 
                catalog[numberKey]["stock"] = changedStock
                print("¡Exito! Actualizaste la cantidad de stock, puedes confirmarlo en la opción 1 del menú")

        else: print("Este producto no existe.")

        if not exitContinue():
            showMenu()
            break

def option3():
    while True:
        newProductName = input("Nombre de tu producto: ")
        newProductPrice = int(input("Precio del producto:"))
        newProductStock = int(input("Cantidad de stock inicial: "))

        numero = len(catalog) + 1

        if numero < 10:
            key = "P0" + str(numero)
        else:
            key = "P" + str(numero)

        confirm = input("¿Deseas agregar el prodcuto? s/n ").lower()

        if not "s" in confirm:
            print("Operación cancelada")
        else: 
            catalog.update({key: {"nombre": newProductName, "precio": newProductPrice,"stock": newProductStock }})
            print("¡Exito! Se actualizó en inventario correctamente.")

        if not exitContinue():
            showMenu()
            break
        
def option4():
    total = 0 
    for identifier in catalog:
        total =  total + catalog[identifier]["precio"] * catalog[identifier]["stock"]

    print(f"el valor monetario total es: {total}$")

    print("Pulse [Escape] para volver al menú principal.")
    while True:
        if msvcrt.getch() == chr(27).encode():
            showMenu()
            break

def option0():
    while True:
        exit = input("¿Seguro que desea salir? s/n ").lower()
        if "s" in exit:
            print("Saliendo...")
            time.sleep(1)
            print("¡Adiós!")
            raise SystemExit
        else:
            showMenu()
showMenu()