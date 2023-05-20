class Vehiculo:
    def __init__(self, _marca, _modelo, _num_ruedas):
        self.marca = _marca
        self.modelo = _modelo
        self.num_ruedas = _num_ruedas
    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.num_ruedas} ruedas"

class Automovil(Vehiculo):
    def __init__(self, _marca, _modelo, _num_ruedas, _velocidad, _cilindrada):
        super().__init__(_marca, _modelo, _num_ruedas)
        self.velocidad = _velocidad
        self.cilindrada = _cilindrada
    def __str__(self):
        return f"{super().__str__()}, {self.velocidad} Km/h, {self.cilindrada} cc"
    
class Particular(Automovil):
    def __init__(self, _marca, _modelo, _num_ruedas, _velocidad, _cilindrada, _num_puestos):
        super().__init__(_marca, _modelo, _num_ruedas, _velocidad, _cilindrada)
        self.num_puestos = _num_puestos
    def __str__(self):
        return f"{super().__str__()}, Puestos: {self.num_puestos}"

class Carga(Automovil):
    def __init__(self, _marca, _modelo, _num_ruedas, _velocidad, _cilindrada, _peso_carga):
        super().__init__(_marca, _modelo, _num_ruedas, _velocidad, _cilindrada)
        self.peso_carga = _peso_carga
    def __str__(self):
        return f"{super().__str__()}, Carga: {self.peso_carga}"

class Bicicleta (Vehiculo):
    def __init__(self, _marca, _modelo, _num_ruedas, _tipo_bicicleta):
        super().__init__(_marca, _modelo, _num_ruedas)
        self.tipo_bicicleta = _tipo_bicicleta
    def __str__(self):
        return f"{super().__str__()}, Tipo: {self.tipo_bicicleta}"

class Motocicleta (Bicicleta):
    def __init__(self, _marca, _modelo, _num_ruedas, _tipo_bicicleta, _motor, _cuadro,  _num_radios):
        super().__init__(_marca, _modelo, _num_ruedas, _tipo_bicicleta)
        self.cuadro = _cuadro
        self.num_radios = _num_radios
        self.motor = _motor
    def __str__(self):
        return f"{super().__str__()}, Motor: {self.motor}, Cuadro: {self.cuadro}, Nro. radios: {self.num_radios}"

#Parte 1
def registro_vehiculos():
    num_vehiculos = int(input('Cuantos vehículos desea insertar: '))
    vehiculos = []

    for i in range(1, num_vehiculos + 1):
        print(f"Datos del automóvil {i}")
        marca = input("Inserte la marca del automóvil: ")
        modelo = input("Inserte el modelo: ")
        ruedas = int(input("Inserte el número de ruedas: "))
        velocidad = int(input("Inserte la velocidad en km/h: "))
        cilindrada = int(input("Inserte el cilindraje en cc: "))

        automovil = Automovil(marca, modelo, ruedas, velocidad, cilindrada)
        vehiculos.append(automovil)

    print("\nImprimiendo por pantalla los vehículos:")
    for vehiculo in vehiculos:
        print(vehiculo)


registro_vehiculos()

#Parte2
print("_______________________________________________________")
particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "DobleViga", 21)

print(particular)
print(carga)
print(bicicleta)
print(motocicleta)

print("\nVerificar la relación que existe de la instancia motocicleta con: Vehículo, Automóvil, Particular, Carga, Bicicleta y Motocicleta.")
print(f"Motocicleta es instancia con relación a Vehículo: {isinstance(motocicleta, Vehiculo)}")
print(f"Motocicleta es instancia con relación a Automovil: {isinstance(motocicleta, Automovil)}")
print(f"Motocicleta es instancia con relación a Vehículo particular: {isinstance(motocicleta, Particular)}")
print(f"Motocicleta es instancia con relación a Vehículo de Carga: {isinstance(motocicleta, Carga)}")
print(f"Motocicleta es instancia con relación a Bicicleta: {isinstance(motocicleta, Bicicleta)}")
print(f"Motocicleta es instancia con relación a Motocicleta: {isinstance(motocicleta, Motocicleta)}")
