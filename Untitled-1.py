#modelo sin espacios , anio int > 1900, precio >0, disponible (true o false)

#cada diccionario se guarda en una colección

#open code agentes locales para entrenar


#git cada vez que creas un codigo solo se crea en ese computador de manera local (repositoria local)

#github // repositorio en la nube, sirve mayormente para entornos de trabajo.

#gir es una herramienta para utilizar en nuestros compitadores / se llama git.

# el CLI es una linea de comandos, si se engresa git hace algo, git-version 

#git init = inicializa el proyecto en la carpeta actual

#git status = entrega el estado de la carpeta actual

#git add = añade un cambio al repositorio

#git commit -m "" crea una nueva versión 

#git checkout HEAD/MASTER // se usara más adelante

#git branch -M main / creal la rama principal a publicar github

#git remote add origin https

#git push origin main

#publica el cambio en el remoto, si yo agrego el

#git add .

#git push
from datetime import date

def validaModelo(modelo):
    if modelo.strip() == "":
        return True
    else:
        return False

def validaAnio(anio):
    try:
        anio_validar = int(anio)
        anio_actual = date.today().year

        if anio > 1900 and anio < anio_actual:
            return True
        else:
            return False
    except ValueError as Error_Anio:
        return False

def validaPrecio(precio):
    try:
        precio_validar = int(precio)
        if precio > 0:
            return True
        else:
            return False
    except ValueError as Error_Precio:
        return False
##############################################################################################################
def buscaVehiculo(lista,modelo):

    for indice, valor in enumerate(lista):
        valor["modelo"] == modelo
        return indice

    return -1
def AgregarVehiculo(lista):
    
    while True:
        try:
            print("==Agregar vehículo==")
            modelo = input("Ingrese el modelo del vehiculo : ")
            anio = input("Ingrese el año del vehiculo : ")
            precio = input("Ingrese el precio del vehiculo : ")

            valida_modelo = validaModelo(modelo)
            valida_anio= validaAnio(anio)
            valida_precio = validaPrecio(precio)

            busca_vehiculo = buscaVehiculo(lista,modelo.strip())

            if busca_vehiculo != -1:
                print(f"El vehiculo ya existe para el modelo {modelo}")
        
                return

            if valida_modelo == True and valida_anio == True and valida_precio == True:
                dic_vehiculo = {
                    "modelo": modelo,
                    "anio": int(anio),
                    "precio": float(precio),
                    "disponible": False
                }  

                lista.append(dic_vehiculo)
                print("Vehiculo agregado correctamente.")
            else:
                print("Los datos ingresados no cumplen con las validaciones")


        except ValueError as error_addv:
            print(f"Error al ingresar vehiculo {error_addv}")
def actualizarVehiculos(lista):

    for vehiculo in lista:
        if vehiculo["anio"] >= 2020:
            vehiculo["disponible"] = True
        else:
            vehiculo["disponible"] = False

    print("Se actualizaron los registros de vehiculos")

def mostrarVehiculos(lista):

    if len(lista) == 0:
        print("No existen vehiculos registrados aún")
        return

    actualizarVehiculos(lista)

    print("=== LISTA DE VEHICULOS ===")
    for vehiculo in lista:
        print(f"Modelo: {vehiculo['modelo']}")
        print(f"Precio: {vehiculo['precio']}")
        print(f"Año: {vehiculo['anio']}")

        if vehiculo['disponible']:
            print(f"Disponible?: DISPONIBLE")
        else:
            print(f"Disponible?: NO DISPONIBLE")
##############################################################################################################

#Plataforma de vehiculos
#MAIN
lista_vehiculos = []

main_menu = True
while main_menu:
    try:
        print("========== MENÚ PRINCIPAL ========== \n1. Agregar vehículo \n2. Buscar vehículo \n3. Eliminar vehículo \n4. Actualizar disponibilidad \n5. Mostrar vehículos \n6. Salir") 
        menu = int(input("Ingrese una opción valida"))

        match menu:
            case 1:
                AgregarVehiculo(lista_vehiculos)         
            case 2:
                modeloBuscado = input("Ingresa el modelo de vehiculo a buscar: ")
                posicion = buscaVehiculo(lista_vehiculos,modeloBuscado)

                if posicion != -1:
                    print(f"Vehiculo encontrado en la posición {posicion}")

                    vehiculoEncontrado = listaVehiculos[posicion]

                    print(f"Modelo: {vehiculoEncontrado['modelo']}")
                    print(f"Precio: {vehiculoEncontrado['precio']}")
                    print(f"Año: {vehiculoEncontrado['anio']}")

                    if vehiculoEncontrado['disponible']:
                        print(f"Disponible?: DISPONIBLE")
                    else:
                        print(f"Disponible?: NO DISPONIBLE")
                else:
                    print(f"El vehículo '{modeloBuscado}' no se encuentra registrado.")

            case 3:
                passmodeloBuscado = input("Ingresa el modelo de vehiculo a buscar: ")

                posicion = buscaVehiculo(listaVehiculos, modeloBuscado)

                if posicion != -1:
                    listaVehiculos.pop(posicion)

                    print(f"Vehiculo con modelo '{modeloBuscado}' eliminado")
                else:
                    print(f"El vehículo '{modeloBuscado}' no se encuentra registrado.")
            case 4:
                actualizarVehiculos(listaVehiculos)
            case 5:
                mostrarVehiculos(listaVehiculos)
            case 6:
                print("Gracias por usar el sistema. Vuelva Pronto")
                break
            case _:
                print("La opción ingresada es incorrecta, debe ser de 1 a 6")
    except ValueError as EM:
        print(f"El valor asignado es incorrecto")
    except Exception as EXM:
        print(f"Error inesperado en Menu {EXM}")
