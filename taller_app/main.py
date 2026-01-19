from modelos.automovil import Automovil
from modelos.motocicleta import Motocicleta
from servicios.taller import TallerMecanico

def main():
    """
    Programa principal que demuestra los conceptos de POO:
    - Herencia: Automovil y Motocicleta heredan de Vehiculo
    - Encapsulación: Atributos privados como __kilometraje
    - Polimorfismo: Métodos encender() y mover() con implementaciones diferentes
    - Abstracción: Clase base Vehiculo con métodos abstractos
    """
    
    print("=" * 20)
    print("DEMOSTRACIÓN ")
    print("=" * 20)
    
    # Crear instancias de las clases
    print("\n🚗 CREANDO VEHÍCULOS:")
    
    # Crear un automóvil
    auto1 = Automovil("Toyota", "Corolla", 2022, 4, "Gasolina")
    print(f"Automóvil creado: {auto1.informacion()}")
    
    # Crear una motocicleta
    moto1 = Motocicleta("Yamaha", "YZF-R3", 2023, 321)
    print(f"Motocicleta creada: {moto1.informacion()}")
    
    # Crear otro automóvil
    auto2 = Automovil("Ford", "Focus", 2021, 5, "Diésel")
    print(f"Automóvil creado: {auto2.informacion()}")
    
    # Crear taller mecánico
    print("\n🏢 CREANDO TALLER MECÁNICO:")
    taller = TallerMecanico("Taller POO Expert")
    
    # Agregar vehículos al taller
    taller.agregar_vehiculo(auto1)
    taller.agregar_vehiculo(moto1)
    taller.agregar_vehiculo(auto2)
    
    # Demostrar polimorfismo con prueba de conducción
    taller.realizar_prueba_conduccion()
    
    # Demostrar uso de métodos específicos de cada clase
    print("\n🎯 MÉTODOS ESPECÍFICOS DE CADA CLASE:")
    print(f"Auto: {auto1.abrir_maletero()}")
    
    # Para la moto, necesitamos colocar casco primero
    print(f"Moto: {moto1.colocar_casco()}")
    print(f"Moto: {moto1.mover(5)}")
    
    # Demostrar encapsulación
    print("\n🔒 DEMOSTRACIÓN DE ENCAPSULACIÓN:")
    print(f"Kilometraje auto (vía getter): {auto1.obtener_kilometraje()} km")
    
    # Intentar acceder directamente al atributo privado (no permitido)
    # print(auto1.__kilometraje)  # Esto generaría un AttributeError
    
    # Buscar vehículos por marca
    print("\n🔍 BUSCANDO VEHÍCULOS POR MARCA 'Toyota':")
    toyotas = taller.buscar_por_marca("Toyota")
    for vehiculo in toyotas:
        print(f"  - {vehiculo.informacion()}")
    
    # Mostrar resumen final
    taller.mostrar_resumen()
    
    print("\n" + "=" * 50)
    print("✅ DEMOSTRACIÓN COMPLETADA")
    print("=" * 50)

if __name__ == "__main__":
    main()