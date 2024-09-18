print("Programacion POO")
# Definicion de clases
class Perro:
    # Funciones dentro de la clase
    def mordudera(self):
        print("El perro mordio a un niño")
    def datosperro(self,nombre,edad):
        print(f" Nombre : {nombre} edad : {edad}")


# zona de creacion de objeto
Pitbull=Perro()

# Zona de uso de objetos

Pitbull.datosperro("Princesa",17)
Pitbull.mordudera()
