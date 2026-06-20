#1 Datos deben manerjar
#cada vez que se agrege libro, debe incluirse a una colección.
#campod : id (>0),titulo(no vacio/sin espacios en blanco),precio(>0), disponible(boolean).
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

def AgregarLibro(libros):
     
        libreria.append(libros)
    
        return print(f"Se ha ingresado el libro {libros["titulo"]}")


def BuscaID(libreria,b_id):
     
     for indice, valor in enumerate(libreria):

            if valor["id"] == b_id:
                 print("El ID ingresado ya existe!")
                       
                       

     return b_id

libreria = []
dic_libros ={}

while True:
    try:
            print(f"========== MENÚ PRINCIPAL ==========\n1. Agregar libro\n2. Buscar libro\n3. Eliminar libro\n4. Actualizar disponibilidad\n5. Mostrar libros\n6. Salir\n=====================================")

            menu = int(input("Ingrese una opción de 1 a 6 para acceder al menu\n=====>"))

            match menu:
                 case 1:
                      while True:
                           try:
                               
                                id = int(input("Ingrese el ID (debe ser único y >0) : "))
                                busca_id = BuscaID(libreria,id)



                                titulo = int(input("Ingrese el Titulo del libro : "))
                                precio = int(input("Ingrese el Precio(debe ser >0) : "))
                                estado = input("Ingrese la opción (SI/NO)").upper()

                                if disponible == "SI":
                                        disponible = True
                                elif disponible == "NO":
                                        disponible = False

                                
                                

                                if busca_id == False and id >0 and titulo != "" and  precio >0:
                                        
                                        dic_libros = {"id": id, "titulo": titulo, "precio":precio,"disponible":disponible}

                                        AgregarLibro(dic_libros)
                                        
                                else:
                                        print(f"El id se esta repitiendo")

                           except ValueError as ILE:
                                print(f"Error al ingresar libro :{ILE}")
                 case 2:
                      pass
                 case 3:
                      pass
                 case 4:
                      pass
                 case 5:
                      pass
                 case 6:
                      break
                 case _:
                      print("El valor ingresado es incorrecto, debe ser de 1 a 6")
    except ValueError as EM:
        print(f"Error al ingresar una opción, los numeros a ingresar deben ser de 1 a 6")
    except Exception as EM:
        print(f"Error no identificado : {EM}")
