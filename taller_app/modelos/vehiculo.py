from abc import ABC, abstractmethod

# Clase base abstracta que representa un vehículo general
# DEMOSTRACIÓN: Abstracción y Encapsulación
class Vehiculo(ABC):
    def __init__(self, marca: str, modelo: str, año: int):
        # Atributos públicos
        self.marca = marca
        self.modelo = modelo
        self.año = año
        
        # Atributo privado (encapsulación) - estado interno protegido
        self.__kilometraje = 0
    
    # Getter para acceder al kilometraje de manera controlada
    def obtener_kilometraje(self) -> int:
        """Método público para consultar el kilometraje (encapsulación)."""
        return self.__kilometraje
    
    # Método protegido para modificar el kilometraje internamente
    def _agregar_kilometros(self, km: int) -> None:
        """Método interno para actualizar kilometraje."""
        if km > 0:
            self.__kilometraje += km
        else:
            print("Error: Los kilómetros deben ser positivos")
    
    @abstractmethod
    def encender(self) -> str:
        """Método abstracto que debe implementarse en clases hijas (polimorfismo)."""
        pass
    
    @abstractmethod
    def mover(self, distancia: int) -> str:
        """Método abstracto para mover el vehículo."""
        pass
    
    def informacion(self) -> str:
        """Método común para todos los vehículos."""
        return f"{self.marca} {self.modelo} ({self.año}) - {self.obtener_kilometraje()} km"