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
#git checkout HEAD/MASTER // se usara más adelante
#git branch -M main / crea la rama principal a publicar github
#git remote add origin https
#git push origin main
#publica el cambio en el remoto, si yo agrego el
#git add .
#git push
###############################################################################################
#########################FUNCIONES#############################################################
###############################################################################################
def AgregarLibro(libros):
     print("Pasa a agregar 1")
     if libros["id"]>0 and libros["titulo"]!= "" and libros["precio"]>0:
          print("Pasa a agregar 2")
          if libros["disponible"] == "SI":
             libros["disponible"] == True
          else:
             libros["disponible"] == False
     
          libreria.append(libros)
          print(f"Se ha ingresado el libro {libros["titulo"]}")
          retorno_ingreso_libro = False
     else:
          print(f"No fue posible ingresar el libro, revise los datos ingresados")
          print(f"ID (debe ser único y  mayor a 0) : {libros["id"]}")
          print(f"TITULO (debe ser texto) : {libros["titulo"]}")
          print(f"PRECIO (debe ser mayor a 0): {libros["precio"]}")
          print(f"DISPONIBLE (Debe ser SI o NO) {libros["disponible"]}")
          retorno_ingreso_libro = True
     return retorno_ingreso_libro
###############################################################################################
def BuscaXNombre(b_libreria, str_libro_buscado):
     cuenta_libros =0
     print("===========================================")
     for indice, valor in enumerate(b_libreria):
          #if valor["titulo"] == str_libro_buscado and indice !=0:
          if valor["titulo"] == str_libro_buscado:
               cuenta_libros  +=1
               print("El libro se encuentra registrado")
               print(f"INDICE LIBRERIA : {indice}")
               print(f"ID : {valor["id"]}")
               print(f"Titulo : {valor["titulo"]}")
               print(f"Precio : {valor["precio"]}")
               if valor["disponible"] == True:
                    print(f"Disponible : SI")
               else:
                    print(f"Disponible : NO")
               print("===========================================")
     if cuenta_libros == 0:
          print("No se ha logrado encontrar el libro que busca")
          print("===========================================")
     
     while (repite_busqueda := input("¿Desea realizar una nueva busqueda? SI/NO : ").strip().upper()) in ("SI","NO"):
          if repite_busqueda == "SI":
               return True
          elif repite_busqueda == "NO":
               return False
          else:
               print("La opción ingresada es incorrecta, debe ser SI o NO. ")
###############################################################################################
def BuscaXId_Filtro2(b_libreria, int_id):
     cuenta_libros = 0
     indice_libro = 0
     print("===========================================")
     for indice, valor in enumerate(b_libreria):
          #if valor["id"] == int_id and indice !=0:
          if valor["id"] == int_id:
               cuenta_libros+=1
               print("El libro se encuentra registrado")
               print(f"INDICE LIBRERIA : {indice}")
               print(f"ID : {valor["id"]}")
               print(f"Titulo : {valor["titulo"]}")
               print(f"Precio : {valor["precio"]}")
               if valor["disponible"] == True:
                    print(f"Disponible : SI")
               else:
                    print(f"Disponible : NO")
               print("===========================================")
               indice_libro = indice
     if cuenta_libros == 0:
          print("No se ha logrado encontrar el libro que busca")
          print("===========================================")
     return indice_libro

def BuscaXId(b_libreria, int_id):
     cuenta_libros = 0
     print("===========================================")
     for indice, valor in enumerate(b_libreria):
          if valor["id"] == int_id:
          #if valor["id"] == int_id and indice !=0:
               cuenta_libros+=1
               print("El libro se encuentra registrado")
               print(f"INDICE LIBRERIA : {indice}")
               print(f"ID : {valor["id"]}")
               print(f"Titulo : {valor["titulo"]}")
               print(f"Precio : {valor["precio"]}")
               if valor["disponible"] == True:
                    print(f"Disponible : SI")
               else:
                    print(f"Disponible : NO")
               print("===========================================")
     if cuenta_libros == 0:
          print("No se ha logrado encontrar el libro que busca")
          print("===========================================")
     while (repite_busqueda := input("¿Desea realizar una nueva busqueda? SI/NO : ").strip().upper()) in ("SI","NO"):
          if repite_busqueda == "SI":
               return True
          elif repite_busqueda == "NO":
               return False
          else:
               print("La opción ingresada es incorrecta, debe ser SI o NO. ")
