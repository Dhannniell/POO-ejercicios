Enunciado del Proyecto: Sistema de Gestión de Vehículos y Transporte
Descripción del Proyecto:
El proyecto consiste en el desarrollo de una aplicación para gestionar diferentes tipos de vehículos (motos, coches, aviones) en una flota de transporte. El sistema debe permitir realizar varias operaciones sobre los vehículos, incluyendo el registro, la gestión de combustible, la aceleración y el frenado, y la aplicación de diferentes comportamientos para cada tipo de vehículo. Además, se implementarán patrones de diseño como Singleton y Factory para gestionar la creación y el control de acceso a los objetos de tipo vehículo, mientras que el Observer y Strategy se utilizarán para gestionar dinámicamente la forma en que los vehículos realizan distintas acciones según su tipo.

Objetivos del Proyecto:
Aplicación de la Programación Orientada a Objetos (POO):

Definir clases base para los vehículos y clases hijas para cada tipo de vehículo (por ejemplo, Moto, Coche, Avión).
Implementar métodos para las acciones comunes a todos los vehículos, como el arranque, el freno y el control de combustible.
Aplicar el principio de encapsulamiento para proteger los atributos sensibles como el salario, combustible, y velocidad de los vehículos, utilizando modificadores de acceso.
Herencia y Polimorfismo:

Crear una jerarquía de clases donde los vehículos compartan comportamientos generales (por ejemplo, arrancar y frenar) y cada tipo de vehículo puede tener su propia implementación de estos métodos mediante el uso de polimorfismo.
Utilizar interfaces para permitir que diferentes tipos de vehículos implementen su comportamiento de forma flexible.
Patrones de Diseño Básicos:

Singleton: Implementar el patrón Singleton para asegurarse de que solo haya una instancia del sistema de gestión de vehículos, lo que permite controlar el acceso a la flota de vehículos.
Factory: Utilizar el patrón Factory para crear instancias de vehículos (moto, coche, avión) sin que el código cliente dependa de las clases específicas de los vehículos.
Composición vs Herencia:

Analizar y decidir cuándo usar la composición frente a la herencia para crear relaciones entre objetos. Por ejemplo, un Coche puede tener una relación de composición con una Radio o Motor en lugar de una relación de herencia.
Patrones de Diseño Avanzados:

Observer: Implementar el patrón Observer para que los vehículos puedan ser observados por otros componentes del sistema (como la estación de combustible o el sistema de mantenimiento), notificando eventos como cuando se queda sin combustible o cuando se necesita mantenimiento.
Strategy: Utilizar el patrón Strategy para cambiar dinámicamente el comportamiento de los vehículos, por ejemplo, diferentes estrategias de combustible para vehículos que usen gasolina, electricidad o hidrógeno.
Uso de Clases Anónimas, Internas y Lambda Expressions:

Implementar clases internas para representar comportamientos específicos dentro de un vehículo (por ejemplo, un Motor que solo tiene sentido dentro de un Coche).
Usar expresiones lambda para realizar cálculos rápidos como el consumo de combustible o el cálculo de la velocidad en función de la carga del vehículo.
Utilizar clases anónimas en situaciones donde la creación de una clase pequeña y temporal sea necesaria, como para gestionar diferentes estrategias de comportamiento en tiempo de ejecución.
Requerimientos del Sistema:
Gestión de Vehículos:

Crear una clase base Vehiculo con atributos comunes como modelo, marca, color, combustible, y métodos como acelerar(), frenar(), cargar_combustible().
Definir clases derivadas como Moto, Coche, y Avión, que implementen su propia versión de métodos como acelerar() y frenar().
Patrones de Diseño:

Singleton: Implementar una clase FlotaVehiculos que controle una única instancia de la flota y gestione el acceso a los vehículos.
Factory: Crear un VehiculoFactory que genere vehículos de diferentes tipos según se necesite.
Composición y Herencia:

El sistema debe ser capaz de componer objetos (por ejemplo, un Coche tiene un Motor y una Radio como atributos) y heredar comportamientos comunes de la clase base Vehiculo.
Patrones Avanzados:

Implementar el patrón Observer para notificar cuando un vehículo necesita mantenimiento o combustible.
Usar el patrón Strategy para gestionar diferentes estrategias de manejo o consumo de combustible según el tipo de vehículo.
Clases Anónimas y Lambda Expressions:

Usar lambda expressions para realizar cálculos como la eficiencia de combustible o la velocidad de los vehículos.
Implementar clases internas si es necesario para agrupar comportamientos específicos dentro de una clase.
Entregables del Proyecto:
Código fuente completo con la implementación de las clases base y derivadas de los vehículos.
Implementación de los patrones de diseño: Singleton, Factory, Observer y Strategy.
Documentación del código explicando el uso de la POO, encapsulamiento, herencia, polimorfismo, y patrones de diseño.
Pruebas unitarias que verifiquen el comportamiento de las clases, patrones de diseño y uso de lambdas.
Este proyecto te permitirá aplicar todos los conceptos que has aprendido sobre la Programación Orientada a Objetos y los Patrones de Diseño en un caso práctico, organizando código de manera modular, reutilizable y eficiente.
