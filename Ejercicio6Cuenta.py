
class Persona: 
  def __init__(self,nombre,apellido,dni):
     self.nombre = nombre
     self.apellido = apellido
     self.dni = dni
  def __str__(self):
    return f"\nNombre: {self.nombre} \nApellido: {self.apellido} \nDni: {self.dni}"

 
class Cuenta:
   def __init__(self,cantidad):
        self.persona = persona1
        self.cantidad = cantidad
   def __str__(self):
        return f"{self.persona.__str__()} \nCantidad en cuenta : {self.cantidad}"
   def ingresar(self,monto):
        if monto>0:
          self.cantidad=monto
        else:
          print("Error. El monto no puede ser negativo")
   def retirar(self,monto_retirar):
     self.cantidad-=monto_retirar
    
   

persona1 = Persona("Julieta","Sanchez",35662725)       
cuenta1=Cuenta(0)
#print(f"{persona1}")
print(f"{cuenta1}")
monto_1 = float(input("¿Que cantidad de dinero desea ingresar a la cuenta?"))
cuenta1.ingresar(monto_1)
print(f"{cuenta1}")
monto_retirar = float(input("¿Que cantidad de dinero desea retirar a la cuenta?"))
cuenta1.retirar(monto_retirar)
print(f"{cuenta1}")


  