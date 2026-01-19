from typing import List
from modelos.vehiculo import Vehiculo

# Clase de servicio que maneja múltiples vehículos
# DEMOSTRACIÓN: Uso de polimorfismo y encapsulación
class TallerMecanico:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.__vehiculos: List[Vehiculo] = []  # Lista privada (encapsulación)
    
    def agregar_vehiculo(self, vehiculo: Vehiculo) -> None:
        """Agrega un vehículo al taller."""
        self.__vehiculos.append(vehiculo)
        print(f"✅ {vehiculo.marca} {vehiculo.modelo} agregado al taller")
    
    def listar_vehiculos(self) -> List[Vehiculo]:
        """Devuelve copia de la lista (protección de datos)."""
        return list(self.__vehiculos)
    
    def realizar_prueba_conduccion(self) -> None:
        """Polimorfismo: todos tienen mover() pero comportamiento diferente."""
        print(f"\n🔧 {self.nombre} - Prueba de conducción:")
        for vehiculo in self.__vehiculos:
            print(f"\nProbando {vehiculo.informacion()}:")
            print(f"  - {vehiculo.encender()}")
            print(f"  - {vehiculo.mover(10)}")
    
    def buscar_por_marca(self, marca: str) -> List[Vehiculo]:
        """Filtra vehículos por marca."""
        return [v for v in self.__vehiculos if v.marca.lower() == marca.lower()]
    
    def mostrar_resumen(self) -> None:
        """Muestra resumen de todos los vehículos."""
        print(f"\n📊 Resumen del Taller {self.nombre}:")
        print(f"Total vehículos: {len(self.__vehiculos)}")
        for i, vehiculo in enumerate(self.__vehiculos, 1):
            print(f"{i}. {vehiculo.informacion()}")