###############################################################################################
def BuscaXPrecio(b_libreria, lowprice, maxprice):
     cuenta_libros = 0
     for indice, valor in enumerate(b_libreria):
          print("===========================================")
          ##############START LISTA LIBROS EN PRECIO#####################
          #if valor["precio"] >= lowprice and valor["precio"]<=maxprice and indice !=0:
          if valor["precio"] >= lowprice and valor["precio"]<=maxprice:
               cuenta_libros+=1
               print("El libro se encuentra registrado")
               print(f"INDICE LIBRERIA : {indice}")
               print(f"ID : {valor["id"]}")
               print(f"Titulo : {valor["titulo"]}")
               print(f"Precio : {valor["precio"]}")
               if valor["disponible"] == True:
                    print(f"Disponible : SI")
               else:
                    print(f"Disponible : NO")
               print("===========================================")
          ##############END LISTA LIBROS EN PRECIO#####################
     if cuenta_libros == 0:
          print("No se ha logrado encontrar el libro que busca")
          print("===========================================")
     while (repite_busqueda := input("¿Desea realizar una nueva busqueda? SI/NO : ").strip().upper()) in ("SI","NO"):
          if repite_busqueda == "SI":
               return True
          elif repite_busqueda == "NO":
               return False
          else:
               print("La opción ingresada es incorrecta, debe ser SI o NO. ")

###############################################################################################
def BuscaID(b_libreria,b_id):
     for indice, valor in enumerate(b_libreria):

          if valor["id"] == b_id:
               
               print("El ID ingresado ya existe, intente nuevamente!")
               return True
          else: 
               print("El ID ingresado es valido")
               return False
###############################################################################################
def Elimina_Libro(b_libreria,b_id):
     print("===========================================")
     print("==============ELIMINAR LIBRO===============")

     busca_indice = BuscaXIdXEliminar(b_libreria,b_id)
     if busca_indice != 0:
          libro_eliminado = b_libreria.pop(busca_indice)
          print(libro_eliminado)
     else:
          print(f"El libro ID : {b_id} no se encuentra para ser eliminado")
     return False
###############################################################################################
def Actualiza_Libro(b_libreria,b_id):
     print("===========================================")
     print("==============Actualiza LIBRO===============")
     busca_indice = BuscaXId_Filtro2(b_libreria,b_id)
     if busca_indice != 0:
          b_libreria[busca_indice]["titulo"] = input("Ingrese el nuevo titulo :")
          b_libreria[busca_indice]["precio"] = int(input("Ingrese el nuevo precio :"))
          while (disponible := input("Ingrese el nuevo disponibilidad (SI/NO):").strip().upper()) in ("SI","NO"):
               if disponible == "SI":
                    b_libreria[busca_indice]["disponible"] == True
               elif disponible == "NO":
                    b_libreria[busca_indice]["disponible"] == False
               else:
                    print("La opción ingresada es incorrecta, debe ser SI o NO. ")
     else:
          print(f"El libro ID : {b_id} no se encuentra para ser eliminado")
     return False
###############################################################################################
###########################MAIN################################################################
###############################################################################################

#libreria = [{"id": 0, "titulo": "BASE", "precio":0,"disponible":False}]
libreria =[]
dic_libros ={}

