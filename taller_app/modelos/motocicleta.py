from modelos.vehiculo import Vehiculo

# Otra clase derivada que hereda de Vehiculo
# DEMOSTRACIÓN: Herencia y Polimorfismo (implementación diferente)
class Motocicleta(Vehiculo):
    def __init__(self, marca: str, modelo: str, año: int, cilindrada: int):
        super().__init__(marca, modelo, año)
        
        # Atributo específico de Motocicleta
        self.cilindrada = cilindrada
        self.__casco_colocado = False
    
    # Implementación diferente del mismo método (polimorfismo)
    def encender(self) -> str:
        """Encendido específico para motocicletas."""
        return f"Motocicleta {self.marca} {self.modelo} {self.cilindrada}cc encendida. Sonido: Neeeooom"
    
    # Implementación diferente del mismo método (polimorfismo)
    def mover(self, distancia: int) -> str:
        """Movimiento específico para motocicletas con chequeo de seguridad."""
        if self.__casco_colocado:
            self._agregar_kilometros(distancia)
            return f"Motocicleta avanzando {distancia} km con seguridad"
        else:
            return "¡Colóquese el casco primero! (Seguridad vial)"
    
    # Método específico de Motocicleta
    def colocar_casco(self) -> str:
        """Método exclusivo de motocicletas."""
        self.__casco_colocado = True
        return f"Casco colocado en {self.marca} {self.modelo}"