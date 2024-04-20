##G3_2024_1C_Programación_Básica_SC-115_Heredia_G03_Academia de manejo

import os
import time 
import os #Importamos esta libreria para hacer uso de la funcion os.sytem
import time  # Importamos esta libreria para hacer uso de la funcion time.sleep

bienvenida = "Bienvenido Academia de Manejo CR"

#Aqui centramos el texto de bienvenida con la funcion center y le damos de referencia parametros 
print("\n"+bienvenida.center(200, " "))

#Aqui el numero se va registrar
from datetime import datetime
Fecha = datetime.now()
Fecha = datetime.strftime(Fecha,"%d/%m/%Y %H:%M:%S")
print(Fecha)
nombre_usuario = str(input ("Ingrese su nombre completo: "))
correo_electronico = input ("Ingrese su correo electronico: ")
num_telefono = int(input ("Ingrese su numero de telefono: "))


#El sistema hace una breve espera antes de limpir consola
time.sleep (0.5)
os.system ("cls")
os.system ("cls") #Esta funcion nos limpia consola

print ("Academica de Manejo CR".center(200," "))

Horarios = [["Lunes","8 a.m.","9 a.m.","10 a.m.","11 a.m.","12 p.m.","1 p.m.","2 p.m.","3 p.m.","4 p.m.","5 p.m.","6 p.m.","7 p.m.","8 p.m.","9 p.m."],
            ["Martes","8 a.m.","9 a.m.","10 a.m.","11 a.m.","12 p.m.","1 p.m.","2 p.m.","3 p.m.","4 p.m.","5 p.m.","6 p.m.","7 p.m.","8 p.m.","9 p.m."],
            ["Miercoles","8 a.m.","9 a.m.","10 a.m.","11 a.m.","12 p.m.","1 p.m.","2 p.m.","3 p.m.","4 p.m.","5 p.m.","6 p.m.","7 p.m.","8 p.m.","9 p.m."],
            ["Jueves","8 a.m.","9 a.m.","10 a.m.","11 a.m.","12 p.m.","1 p.m.","2 p.m.","3 p.m.","4 p.m.","5 p.m.","6 p.m.","7 p.m.","8 p.m.","9 p.m."],
            ["Viernes","8 a.m.","9 a.m.","10 a.m.","11 a.m.","12 p.m.","1 p.m.","2 p.m.","3 p.m.","4 p.m.","5 p.m.","6 p.m.","7 p.m.","8 p.m.","9 p.m."],
            ["Sabados","8 a.m.","9 a.m.","10 a.m.","11 a.m.","12 p.m.","1 p.m.","2 p.m.","3 p.m.","4 p.m.","5 p.m.","6 p.m.","7 p.m.","8 p.m.","9 p.m."]] #Variable para los horarios

def MostrarHorarios():
    for dia in range(len(Horarios)):
        for hora in range(len(Horarios[dia])):
            print(Horarios[dia][hora], end =" ")
        print("\n")

def CursoTeorico(MostrarHorario):

    import os
    fileCursoTeorico = open("Registros Cursos Teoricos.doc","a")
        
    while True:
        CantidadHoras = int(input("Horario: de 8 a.m. a 9 p.m.\nIngrese la cantidad de horas que desea contratar: "))
        for repeticion in range (CantidadHoras):
            Dia = int(input("Ingrese el numero del dia que desea reservar\n1. Lunes, 2. Martes, 3.Miercoles, 4. Jueves, 5. Viernes, 6. Sabados\n:"))
            Hora = int(input("Ingrese el numero del la hora que desea reservar\n1. 8H, 2. 9H, 3. 10H, 4. 11H, 5. 12H, 6. 13H, 7. 14H, 8. 15H, 9. 16H, 10. 17H, 11. 18H, 12. 19H, 13. 20H, 14., 21H \n:"))
            if Horarios[Dia-1][Hora] != "":
                print("Espacio Reservado:",Horarios[Dia-1][0],Horarios[0][Hora])
                Nombre = str(input("Espacio va a ser reservado a nombre de:"))
                fileCursoTeorico = open("Registros Cursos Teoricos.doc","a+")
                fileCursoTeorico.write(Nombre)
                fileCursoTeorico.write(" ")
                fileCursoTeorico.write(Horarios[Dia-1][0])
                fileCursoTeorico.write(" ")
                fileCursoTeorico.write(Horarios[0][Hora])
                fileCursoTeorico.write("\n")
                fileCursoTeorico.close()
                Horarios[Dia-1][Hora] = Nombre
            else:
                print("Espacio seleccionado ya ha sido reservado")
        
            
        Seleccion = str(input("Acepta los horarios y dias ofrecidos? SI/NO\n:"))
        
        if Seleccion == "No" or Seleccion == "no":
            continue #Si el usuario decide que no es un horario adecuado escribiendo "No", el programa va a volver a solictar la informacion de horario y dias y generara los disponibles de forma aleatoria

        else:
            CostoTotal = CantidadHoras * 2000 #Costo Total de curso mediante las horas contradas
            print("Costo Total del curso:",CostoTotal,"\nSeleccione la forma de pago")
            FormadePago = int(input("1.De Contado/Efectivo  2.Tarjeta de Credito/Debito\n:")) #Debe seleccionar la forma de pago 

            if FormadePago == 1:
                print("Dirijase a nuestra sede en Heredia para realizar el pago del curso")
                break #Detiene el programa
            else:
                import webbrowser
                print("Ingrese al siguiente link para realizar en pago del curso:",webbrowser.open_new("https//ademicademanejocr.com")) #Direcciona al usuario a la pagina web donde se puede realizar el pago (link no existente, solo con fines de estudio)
                break #Detiene el programa
            
    

