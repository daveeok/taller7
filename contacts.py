import msvcrt
import time
import pprint

contacts = {
    "David" : "320 938639",
    "Alejo": "302 9730456",
    "Samuel": "313 837823",
    "Camilo": "321 7294638",
    "Jeremy": "320 30486204"
}

def contactMenu():
    print(f"""-CONTACTOS-
    1. Consultar contactos. 
    2. Actualizar contacto. 
    3. Nuevo contacto.
    4. Lista de contactos.
    0. Salir """)

    contactOption()

def contactOption():
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
        contactMenu()

def exitContinue():
    print("Pulse cualquier tecla para continuar/Intentar de nuevo o pulse [Escape] para salir del menú.")
    return msvcrt.getch() != chr(27).encode()  

def option1(): 
    while True:
        name = input("Nombre del contacto: ").strip()
        if name in contacts:
            number = contacts.get(name)
            print(f"Numero de {name}: {number}")
        else: 
            print("El contacto no existe.")
        if not exitContinue():
            contactMenu()
            break

def option2():
    name = input("Nombre del contacto: ").strip()
    if name in contacts:
        newNumber = int(input("Nuevo numero: "))
        contacts[name] = newNumber
        print(f"¡Exito, el numero de {name} acualizado correctamente a {newNumber}!")
    else: 
        print("El contacto no existe.")
    if not exitContinue():
        contactMenu()
    else: 
        option2()

def option3():
    name = input("Nombre del nuevo contacto: ").strip()
    number = int(input("Numero del nuevo contacto: "))
    contacts.update({name: number})
    print(f"¡Exito, se agrego a {name} en tu lista de contactos!")
    if not exitContinue():
        contactMenu()
    else: 
        option3()

def option4():
    print("------ TUS CONTACTOS -------")
    pprint.pprint(contacts)
    print("Pulse [Escape] para volver al menú principal.")
    while True:
        if msvcrt.getch() == chr(27).encode():
            contactMenu()
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
            contactMenu()

contactMenu()
