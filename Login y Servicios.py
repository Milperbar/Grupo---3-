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



#MenuPrincipal
opcion = 1
menu = print("1. Curso Teorico"
          "\n2. Clases de Manejo"
          "\n3. Dictamen Medico"
          "\n4. Salir"
          )
opcion = int (input ("\nSeleccionar una opcion: "))


#CursoTeorico
if opcion == 1:
    Reserva = 0
    NumFactura = 1000000000
    from datetime import datetime
    Fecha = datetime.now()
    Servicio = "Curso Teorico"
    print(Servicio.center(200," "))
    Horarios = ("8 a.m.","9 a.m.","10 a.m.","11 a.m.","12 p.m.","1 p.m.","2 p.m.","3 p.m.","4 p.m.","5 p.m.","6 p.m.","7 p.m.","8 p.m.","9 p.m.") #Variable para los horarios
    Dias = ("Lunes(L)","Martes(K)","Miercoles(M)","Jueves(J)","Viernes(V)","Sabado(S)") #Variable para los dias



    while True:
        CantidadHoras = int(input("Horario: de 8 a.m. a 9 p.m.\nIngrese la cantidad de horas que desea contratar: "))
        if CantidadHoras > 14 or CantidadHoras < 1:
            print("Cantidad de hora seleccionada no es permitida para contratar. Por favor ingrese de nuevo la cantidad de horas")

        else:
            CantidadDias = int(input("Lunes(L),Martes(K), Miercoles(M),Jueves(J),Viernes(V),Sabado(S)\nIngrese la cantidad de dias en los que desea distribuir las horas:"))

            from random import choice #Esta funcion hara que, dependiendo de la cantidad de horas que el usuario quiere contratar, elija una hora de la variable "Horarios" de forma aleatoria
            HorariosDisponibles = choice(Horarios)
            
            for _ in range(CantidadHoras):
                print("Horas diponibles:",choice(Horarios))

            from random import choice #Esta funcion hara que, dependiendo de la cantidad de horas que el usuario quiere contratar, elija una hora de la variable "Dias" de forma aleatoria
            DiasDisponibles = choice(Dias)

            for _ in range(CantidadDias):
                print("Dias disponibles:",choice(Dias))

            Seleccion = str(input("Acepta los horarios y dias ofrecidos? SI/NO\n:"))
            
            if Seleccion == "No" or Seleccion == "no":
                continue #Si el usuario decide que no es un horario adecuado escribiendo "No", el programa va a volver a solictar la informacion de horario y dias y generara los disponibles de forma aleatoria

            else:
                Reserva += 1
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
                
    FacturaElectronica = str(input("Desea solicitar factura electronica? (SI/NO)\n:"))
    if FacturaElectronica == "No" or FacturaElectronica == "NO":
        print("Gracias por utilizar nuestros servicios!")
    else:
        print("Nombre:",nombre_usuario)
        print("Correo_electronico:",correo_electronico)
        print("Numero de telefono:",num_telefono)
        from datetime import datetime
        print("Fecha de emision:",datetime.strftime(Fecha,"%d/%m/%Y %H:%M:%S"))
        print("Numero de Factura:",NumFactura)
        print("Item:",Servicio)
        print("Numero de Reserva: N°",Reserva)
        print("Precio:",CostoTotal) 
    print("Gracias por utilizar nuestros servicios!")


#Clases de Manejo
elif opcion == 2:
    Reserva = 0
    NumFactura = 1000000000
    from datetime import datetime
    Fecha = datetime.now()
    Servicio= "Clases de Manejo"
    print(Servicio.center(200," "))
    Horarios = ("8 a.m.","9 a.m.","10 a.m.","11 a.m.","12 p.m.","1 p.m.","2 p.m.","3 p.m.","4 p.m.","5 p.m.") #Variable para los horarios
    Dias = ("Martes(K)","Miercoles(M)","Jueves(J)","Viernes(V)","Sabado(S)","Domingo(D)") #Variable para los dias
    
    while True:
        CantidadHoras = int(input("Horario: de 8 a.m. a 9 p.m.\nIngrese la cantidad de horas que desea contratar: "))
        if CantidadHoras > 14 or CantidadHoras < 1:
            print("Cantidad de hora seleccionada no es permitida para contratar. Por favor ingrese de nuevo la cantidad de horas")

        else:
            Carro = int(input("Va a hacer uso de carro propio o se necesita que se le proporcione uno? \n1.Carro Propio  2.Carro de la Academia de Manejo\n:")) #Debe seleccionar el carro a usar
            CantidadDias = int(input("Martes(K), Miercoles(M),Jueves(J),Viernes(V),Sabado(S),Domingo(D)\nIngrese la cantidad de dias en los que desea distribuir las horas:"))

            from random import choice #Esta funcion hara que, dependiendo de la cantidad de horas que el usuario quiere contratar, elija una hora de la variable "Horarios" de forma aleatoria
            HorariosDisponibles = choice(Horarios)
            
            for _ in range(CantidadHoras):
                print("Horas diponibles:",choice(Horarios))

            from random import choice #Esta funcion hara que, dependiendo de la cantidad de horas que el usuario quiere contratar, elija una hora de la variable "Dias" de forma aleatoria
            DiasDisponibles = choice(Dias)

            for _ in range(CantidadDias):
                print("Dias disponibles:",choice(Dias))

            Seleccion = str(input("Acepta los horarios y dias ofrecidos? SI/NO\n:"))
            if Seleccion == "No" or Seleccion == "no":
                continue #Si el usuario decide que no es un horario adecuado escribiendo "No", el programa va a volver a solictar la informacion de horario y dias y generara los disponibles de forma aleatoria

            else:
                Reserva += 1
                NumFactura += 1 
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

    FacturaElectronica = str(input("Desea solicitar factura electronica? (SI/NO)\n:"))
    if FacturaElectronica == "No" or FacturaElectronica == "NO":
        print("Gracias por utilizar nuestros servicios!")
    else:
        print("Nombre:",nombre_usuario)
        print("Correo_electronico:",correo_electronico)
        print("Numero de telefono:",num_telefono)
        from datetime import datetime
        print("Fecha de emision:",datetime.strftime(Fecha,"%d/%m/%Y %H:%M:%S"))
        print("Numero de Factura:",NumFactura)
        print("Item:",Servicio)
        print("Numero de Reserva: N°",Reserva)
        print("Precio:",CostoTotal)
    print("Gracias por utilizar nuestros servicios!")
        

#Dictamen Medico
    
elif opcion == 3:
    Reserva = 0
    NumFactura = 1000000000
    from datetime import datetime
    Fecha = datetime.now()
    Servicio = "Dictamen Medico"
    print(Servicio.center(200," "))
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

    #Factura elecronica sin costo?

    print("Gracias por utilizar nuestros servicios!")
    
#Salir
elif opcion == 4:
    print("\nGracias por usar nuestro programa\n")