def ClasesdeManejo(MostrarHorario):
    
    import os
    fileClasesdeManejo = open("Registros Clases de Manejo.doc","a")
    
    while True:
        MostrarHorarios(Horarios)
        CantidadHoras = int(input("Horario: de 8 a.m. a 9 p.m.\nIngrese la cantidad de horas que desea contratar: "))
        Dia = int(input("Ingrese el numero del dia que desea reservar\n1. Lunes, 2. Martes, 3.Miercoles, 4. Jueves, 5. Viernes, 6. Sabados\n:"))
        Hora = int(input("Ingrese el numero del la hora que desea reservar\n1. 8H, 2. 9H, 3. 10H, 4. 11H, 5. 12H, 6. 13H, 7. 14H, 8. 15H, 9. 16H, 10. 17H, 11. 18H, 12. 19H, 13. 20H, 14., 21H \n:"))
        if Horarios[Dia-1][Hora] != "":
            print("Espacio Reservado:",Horarios[Dia-1][0],Horarios[0][Hora])
            Nombre = str(input("Espacio va a ser reservado a nombre de:"))
            fileClasesdeManejo = open("Registros Clases de Manejo.doc","a+")
            fileClasesdeManejo.write(Nombre)
            fileClasesdeManejo.write(" ")
            fileClasesdeManejo.write(Horarios[Dia-1][0])
            fileClasesdeManejo.write(" ")
            fileClasesdeManejo.write(Horarios[0][Hora])
            fileClasesdeManejo.write("\n")
            fileClasesdeManejo.close()
            Horarios[Dia-1][Hora] = Nombre
        else:
            print("Espacio seleccionado ya ha sido reservado")


        if CantidadHoras > 14 or CantidadHoras < 1:
            print("Cantidad de hora seleccionada no es permitida para contratar. Por favor ingrese de nuevo la cantidad de horas")

        else:
            Carro = int(input("Va a hacer uso de carro propio o se necesita que se le proporcione uno? \n1.Carro Propio  2.Carro de la Academia de Manejo\n:")) #Debe seleccionar el carro a usar

            Seleccion = str(input("Acepta los horarios y dias ofrecidos? SI/NO\n:"))

            if Seleccion == "No" or Seleccion == "no":
                continue #Si el usuario decide que no es un horario adecuado escribiendo "No", el programa va a volver a solictar la informacion de horario y dias y generara los disponibles de forma aleatoria

            else: 
                if Carro == 1:
                    CostoTotal = CantidadHoras * 3000 #Costo Total de curso tomando en cuenta las horas contradas y si el carro a utilizar es propio
                    print("Costo Total del curso:",CostoTotal,"\nSeleccione la forma de pago")
                    FormadePago = int(input("1.De Contado/Efectivo  2.Tarjeta de Credito/Debito\n:")) #Debe seleccionar la forma de pago
                elif Carro == 2:
                    CostoTotal = CantidadHoras * 4000 #Costo Total de curso tomando en cuenta las horas contradas y si el carro a utilizar es propio
                    print("Costo Total del curso:",CostoTotal,"\nSeleccione la forma de pago")
                    FormadePago = int(input("1.De Contado/Efectivo  2.Tarjeta de Credito/Debito\n:")) #Debe seleccionar la forma de pago

                    if FormadePago == 1:
                        print("Dirijase a nuestra sede en Heredia para realizar el pago del curso")
                        break #Detiene el programa
                    else:
                        import webbrowser
                        print("Ingrese al siguiente link para realizar en pago del curso: https//ademicademanejocr.com",webbrowser.open_new("https//ademicademanejocr.com")) #Direcciona al usuario a la pagina web donde se puede realizar el pago (link no existente, solo con fines de estudio)
                        break #Detiene el programa

