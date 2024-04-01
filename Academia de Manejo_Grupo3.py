##G3_2024_1C_Programación_Básica_SC-115_Heredia_G03_Academia de manejo

import os
import time 
import os #Importamos esta libreria para hacer uso de la funcion os.sytem
import time  # Importamos esta libreria para hacer uso de la funcion time.sleep

bienvenida = "Bienvenido Academia de Manejo CR"

#Aqui centramos el texto de bienvenida con la funcion center y le damos de referencia parametros 
print("\n"+bienvenida.center(200, " "))

#Aqui el numero se va registrar
nombre_usuario = input ("Ingrese su nombre: ")
correo_electronico = input ("Ingrese su correo electronico: ")
num_telefono = int (input ("Ingrese su numero de telefono: "))

#El sistema hace una breve espera antes de limpir consola
time.sleep (0.5)
os.system ("cls")
os.system ("cls") #Esta funcion nos limpia consola

print ("Academica de Manejo CR".center(200," "))

Horarios = [["Lunes(L)","8 a.m.","9 a.m.","10 a.m.","11 a.m.","12 p.m.","1 p.m.","2 p.m.","3 p.m.","4 p.m.","5 p.m.","6 p.m.","7 p.m.","8 p.m.","9 p.m."],
            ["Martes (K)","8 a.m.","9 a.m.","10 a.m.","11 a.m.","12 p.m.","1 p.m.","2 p.m.","3 p.m.","4 p.m.","5 p.m.","6 p.m.","7 p.m.","8 p.m.","9 p.m."],
            ["Miercoles(M)","8 a.m.","9 a.m.","10 a.m.","11 a.m.","12 p.m.","1 p.m.","2 p.m.","3 p.m.","4 p.m.","5 p.m.","6 p.m.","7 p.m.","8 p.m.","9 p.m."],
            ["Jueves(J)","8 a.m.","9 a.m.","10 a.m.","11 a.m.","12 p.m.","1 p.m.","2 p.m.","3 p.m.","4 p.m.","5 p.m.","6 p.m.","7 p.m.","8 p.m.","9 p.m."],
            ["Viernes(V)","8 a.m.","9 a.m.","10 a.m.","11 a.m.","12 p.m.","1 p.m.","2 p.m.","3 p.m.","4 p.m.","5 p.m.","6 p.m.","7 p.m.","8 p.m.","9 p.m."],
            ["Sabados(S)","8 a.m.","9 a.m.","10 a.m.","11 a.m.","12 p.m.","1 p.m.","2 p.m.","3 p.m.","4 p.m.","5 p.m.","6 p.m.","7 p.m.","8 p.m.","9 p.m."]] #Variable para los horarios

def MostrarHorarios(x):
    for dia in range(len(Horarios)):
        for hora in range(len(Horarios[dia])):
            print(Horarios[dia][hora], end =" ")
        print("\n")

def CursoTeorico(MostrarHorario):

    while True:
        MostrarHorarios(Horarios)
        CantidadHoras = int(input("Horario: de 8 a.m. a 9 p.m.\nIngrese la cantidad de horas que desea contratar: "))
        Dia = int(input("Ingrese el numero del dia que desea reservar(Ejemplo: Lunes(L) = 1)\n:"))
        Hora = int(input("Ingrese el numero del la hora que desea reservar(Ejemplo: 8 a.m. = 1)\n:"))
        if Horarios[Dia-1][Hora] != "":
            print("Espacio Reservado:",Horarios[Dia-1][0],Horarios[0][Hora])
            Nombre = str(input("Espacio va a ser reservado a nombre de:"))
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
    

def ClasesdeManejo():
    while True:
        MostrarHorarios(Horarios)
        CantidadHoras = int(input("Horario: de 8 a.m. a 9 p.m.\nIngrese la cantidad de horas que desea contratar: "))
        Dia = int(input("Ingrese el numero del dia que desea reservar(Ejemplo: Lunes(L) = 1)\n:"))
        Hora = int(input("Ingrese el numero del la hora que desea reservar(Ejemplo: 8 a.m. = 1)\n:"))
        if Horarios[Dia-1][Hora] != "":
            print("Espacio Reservado:",Horarios[Dia-1][0],Horarios[0][Hora])
            Nombre = str(input("Espacio va a ser reservado a nombre de:"))
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

def crear_factura_electronica():
    # Datos de la factura
    numero_factura = int(input("Número de factura: "))
    fecha = input("Fecha de la factura: ")
    descripcion = input("Descripción del producto o servicio: ")
    precio = float(input("Precio: "))
    # Imprimimos un mensaje de confirmacion
    print("Factura electronica generada de manera correcta.")



#MenuPrincipal
opcion = 1
menu = print("1. Curso Teorico"
             "\n2. Clases de Manejo"
             "\n3. Dictamen Medico"
             "\n4. Crear Factura Electronica"
             "\n5. Salir")

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
    FacturaElectronica = str(input("Desea solicitar factura electronica? (SI/NO)\n:"))
    if FacturaElectronica == "No" or FacturaElectronica == "NO":
        print("Gracias por utilizar nuestros servicios!")
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
    FacturaElectronica = str(input("Desea solicitar factura electronica? (SI/NO)\n:"))
    if FacturaElectronica == "No" or FacturaElectronica == "NO":
        print("Gracias por utilizar nuestros servicios!")
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
    print("Gracias por utilizar nuestros servicios!")
    
#Salir
elif opcion == 4:
    crear_factura_electronica()

elif opcion == 5:
    print("\nGracias por usar nuestro programa\n")
