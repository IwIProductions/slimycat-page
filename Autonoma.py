# Codigo por Noah Leon
class Vehiculo:
    # Atributo de clase
    categoria = "Objeto Mecánico"

    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def mostrar_datos(self):
        print("\n----- VEHÍCULO -----")
        print(f"Marca : {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Color : {self.color}")

    def hacer_sonido(self):
        print(f"El {self.marca} {self.modelo} hace: ¡Brrmmm Brrmmm!")

    @classmethod
    def mostrar_categoria(cls):
        print("\nCategoría:", cls.categoria)


class Animal:
    # Atributo de clase
    reino = "Animal"

    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def mostrar_datos(self):
        print("\n----- ANIMAL -----")
        print(f"Nombre : {self.nombre}")
        print(f"Especie: {self.especie}")
        print(f"Edad   : {self.edad} años")

    def hacer_sonido(self):
        sonidos = {
            "Perro": "Guau Guau",
            "Gato": "Miau",
            "Vaca": "Muuu",
            "Pato": "Cuac",
            "Caballo": "Relincho"
        }

        sonido = sonidos.get(self.especie, "Sonido desconocido")
        print(f"{self.nombre} hace: {sonido}")

    @classmethod
    def mostrar_reino(cls):
        print("\nReino:", cls.reino)


print("=" * 50)
print("      REGISTRO DE VEHÍCULOS Y ANIMALES")
print("=" * 50)

print("\nIngrese los datos del Vehículo 1")
marca1 = input("Marca: ")
modelo1 = input("Modelo: ")
color1 = input("Color: ")

print("\nIngrese los datos del Vehículo 2")
marca2 = input("Marca: ")
modelo2 = input("Modelo: ")
color2 = input("Color: ")

print("\nIngrese los datos del Animal 1")
nombre1 = input("Nombre: ")
especie1 = input("Especie: ")
edad1 = int(input("Edad: "))

print("\nIngrese los datos del Animal 2")
nombre2 = input("Nombre: ")
especie2 = input("Especie: ")
edad2 = int(input("Edad: "))

# Instancias
vehiculo1 = Vehiculo(marca1, modelo1, color1)
vehiculo2 = Vehiculo(marca2, modelo2, color2)

animal1 = Animal(nombre1, especie1, edad1)
animal2 = Animal(nombre2, especie2, edad2)

print("\n")
print("=" * 50)
print("INFORMACIÓN REGISTRADA")
print("=" * 50)

Vehiculo.mostrar_categoria()

vehiculo1.mostrar_datos()
vehiculo1.hacer_sonido()

vehiculo2.mostrar_datos()
vehiculo2.hacer_sonido()

Animal.mostrar_reino()

animal1.mostrar_datos()
animal1.hacer_sonido()

animal2.mostrar_datos()
animal2.hacer_sonido()

print("\n")
print("=" * 50)
print("Interacción entre objetos")
print("=" * 50)

print(
    f"El vehículo {vehiculo1.marca} {vehiculo1.modelo} "
    f"transporta a {animal1.nombre}."
)

print(
    f"El vehículo {vehiculo2.marca} {vehiculo2.modelo} "
    f"transporta a {animal2.nombre}."
)

print("\n")
print("=" * 50)
print("Programa desarrollado por:")
print("Noah Leon")
print("=" * 50)