while True:
    try:
            print(f"========== MENÚ PRINCIPAL ==========\n1. Agregar libro\n2. Buscar libro\n3. Eliminar libro\n4. Actualizar disponibilidad\n5. Mostrar libros\n6. Salir\n=====================================")

            menu = int(input("Ingrese una opción de 1 a 6 para acceder al menu\n=====>"))
            c_ingresa_libro = True
            c_busca_libro = True
            c_elimina_libro = True
            c_actualiza_libro = True

            match menu:
                 case 1:
                      while c_ingresa_libro:
                         try:
                              busca_id = True
                              while busca_id:
                                   id = int(input("Ingrese el ID (debe ser único y >0) : "))
                                   busca_id = BuscaID(libreria,id)



                              titulo = input("Ingrese el Titulo del libro : ")
                              precio = int(input("Ingrese el Precio(debe ser >0) : "))
                              while True:
                                   estado = input("Ingrese la disponibilidad (SI/NO)").strip().upper()

                                   if estado in ("SI","NO"):
                                        print("Pasa")
                                        break
                                   else:
                                        print("El valor ingresado es incorrecto")
                                        
                              dic_libros = {"id": id, "titulo": titulo, "precio":precio,"disponible":estado}

                              c_ingresa_libro = AgregarLibro(dic_libros)
                                        
                         except ValueError as ILE:
                              print(f"Error al ingresar libro :{ILE}")
                 case 2:
                      while c_busca_libro:
                         try:
                              print("==Busqueda de libro==")
                              menu_busca_libro = int(input("¿Como desea buscar el libro? \n1.-ID\n2.-Nombre\n3.-Filtrar por precio\n4.-Salir al menu principal\nIngrese una opción : "))
                              match menu_busca_libro:
                                   case 1:
                                        busca_id_libro = int(input("Ingrese el ID del libro a buscas : "))
                                        c_busca_libro = BuscaXId(libreria,busca_id_libro)
                                   case 2:
                                        busca_nombre_libro = input("Ingrese el nombre del libro a buscar : ")
                                        c_busca_libro = BuscaXNombre(libreria,busca_nombre_libro)
                                   case 3:
                                        busca_lowprice_libro = int(input("Ingrese el valor minimo a buscar : "))
                                        busca_maxprice_libro = int(input("Ingrese el valor maximo a buscar : "))
                                        c_busca_libro =BuscaXPrecio(libreria,busca_lowprice_libro,busca_maxprice_libro)
                                   case 4:
                                        break
                                   case _:
                                        print("La opción de menu busqueda libros es incorrecta")   
                         except ValueError as BLE:
                              print(f"Error al buscar libro :{BLE}")
                         except Exception as BLE_EX:
                              print(f"Error al buscar libro : EX =>{BLE_EX}")
                         
                 case 3:
                      while c_elimina_libro:
                         try:
                              print("==Eliminación de libro==")
                              busca_eliminar_libro = int(input("Ingrese el Indice del libro que desea eliminar : "))
                              
                              c_elimina_libro = Elimina_Libro(libreria, busca_eliminar_libro)
                              
                         except ValueError as ELE:
                              print(f"Error al eliminar libro :{BLE}")
                         except Exception as BLE_EX:
                              print(f"Error al eliminar libro : EX =>{BLE_EX}")

                 case 4:
                      while c_actualiza_libro:
                         try:
                              print("==Actualización de libro==")
                              act_libro = int(input("Ingrese el Indice del libro que desea Actualizar : "))
                              
                              c_actualiza_libro = Elimina_Libro(libreria, act_libro)
                              
                         except ValueError as ALE:
                              print(f"Error al actualizar libro :{ALE}")
                         except Exception as ALE_EX:
                              print(f"Error al actualizar libro : EX =>{ALE_EX}")

                 case 5:
                    infinito = float('inf') 
                    BuscaXPrecio(libreria,0,infinito)
                 case 6:
                      print("Gracias por usar el sistema. Vuelva Pronto")
                      break
                 case _:
                      print("El valor ingresado es incorrecto, debe ser de 1 a 6")
    except ValueError as EM:
        print(f"Error al ingresar una opción, los numeros a ingresar deben ser de 1 a 6")
    except Exception as EM:
        print(f"Error no identificado : {EM}")
