
def crear_factura_electronica(cedula, nombre, direccion, correo_electronico):
# Datos de la factura
  numero_factura = int(input("Número de factura: "))
  fecha = input("Fecha de la factura: ")
  descripcion = input("Descripción del producto o servicio: ")
  precio = float(input("Precio: "))
# Imprimimos un mensaje de confirmacion
  print("Factura electronica generada de manera correcta.")

# Solicitamos los datos del cliente para crear la factura
cedula = input("Cedula: ")
nombre = input("Nombre completo: ")
direccion = input("Direccion: ")
correo_electronico = input("Correo electronico: ")

# Creamos la factura electronica
crear_factura_electronica(cedula, nombre, direccion, correo_electronico)
