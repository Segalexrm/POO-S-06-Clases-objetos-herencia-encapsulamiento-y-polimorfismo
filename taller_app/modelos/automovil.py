from modelos.vehiculo import Vehiculo

# Clase derivada que hereda de Vehiculo
# DEMOSTRACIÓN: Herencia y Polimorfismo
class Automovil(Vehiculo):
    def __init__(self, marca: str, modelo: str, año: int, puertas: int, combustible: str):
        # Llamada al constructor de la clase padre (herencia)
        super().__init__(marca, modelo, año)
        
        # Atributos específicos de Automovil
        self.puertas = puertas
        self.combustible = combustible
        self.__estado_motor = "apagado"  # Atributo privado
    
    # Implementación del método abstracto (polimorfismo)
    def encender(self) -> str:
        """Encendido específico para automóviles."""
        if self.__estado_motor == "apagado":
            self.__estado_motor = "encendido"
            return f"Automóvil {self.marca} {self.modelo} encendido. Sonido: Brrum brrum"
        else:
            return f"El automóvil ya está encendido"
    
    # Implementación del método abstracto (polimorfismo)
    def mover(self, distancia: int) -> str:
        """Movimiento específico para automóviles."""
        if self.__estado_motor == "encendido":
            self._agregar_kilometros(distancia)  # Uso de método protegido
            return f"Automóvil moviéndose {distancia} km. Quedan {self.obtener_kilometraje()} km totales"
        else:
            return "Primero debe encender el automóvil"
    
    # Método específico de Automovil
    def abrir_maletero(self) -> str:
        """Método exclusivo de automóviles."""
        return f"Maletero del {self.marca} {self.modelo} abierto"