def DictamenMedico():
    import os
    fileDictamenMedico = open("Registros Dictamenes Medicos.doc","a")
    
    TipoSangre = str(input("Tipo de Sangre\n:"))
    Peso = str(input("Ingrse su peso en Kg\n:"))
    Estatura = str(input("Ingrese su estatura en cm\n:"))
    Donador =str(input("Desea ser donador?(SI/NO)\n:"))
    #Costo?

    print("A continuacion podra ver los detalles referentes a su Dictamen Medico:") 
    print(nombre_usuario)
    print(correo_electronico)
    print(num_telefono)
    print(TipoSangre)
    print(Peso)
    print(Estatura)
    print(Donador)

    fileDictamenMedico = open("Registros Dictamenes Medicos.doc","a+")
    fileDictamenMedico.write(nombre_usuario)
    fileDictamenMedico.write(" ")
    fileDictamenMedico.write(TipoSangre)
    fileDictamenMedico.write(" ")
    fileDictamenMedico.write(Peso)
    fileDictamenMedico.write(" ")
    fileDictamenMedico.write(Estatura)
    fileDictamenMedico.write(" ")
    fileDictamenMedico.write(Donador)
    fileDictamenMedico.write(" ")
    fileDictamenMedico.write(num_telefono)
    fileDictamenMedico.write("\n")
    fileDictamenMedico.close()
    

def crear_factura_electronica():

    import os
    fileFacturas = open("Registros Facturas Electronicas.doc","a")
    
    # Datos de la factura
    fecha = print(Fecha)
    numero_factura = int(input("Número de factura: "))
    cliente = print("Cliente:",nombre_usuario,"\nCorreo:",correo_electronico,"\nNumero Telefonico:",num_telefono)
    descripcion = input("Descripción del producto o servicio: ")
    precio = float(input("Precio: "))
    # Imprimimos un mensaje de confirmacion
    print("Factura electronica generada de manera correcta.\n")

    fileFacturas = open("Registros Facturas Electronicas.doc","a+")
    fileFacturas.write(fecha)
    fileFacturas.write(" ")
    fileFacturas.write(numero_factura)
    fileFacturas.write(" ")
    fileFacturas.write(cliente)
    fileFacturas.write(" ")
    fileFacturas.write(descripcion)
    fileFacturas.write(" ")
    fileFacturas.write(precio)
    fileFacturas.write("\n")
    fileFacturas.close()


#MenuPrincipal
opcion = 1
while True:
    menu = print("1. Curso Teorico"
                 "\n2. Clases de Manejo"
                 "\n3. Dictamen Medico"
                 "\n4. Crear Factura Electronica"
                 "\n5. Mostrar Horarios"
                 "\n6. Revisar Archivo"
                 "\n7. Salir")

    opcion = int (input ("\nSeleccionar una opcion: "))


    #CursoTeorico
    if opcion == 1:
        Reserva = 0
        NumFactura = 1000000000
        from datetime import datetime
        Fecha = datetime.now()
        Servicio = "Curso Teorico"
        print(Servicio.center(200," "))
        CursoTeorico(Horarios)
        FacturaElectronica = int(input("Desea solicitar factura electronica? (1.SI/2.NO)\n:"))
        if FacturaElectronica == 2:
            print("Gracias por utilizar nuestros servicios! Volvera al menu principal\n")
        else:
            crear_factura_electronica()


    #ClasesdeManejo
    elif opcion == 2:
        Reserva = 0
        NumFactura = 1000000000
        from datetime import datetime
        Fecha = datetime.now()
        Servicio= "Clases de Manejo"
        print(Servicio.center(200," "))
        ClasesdeManejo(Horarios)
        FacturaElectronica = int(input("Desea solicitar factura electronica? (1.SI/2.NO)\n:"))
        if FacturaElectronica == 2:
            print("Gracias por utilizar nuestros servicios! Volvera al menu principal\n")
        else:
            crear_factura_electronica()


    #DictamenMedico
    elif opcion == 3:
        Reserva = 0
        NumFactura = 1000000000
        from datetime import datetime
        Fecha = datetime.now()
        Servicio = "Dictamen Medico"
        print(Servicio.center(200," "))
        DictamenMedico()
        print("Gracias por utilizar nuestros servicios! Volvera al menu principal\n")
        
    #Salir
    elif opcion == 4:
        crear_factura_electronica()

    elif opcion == 5:
        MostrarHorarios()

    elif opcion == 6:
        SeleccionArchivo = print("1.Registros Curso Teorico"
                                 "\n2.Registros Clases de Manejo"
                                 "\n3.Registros Dictamenes Medicos"
                                 "\n4.Registros Facturas Electronicas")
        SeleccionArchivo = int (input ("\nSeleccionar una opcion: "))

        if SeleccionArchivo == 1:
            import os
            fileCursoTeorico = open("Registros CursoTeorico.doc","r")
            mensaje = fileCursoTeorico.read()
            print(mensaje)
            
        if SeleccionArchivo == 2:
            import os
            fileClasesdeManejo = open("Registros ClasesdeManejo.doc","r")
            mensaje = fileClasesdeManejo.read()
            print(mensaje)

        if SeleccionArchivo == 3:
            import os
            fileDictamenMedico = open("Registros Dictamenes Medicos.doc","r")
            mensaje = fileDictamenMedico.read()
            print(mensaje)
            
        if SeleccionArchivo == 4:
            import os
            fileFacturas = open("Registros Facturas Electronicas.doc","r")
            mensaje = fileFacturas.read()
            print(mensaje)
        else:
            print("Archivo no existe")
                                 

    elif opcion == 7:
        print("\nGracias por usar nuestro programa\n")

    
