import pymongo
def traer_bd():
    try:  
        client = pymongo.MongoClient("mongodb+srv://Admin2022:admin123@cluster0.ruz9u.mongodb.net/?retryWrites=true&w=majority")
        db = client.ModuloAcompañamiento
    #nombre: Admin2022
    #contraseña: admin123
    except:
        print("Error de conexion con la base de datos")
    return db

def consultarInfo():
    db = traer_bd()
    clientes = db.clientes.find().limit(10)
    for cliente in clientes:
        print("-----------------------------------------")
        print("Nombre: "+cliente["Nombre"])
        print("Edad: "+str(cliente["Edad"]))
        print("Dirreccion: "+str(cliente["Direccion"]))
        print("Telefono: "+cliente["Telefono"])
        

def filtrarNombre(parametro):
    try:
        db = traer_bd()
        nombre = db.clientes.find({"Nombre":parametro}).limit(1)
        for filtro in nombre:
            print("-----------------------------------------")
            print("Nombre: "+filtro["Nombre"])
            print("Edad: "+str(filtro["Edad"]))
            print("Dirreccion: "+str(filtro["Direccion"]))
            print("Telefono: "+filtro["Telefono"])
    except:
        print("Ocurrio un Error")
    return filtro


def filtrarEdad(parametro):
    try:
        db = traer_bd()
        edad = db.clientes.find({"Edad":parametro}).limit(1)
        for filtro in nombre:
            print("-----------------------------------------")
            print("Nombre: "+filtro["Nombre"])
            print("Edad: "+str(filtro["Edad"]))
            print("Dirreccion: "+str(filtro["Direccion"]))
            print("Telefono: "+filtro["Telefono"])
    except:
        print("Ocurrio un Error")
    return edad


def filtrarTelefono(parametro):
    try:
        db = traer_bd()
        telefono = db.clientes.find({"Telefono":parametro}).limit(1)
        for filtro in nombre:
            print("-----------------------------------------")
            print("Nombre: "+filtro["Nombre"])
            print("Edad: "+str(filtro["Edad"]))
            print("Dirreccion: "+str(filtro["Direccion"]))
            print("Telefono: "+filtro["Telefono"])
    except:
        print("Ocurrio un Error")
    return telefono


def menu():
    print("Sistema del Modulo de Acompañamiento")
    print("""Seleciona una opcion
    1) Consulta general de los usuarios
    2) Filtrar usuario por nombre
    3) Filtrar usuario por edad
    4) Filtrar usuario por telegono
    5) Salir """)
    opcion = str(input("Has seleccionado:"))
    if opcion == '1':
        consultarInfo()
    elif opcion == "2":
        filtro=input("Escribe aca el nombre: ")
        filtrarNombre(filtro)
    elif opcion == "3":
        filtro=input("Escribe aca la edad: ")
        filtrarEdad(filtro)
    elif opcion == "4":
        filtro=input("Escribe aca el telefono: ")
        filtrarTelefono(filtro)
    elif opcion == "5":
        print("Salida del Modulo Exitosa")
    else:
        print("Opcion no reconocida, Ejecucion finalizada...")

menu()
