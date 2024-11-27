Enunciado del Proyecto: Sistema de Gestión de Vehículos en una Flota de Transporte

Descripción del Proyecto:
El proyecto consiste en desarrollar un sistema de gestión para una flota de vehículos utilizados en una empresa de transporte. El sistema debe permitir realizar operaciones como la creación de vehículos, la gestión de sus atributos (modelo, marca, color), y la ejecución de acciones como el llenado de combustible, la aceleración y el frenado. Además, el sistema debe ser capaz de gestionar vehículos de distintos tipos (motos, coches, camiones), aplicando diferentes comportamientos de acuerdo a cada tipo, como el uso de distintas estrategias para el consumo de combustible.

Objetivos del Proyecto:
Aplicación de la Programación Orientada a Objetos (POO):

Definir una clase base Vehiculo con atributos comunes (como modelo, marca, color) y métodos generales (por ejemplo, acelerar(), frenar(), cargar_combustible()).
Crear clases derivadas, como Moto, Coche y Camion, que hereden de la clase base Vehiculo y tengan implementaciones específicas para cada tipo de vehículo (por ejemplo, diferentes formas de acelerar o frenar según el tipo).
Uso de Encapsulamiento y Herencia:

Los atributos sensibles como el combustible y velocidad deben estar encapsulados para proteger su acceso directo. Se usará herencia para crear relaciones entre la clase base Vehiculo y sus clases hijas (Moto, Coche, Camion), de modo que compartan comportamiento común.
Polimorfismo y Métodos Abstractos:

Implementar polimorfismo para permitir que los métodos como acelerar() y frenar() tengan comportamientos diferentes según el tipo de vehículo.
Usar clases abstractas para definir métodos que deben ser implementados por todas las clases hijas, asegurando que cada tipo de vehículo tenga su propia implementación de ciertas acciones (como el frenado o aceleración).
Patrones de Diseño:

Singleton: Implementar un patrón Singleton para la clase GestorFlota que asegure que solo haya una instancia encargada de gestionar la flota de vehículos. Este patrón asegura que no haya múltiples instancias que gestionen los mismos vehículos.
Factory: Usar un patrón Factory para crear instancias de vehículos (moto, coche, camión) de manera flexible sin que el código cliente dependa directamente de las clases específicas.
Patrones de Diseño Avanzados:

Strategy: Implementar el patrón Strategy para manejar diferentes estrategias de consumo de combustible o diferentes métodos de aceleración, según el tipo de vehículo (por ejemplo, vehículos eléctricos vs vehículos de combustión interna).
Observer: Usar el patrón Observer para notificar a otros sistemas del estado del vehículo, como cuando el combustible está bajo o cuando se necesita mantenimiento.
Uso de Clases Anónimas, Internas y Lambda Expressions:

Implementar clases anónimas o internas para encapsular comportamientos específicos dentro de un vehículo, como una clase interna que maneje el sistema de frenado de un vehículo.
Utilizar lambda expressions para realizar cálculos rápidos, como determinar el consumo de combustible en función de la velocidad o calcular la aceleración en tiempo real.
Requerimientos del Sistema:
Gestión de Vehículos:

Crear una clase base Vehiculo con métodos comunes (acelerar(), frenar(), cargar_combustible()) y atributos (modelo, marca, color).
Crear las clases hijas Moto, Coche y Camion, que hereden de la clase base y redefinan los métodos de acuerdo a su tipo.
Patrones de Diseño:

Singleton: Implementar un sistema centralizado para gestionar la flota de vehículos mediante el patrón Singleton.
Factory: Crear una clase VehiculoFactory que genere vehículos de diferentes tipos (moto, coche, camión) sin que el cliente tenga que preocuparse por la implementación concreta.
Patrones Avanzados:

Strategy: Implementar estrategias específicas de consumo de combustible según el tipo de vehículo (por ejemplo, vehículos eléctricos que usan una estrategia de carga rápida).
Observer: Utilizar el patrón Observer para notificar a un sistema centralizado cuando un vehículo necesita mantenimiento o tiene bajo nivel de combustible.
Clases Anónimas y Lambda Expressions:

Implementar clases internas para funcionalidades específicas de los vehículos (por ejemplo, un sistema de frenos de un coche).
Usar expresiones lambda para realizar cálculos rápidos como la eficiencia de combustible en función de la carga del vehículo.
Entregables del Proyecto:
Código fuente completo con las clases base y derivadas de vehículos.
Implementación de los patrones de diseño Singleton, Factory, Strategy y Observer.
Documentación detallada del código, explicando cómo se implementaron los patrones de diseño y la POO en el sistema.
Pruebas unitarias que verifiquen el comportamiento de las clases, los patrones de diseño y el uso de lambdas.
Resumen:
Este proyecto te permitirá aplicar conceptos clave de la Programación Orientada a Objetos (POO), como herencia, polimorfismo y encapsulamiento, junto con patrones de diseño como Singleton, Factory, Strategy y Observer en un caso realista de gestión de vehículos en una flota de transporte. Se busca crear un sistema modular y flexible que gestione diferentes tipos de vehículos, adaptándose a las necesidades cambiantes del negocio.
